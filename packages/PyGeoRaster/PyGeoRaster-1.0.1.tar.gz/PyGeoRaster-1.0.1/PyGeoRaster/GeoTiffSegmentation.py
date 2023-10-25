# encoding=utf8
import os
import glob
from osgeo import gdal

"""geo tiff 分段和合并"""
class GeoTiffSegmentation:
    def __init__(self) -> None:
        pass

    """获取遥感影像地理范围"""
    def get_extent(self,img_file):
        gdal.AllRegister()
        ds = gdal.Open(img_file)
        img_data = ds.ReadAsArray()
        if len(img_data.shape)==3:
            bounds,rows, cols = img_data.shape
        elif len(img_data.shape)==2:
            rows, cols = img_data.shape
        else:
            rows,cols=img_data.shape[:-2]
        # 获取图像角点坐标
        gt = ds.GetGeoTransform()
        minx = gt[0]
        maxy = gt[3]
        maxx = gt[0] + gt[1] * cols
        miny = gt[3] + gt[5] * rows
        return (minx, maxy, maxx, miny)

    def get_xy_to_rowcol(self,trans,x,y):
        ul_x= trans[0]
        ul_y = trans[3]
        x_dist = trans[1]
        y_dist = trans[5]
        row = int((x - ul_x) / x_dist)
        col = -int((ul_y - y) / y_dist)
        return row, col

    def get_rowcol_to_xy(self,trans,row,col):
        px = trans[0] + col * trans[1] + row * trans[2]
        py = trans[3] + col * trans[4] + row * trans[5]
        return px, py  

    def load_img(self,img_file):
            gdal.AllRegister()
            image=gdal.Open(img_file)
            img_w=image.RasterXSize
            img_h=image.RasterYSize
            img_geo_trans=image.GetGeoTransform()
            img_proj=image.GetProjection()
            img_data=image.ReadAsArray(0,0,img_w,img_h)
            bands=image.RasterCount
            del image
            return img_proj,img_geo_trans,img_data,bands

    def write_img(self,img_file,img_proj,geotrans,img_data):
        if 'int8' in img_data.dtype.name:
            datatype=gdal.GDT_Byte
        elif 'int6' in img_data.dtype.name:
            datatype=gdal.GDT_UInt16
        else:
            datatype=gdal.GDT_Float32

        if len(img_data.shape)==3:
            img_bands,img_h,img_w=img_data.shape
        elif len(img_data.shape)==2:
            img_bands, (img_h, img_w) =1, img_data.shape
        else:
            pass

        if img_h==0 or img_w==0:
            return

        gdal.AllRegister()
        driver = gdal.GetDriverByName("GTiff")
        dataset = driver.Create(img_file,int(img_w),int(img_h),int(img_bands), datatype)

        if(dataset!=None):
            dataset.SetGeoTransform(geotrans)   # 写入仿射变换参数
            dataset.SetProjection(img_proj)

        if img_bands==1:
            dataset.GetRasterBand(1).WriteArray(img_data)
        else:
            for i in range(img_bands):
                dataset.GetRasterBand(1+i).WriteArray(img_data[i])

        del dataset
    
    """tiff图片拆分的指定大小的块
    #     Args:
    #         img_file: 待分块影像文件
    #                    str
    #         split_folder: 分块结果保存文件夹
    #                    str
    #         cell:块的大小
    #           int
    """
    def split_img(self,img_file,split_folder,cell):
        img_proj,img_geotrans,img_data,img_bands=self.load_img(img_file)
        # 判断波段数
        if img_bands > 1:
            raster_num, img_rows, img_cols = img_data.shape
        else:
            img_rows, img_cols = img_data.shape

        n_row=img_rows//cell
        n_col=img_cols//cell

        if img_rows%cell!=0:
            n_row=n_row+1
        if img_cols%cell!=0:
            n_col=n_col+1

        cnt=0
        for i in range(n_row):
            for j in range(n_col):
                block_img_name=os.path.join(split_folder, '{}_{}.tif'.format(i,j))
 
                plg_row_min = i * cell # 第几行
                plg_col_min = j * cell # 第列行

                # 如果起始点 + 块大小超出了影像范围，就取最后的块大小影像
                if plg_row_min + cell > img_rows:
                    plg_row_min = img_rows - cell
                if plg_col_min + cell > img_cols:
                    plg_col_min = img_cols - cell

                #计算每一个分块的坐标信息
                geo_x, geo_y = self.get_rowcol_to_xy(img_geotrans,plg_row_min, plg_col_min)
                masked_tran = list(img_geotrans)
                masked_tran[0] = geo_x
                masked_tran[3] = geo_y

                block_img=img_data[:,plg_row_min: plg_row_min+cell, plg_col_min: plg_col_min + cell]
                self.write_img(block_img_name,img_proj,masked_tran,block_img)
                cnt=cnt+1
        return cnt
    
    """ tiff影像合并
    Args:
        images_folder: 待合并影像文件夹
                str
        save_folder: 合并结果保存路径
                str
    """
    def imgs_merge(self,image_folder,save_folder):
        os.chdir(image_folder)
        in_files = glob.glob('*.tif')
        # 通过两两比较大小,将最终符合条件的四个角点坐标保存，
        # 即为拼接图像的四个角点坐标
        
        minX, maxY, maxX, minY = self.get_extent(in_files[0])
        for fn in in_files[1:]:
            minx, maxy, maxx, miny = self.get_extent(fn)
            minX = min(minX, minx)
            maxY = max(maxY, maxy)
            maxX = max(maxX, maxx)
            minY = min(minY, miny)
        # 获取输出图像的行列数
        in_ds = gdal.Open(in_files[0])
        gt = in_ds.GetGeoTransform()
        im_bands=in_ds.RasterCount
        
        #计算合并后的图像大小
        sx,sy=self.get_xy_to_rowcol(gt,minX,minY)
        ex,ey=self.get_xy_to_rowcol(gt,maxX,maxY)
        rows=abs(ex-sx)
        cols=abs(ey-sy)

        # 创建输出图像
        driver = gdal.GetDriverByName('GTiff')
        out_ds = driver.Create(save_folder, rows, cols, im_bands)
        out_ds.SetProjection(in_ds.GetProjection())

        gt = list(in_ds.GetGeoTransform())
        gt[0], gt[3] = minX, maxY
        out_ds.SetGeoTransform(gt)

        for fn in in_files:
            in_ds = gdal.Open(fn)
            w=in_ds.RasterXSize
            h=in_ds.RasterYSize
            trans = gdal.Transformer(in_ds, out_ds, [])
            success, xyz = trans.TransformPoint(False, 0, 0)
            _x, _y, z = map(float, xyz)

            x=int(_x)
            y=int(_y)

            if _x%w!=0:
                x=x+1
            if _y%h!=0:
                y=y+1

            if (x+w)>rows:
                x=rows-w
  
            if (h+y)>cols:
                y=cols-h

            if im_bands > 1:
                for i in range(im_bands):
                    img_data = in_ds.GetRasterBand(i + 1).ReadAsArray()
                    out_ds.GetRasterBand(i + 1).WriteArray(img_data,x,y)
            else:
                img_data = in_ds.GetRasterBand(1).ReadAsArray()
                colortable = gdal.ColorTable()
                colortable.CreateColorRamp(1, (255, 0, 0), 2, (0, 0, 255))
                outband = out_ds.GetRasterBand(1)
                outband.SetColorTable(colortable)
                outband.WriteArray(img_data, x, y)
        del in_ds, out_ds
        return len(in_files)