from setuptools import setup, find_packages

setup(
    name="uledgersdk",
    version="0.1.3",
    packages=find_packages(),
    install_requires=[
        "requests",  
        "ecdsa",
        "datetime",
        "urllib3"
        "cryptography"
    ],
    author="Carlomagno Amaya",
    author_email="carlomagno@uledger.io",
    description="ULedger's Python SDK",
    license="MIT",
    keywords="uledger sdk api",
    project_urls={ 
        "Documentation": "https://docs.uledger.io/python"
    },
    classifiers=[  
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
