# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
# from pip.req import parse_requirements

try: # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements

version = '0.0.1'
# requirements = parse_requirements("requirements.txt", session="")
# https://discuss.erpnext.com/t/solved-command-python-setup-py-egg-info-failed-with-error-code-1/44487

with open('requirements.txt') as f:
	install_requires= f.read().strip().split('\n')
setup(
	name='title_links',
	version=version,
	description='Links using DocType title instead of name as Description',
	author='MaxMorais',
	author_email='max.morais.dmm@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires,
	#dependency_links=[str(ir._link) for ir in requirements if ir._link]
)
