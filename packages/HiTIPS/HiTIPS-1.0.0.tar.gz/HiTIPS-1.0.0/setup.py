from setuptools import setup, find_packages

setup(
    name='HiTIPS',
    version='1.0.0',
    author='Adib Keikhosravi',
    author_email='adib.k.bme@gmail.com',
    description='High throughput image processing software for analyzing cell dynamics and DNA/RNA',
    packages=find_packages(),
    install_requires=[
        'pyqt5',
        'scipy',
        'pandas',
        'pillow',
        'matplotlib',
        'imageio',
        'tifffile',
        'scikit-image==0.18.3',
        'btrack',
        'qimage2ndarray',
        'aicsimageio',
        'cellpose',
        'opencv-python-headless',
        'deepcell',
        'hmmlearn',
        'aicsimageio[nd2]',
        'nd2reader',
        'joblib',
        'tensorflow',
        'scikit-learn',
        'dask',
        'imaris-ims-file-reader',
        'imagej',
        'jnius'
    ],
    entry_points={
        'console_scripts': [
            'HiTIPS=HiTIPS.HiTIPS:main',
        ],
    },
)

