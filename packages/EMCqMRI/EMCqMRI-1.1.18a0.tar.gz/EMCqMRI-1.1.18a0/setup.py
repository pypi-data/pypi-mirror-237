import setuptools

try:
    with open("README.md", "r") as fh:
        long_description = fh.read()
except FileNotFoundError:
    print("No readme file found")
    long_description = 'Project without long description'

# print(long_description)


setuptools.setup(name="EMCqMRI", # Replace with your own username
    version="1.1.18a",
    author="Emanoel R. Sabidussi",
    author_email="e.ribeirosabidussi@erasmusmc.nl",
    description="A distribution of a general tool for training and inference of QMRI models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/e.ribeirosabidussi/emcqmri",
    packages=setuptools.find_packages(),
    install_requires=['h5py', 'numpy >=1.19.0', 'scipy >=1.2.1', 'matplotlib >=3.3.2', 'PyQt5 >=5.15.1', 'progress >=1.5', 'monai', 'pytorch-ignite', 'pillow', 'dipy==1.7.0', 'fury ==0.9.0', 'tensorboard'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
    )
