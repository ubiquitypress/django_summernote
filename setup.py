#!/usr/bin/env python

from distutils.core import setup
kwargs = {
	'name': 'django_summernote',
	'version': '0.0.1',
	'description': "Modified version of Summernote.",
	'keywords': 'Ubiquity Press Django Summernote',
	'author': 'UP Tech',
	'author_email': 'tech@ubiquitypress.com',
	'url': 'https://github.com/ubiquitypress/django_summernote',
	'license': 'unlicensed - do not distribute',
	# setuptools/pip args
	
	'zip_safe': False, 		 	
	'install_requires': [

	],
}
setup(**kwargs)
