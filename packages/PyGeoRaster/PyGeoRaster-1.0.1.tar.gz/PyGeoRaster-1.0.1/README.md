# PyGeoRaster

#### 介绍
tiff影像分块和合并等

#### 安装教程

1.  本地安装：python setup.py install
2.  在线安装：pip install PyGeoRaster
3.  源码安装：pip install https://gitee.com/bouyei/py-geo-raster

#### 使用说明
    import sys
    from PyGeoRaster import GeoTiffSegmentation

    def main(args):
        geoRaster=GeoTiffSegmentation()
        geoRaster.split_img("E:\\40_tif\\水库边部分区域.tif","E:\\40_tif\\rx",1024)
        geoRaster.imgs_merge("E:\\40_tif\\rx","E:\\40_tif\\rx.tif")

    if __name__ == "__main__":
        main(sys.argv)
