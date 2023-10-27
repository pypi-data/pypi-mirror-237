from setuptools import setup, find_packages

setup(
    name='torch_sparsify',
    version="1.0",
    url='https://github.com/MingxuanZhangPurdue/pytorch_sparsify',
    author='Mingxuan Zhang',
    author_email='zhan3692@purdue.edu',
    packages=find_packages(),
    install_requires=['torch', 'numpy', 'scipy'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)