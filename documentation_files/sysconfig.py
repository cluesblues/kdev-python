#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Python's configuration information
"""
def get_config_vars(ESCargs):
	"""
	With no arguments, return a dictionary of all configuration variables
	relevant for the current platform.
	
	With arguments, return a list of values that result from looking up each
	argument in the configuration variable dictionary.
	
	For each argument, if the value is not found, return ``None``.
	
	
	"""
	pass
	
def get_config_var(name):
	"""
	Return the value of a single variable *name*. Equivalent to
	``get_config_vars().get(name)``.
	
	If *name* is not found, return ``None``.
	
	Example of usage::
	
	>>> import sysconfig
	>>> sysconfig.get_config_var('Py_ENABLE_SHARED')
	0
	>>> sysconfig.get_config_var('LIBDIR')
	'/usr/local/lib'
	>>> sysconfig.get_config_vars('AR', 'CXX')
	['ar', 'g++']
	
	
	Installation paths
	------------------
	
	Python uses an installation scheme that differs depending on the platform and on
	the installation options.  These schemes are stored in :mod:`sysconfig` under
	unique identifiers based on the value returned by :const:`os.name`.
	
	Every new component that is installed using :mod:`distutils` or a
	Distutils-based system will follow the same scheme to copy its file in the right
	places.
	
	Python currently supports seven schemes:
	
	- *posix_prefix*: scheme for Posix platforms like Linux or Mac OS X.  This is
	the default scheme used when Python or a component is installed.
	- *posix_home*: scheme for Posix platforms used when a *home* option is used
	upon installation.  This scheme is used when a component is installed through
	Distutils with a specific home prefix.
	- *posix_user*: scheme for Posix platforms used when a component is installed
	through Distutils and the *user* option is used.  This scheme defines paths
	located under the user home directory.
	- *nt*: scheme for NT platforms like Windows.
	- *nt_user*: scheme for NT platforms, when the *user* option is used.
	- *os2*: scheme for OS/2 platforms.
	- *os2_home*: scheme for OS/2 patforms, when the *user* option is used.
	
	Each scheme is itself composed of a series of paths and each path has a unique
	identifier.  Python currently uses eight paths:
	
	- *stdlib*: directory containing the standard Python library files that are not
	platform-specific.
	- *platstdlib*: directory containing the standard Python library files that are
	platform-specific.
	- *platlib*: directory for site-specific, platform-specific files.
	- *purelib*: directory for site-specific, non-platform-specific files.
	- *include*: directory for non-platform-specific header files.
	- *platinclude*: directory for platform-specific header files.
	- *scripts*: directory for script files.
	- *data*: directory for data files.
	
	:mod:`sysconfig` provides some functions to determine these paths.
	
	"""
	pass
	
def get_scheme_names():
	"""
	Return a tuple containing all schemes currently supported in
	:mod:`sysconfig`.
	
	
	"""
	pass
	
def get_path_names():
	"""
	Return a tuple containing all path names currently supported in
	:mod:`sysconfig`.
	
	
	"""
	pass
	
def get_path(name,scheme,vars,expand):
	"""
	Return an installation path corresponding to the path *name*, from the
	install scheme named *scheme*.
	
	*name* has to be a value from the list returned by :func:`get_path_names`.
	
	:mod:`sysconfig` stores installation paths corresponding to each path name,
	for each platform, with variables to be expanded.  For instance the *stdlib*
	path for the *nt* scheme is: ``{base}/Lib``.
	
	:func:`get_path` will use the variables returned by :func:`get_config_vars`
	to expand the path.  All variables have default values for each platform so
	one may call this function and get the default value.
	
	If *scheme* is provided, it must be a value from the list returned by
	:func:`get_path_names`.  Otherwise, the default scheme for the current
	platform is used.
	
	If *vars* is provided, it must be a dictionary of variables that will update
	the dictionary return by :func:`get_config_vars`.
	
	If *expand* is set to ``False``, the path will not be expanded using the
	variables.
	
	If *name* is not found, return ``None``.
	
	
	"""
	pass
	
def get_paths(scheme,vars,expand):
	"""
	Return a dictionary containing all installation paths corresponding to an
	installation scheme. See :func:`get_path` for more information.
	
	If *scheme* is not provided, will use the default scheme for the current
	platform.
	
	If *vars* is provided, it must be a dictionary of variables that will
	update the dictionary used to expand the paths.
	
	If *expand* is set to False, the paths will not be expanded.
	
	If *scheme* is not an existing scheme, :func:`get_paths` will raise a
	:exc:`KeyError`.
	
	
	Other functions
	---------------
	
	"""
	pass
	
def get_python_version():
	"""
	Return the ``MAJOR.MINOR`` Python version number as a string.  Similar to
	``sys.version[:3]``.
	
	
	"""
	pass
	
def get_platform():
	"""
	Return a string that identifies the current platform.
	
	This is used mainly to distinguish platform-specific build directories and
	platform-specific built distributions.  Typically includes the OS name and
	version and the architecture (as supplied by :func:`os.uname`), although the
	exact information included depends on the OS; e.g. for IRIX the architecture
	isn't particularly important (IRIX only runs on SGI hardware), but for Linux
	the kernel version isn't particularly important.
	
	Examples of returned values:
	
	- linux-i586
	- linux-alpha (?)
	- solaris-2.6-sun4u
	- irix-5.3
	- irix64-6.2
	
	Windows will return one of:
	
	- win-amd64 (64bit Windows on AMD64 (aka x86_64, Intel64, EM64T, etc)
	- win-ia64 (64bit Windows on Itanium)
	- win32 (all others - specifically, sys.platform is returned)
	
	Mac OS X can return:
	
	- macosx-10.6-ppc
	- macosx-10.4-ppc64
	- macosx-10.3-i386
	- macosx-10.4-fat
	
	For other non-POSIX platforms, currently just returns :data:`sys.platform`.
	
	
	"""
	pass
	
def is_python_build():
	"""
	Return ``True`` if the current Python installation was built from source.
	
	
	"""
	pass
	
def parse_config_h(fp,vars):
	"""
	Parse a :file:`config.h`\-style file.
	
	*fp* is a file-like object pointing to the :file:`config.h`\-like file.
	
	A dictionary containing name/value pairs is returned.  If an optional
	dictionary is passed in as the second argument, it is used instead of a new
	dictionary, and updated with the values read in the file.
	
	
	"""
	pass
	
