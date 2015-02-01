try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'Tiny script to count estimate for speeded up (or down) video/audio/etc content.',
	'author': '23ua',
	'url': '',
	'download_url': '',
	'author_email': 'artefacter@gmail.com',
	'version': '0.1',
	'install_requires': ['plumbum'],
	'packages': ['changespeed'],
	'scripts': ['changespeed/changespeed.py'],
	'name': 'changespeedpy'
}

setup(**config)
