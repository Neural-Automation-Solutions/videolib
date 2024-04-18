from setuptools import setup, find_packages

setup(
  name='videolib',
  version='1.0.1',
  package=find_packages(),
  install_requires=[
	'opencv-python',
	'numpy',
	'zmq',
  ]
)
