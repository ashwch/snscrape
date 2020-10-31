import importlib_metadata


try:
	__version__ = importlib_metadata.version('snscrape')
except importlib_metadata.PackageNotFoundError:
	__version__ = None
