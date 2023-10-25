from setuptools import find_packages, setup

setup(
    name="PyGeoRaster",
    version="1.0.1",
    author="bouyei",
    author_email="453840293@qq.com",
    description="tiff split or merge",
    long_description="tiff segmentation or merge library etc",
    keywords=["geo", "tiff","img raster","segmentation"],
    url="https://gitee.com/bouyei/py-geo-raster",
    license="MIT License",
    packages=find_packages(exclude="sample"),
    install_requires=["gdal"],
)