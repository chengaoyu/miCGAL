from setuptools import setup, find_packages

setup(name='micgal',
      version='0.0.1',
      description='A medical imaging computational geometry and algotihms library based on the python binding of CGAL.',
      url='https://github.com/chengaoyu/miCGAL',
      author='Chen Gaoyu',
      author_email='chengaoyu2013@gmail.com',
      packages=find_packages('src/python'),
      package_dir={'': 'src/python'},
      scripts=[],
      zip_safe=False)