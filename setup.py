# coding=utf-8
"""
appinstance
Active8 (04-03-15)
license: GNU-GPL2
"""
from setuptools import setup
setup(name='appinstance',
      version='27',
      description='Check if an app with the same name is running, supports parameters.',
      url='https://github.com/erikdejonge/appinstance',
      author='Erik de Jonge',
      author_email='erik@a8.nl',
      license='GPL',
      packages=['appinstance'],
      zip_safe=True,
      #install_requires=['psutil'],
      classifiers=[
          "Programming Language :: Python",
          "Programming Language :: Python :: 3",
          "Development Status :: 4 - Beta ",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
          "Operating System :: POSIX",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "Topic :: System",
      ], requires=['netifaces', 'future', 'pygments'])
