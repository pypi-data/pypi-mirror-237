from setuptools import setup
from setuptools_rust import Binding, RustExtension

from pathlib import Path

ROOT_DIR = Path(__file__).parent
README = (ROOT_DIR / "README.md").read_text()

VERSION = {}
with open(ROOT_DIR / "snapatac2/_version.py") as fp:
    exec(fp.read(), VERSION)

setup(
    name="snapatac2",
    description='SnapATAC2: Single-cell epigenomics analysis pipeline',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://kzhang.org/SnapATAC2/', 
    author='Kai Zhang',
    author_email='kai@kzhang.org',
    license='MIT',
    version=VERSION['__version__'],
    rust_extensions=[
        RustExtension("snapatac2._snapatac2", debug=False, binding=Binding.PyO3),
    ],
    packages=[
        "snapatac2",
        "snapatac2.preprocessing",
        "snapatac2.tools",
        "snapatac2.metrics",
        "snapatac2.plotting",
        "snapatac2.export",
    ],
    zip_safe=False,
    python_requires=">=3.8, <3.12",
    install_requires=[
        "anndata>=0.8.0, <0.10.0",
        "kaleido",
        "multiprocess",
        "MACS3==3.0.0b3",
        "natsort",
        "numpy>=1.16.0",
        "pandas>=1.0",
        "plotly>=5.6.0",
        "polars>=0.18.15, <0.20.0",
        "pooch>=1.6.0",
        "igraph>=0.10.3",
        "pynndescent",
        "pyarrow",
        "pyfaidx",
        "rustworkx",
        "scipy>=1.4",
        "scikit-learn>=1.0",
        "tqdm>=4.62",
        "typing_extensions",
        "umap-learn>=0.5.0",
    ],
    extras_require={
        'extra': ['scanorama>=1.7.3', 'harmonypy>=0.0.9', 'xgboost>=1.4'],
        'recommend': ['scanpy>=1.9', 'scvi-tools>=1.0'],
        'all': ['snapatac2[extra]', 'snapatac2[recommend]']
    }
)
