from distutils.core import setup
from setuptools import find_packages

with open("README.rst", "r") as f:
  long_description = f.read()

setup(name='LanyData',  # 包名
      version='0.0.6',  # 版本号
      description='A small package',
      long_description=long_description,
      author='weif',
      author_email='2658133323@qq.com',
      url='https://mp.weixin.qq.com/s/9FQ-Tun5FbpBepBAsdY62w',
      install_requires=[],
      license='MIT License',
      packages=find_packages(),
      platforms=["all"],
      classifiers=[
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Natural Language :: Chinese (Simplified)',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3.11',
          'Topic :: Software Development :: Libraries'
      ],
      )

"""
[bumpversion]
current_version = 0.0.6
commit = True
files = LanyData/__init__.py
tag = True
tag_name = {new_version}

[aliases]
release = sdist bdist_wheel

[bdist_wheel]
universal = 1
"""