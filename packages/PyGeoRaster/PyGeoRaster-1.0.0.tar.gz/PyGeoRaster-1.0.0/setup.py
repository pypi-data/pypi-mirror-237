from setuptools import find_packages, setup

setup(
    name="PyGeoRaster",
    version="1.0.0",
    author="bouyei",
    author_email="453840293@qq.com",
    description="tiff split or merge",
    long_description="tiff split or merge library",
    keywords="geo tiff img raster",
    url="https://gitee.com/bouyei/py-geo-raster",
    packages=find_packages(),
    install_requires=["gdal"]
)