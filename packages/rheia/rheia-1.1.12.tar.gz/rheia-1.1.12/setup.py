import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(name='rheia',
      version='1.1.12',
      description='Robust design optimization of renewable Hydrogen and dErIved energy cArrier systems',
      url='https://github.com/rheia-framework/RHEIA',
      author='Diederik Coppitters, Panagiotis Tsirikoglou, Ward De Paepe, Konstantinos Kyprianidis, Anestis Kalfas, Francesco Contino',
      author_email='rheia.framework@gmail.com',
      package_dir={"": "src"},
      packages= setuptools.find_packages(where="src"),
      classifiers=[
                "Programming Language :: Python :: 3",
                "License :: OSI Approved :: MIT License",
                "Operating System :: OS Independent",
      ],       
      install_requires=[
      'deap>=1.4.1',
      'h5py>=3.9.0',
      'matplotlib>=3.7.2',
      'numpy>=1.24.3',
      'pandas>=2.0.3',
      'pvlib>=0.10.2',
      'pyDOE>=0.3.8',
      'scipy>=1.11.1',
      'sobolsequence>=0.2.1',
      ],
      python_requires = ">=3.10",
      include_package_data=True,
      zip_safe=False)