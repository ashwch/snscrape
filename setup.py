import ast

import setuptools


def get_info(filename):
    """Parse input file and return dict containing variables and their values."""
    try:
        Constant = ast.Constant
    except AttributeError:
        Constant = ast.Str
    info = {}
    with open(filename) as _file:
        data = ast.parse(_file.read())
        for node in data.body:
            if type(node) != ast.Assign:
                continue
            if type(node.value) not in [
                ast.Str,
                ast.Num,
                Constant,
            ]:
                continue
            name = None
            for target in node.targets:
                name = target.id
            if type(node.value) in [ast.Str, Constant]:
                info[name] = node.value.s
            elif type(node.value) == ast.Num:
                info[name] = node.value.n
    return info


file_with_packageinfo = "snscrape/version.py"
info = get_info(file_with_packageinfo)

__version__ = info.get("__version__", "0.0.0")


setuptools.setup(
	name = 'snscrape',
	version=__version__,
	description = 'A social networking service scraper',
	author = 'JustAnotherArchivist',
	url = 'https://github.com/JustAnotherArchivist/snscrape',
    include_package_data=True,
	classifiers = [
		'Development Status :: 4 - Beta',
		'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
		'Programming Language :: Python :: 3.6',
	],
	packages = ['snscrape', 'snscrape.modules'],
	install_requires = [
		'requests[socks]',
		'lxml',
		'backports.cached_property',
		'dataclasses',
		'beautifulsoup4',
		'importlib_metadata',
		'pytz; python_version < "3.7.0"',
	],
	python_requires = '~=3.6',
	extras_require = {
		'test': ['coverage'],
	},
	entry_points = {
		'console_scripts': [
			'snscrape = snscrape._cli:main',
		],
	},
)
