#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":platform: Unix
:synopsis: The group database (getgrnam() and friends).


This module provides access to the Unix group database. It is available on all
Unix versions.

Group database entries are reported as a tuple-like object, whose attributes
correspond to the members of the ``group`` structure (Attribute field below, see
``<pwd.h>``):

+-------+-----------+---------------------------------+
| Index | Attribute | Meaning                         |
+=======+===========+=================================+
| 0     | gr_name   | the name of the group           |
+-------+-----------+---------------------------------+
| 1     | gr_passwd | the (encrypted) group password; |
|       |           | often empty                     |
+-------+-----------+---------------------------------+
| 2     | gr_gid    | the numerical group ID          |
+-------+-----------+---------------------------------+
| 3     | gr_mem    | all the group member's  user    |
|       |           | names                           |
+-------+-----------+---------------------------------+

The gid is an integer, name and password are strings, and the member list is a
list of strings. (Note that most users are not explicitly listed as members of
the group they are in according to the password database.  Check both databases
to get complete membership information.  Also note that a ``gr_name`` that
starts with a ``+`` or ``-`` is likely to be a YP/NIS reference and may not be
accessible via :func:`getgrnam` or :func:`getgrgid`.)

It defines the following items:


"""
def getgrgid(gid):
	"""
	Return the group database entry for the given numeric group ID. :exc:`KeyError`
	is raised if the entry asked for cannot be found.
	
	
	"""
	pass
	
def getgrnam(name):
	"""
	Return the group database entry for the given group name. :exc:`KeyError` is
	raised if the entry asked for cannot be found.
	
	
	"""
	pass
	
def getgrall():
	"""
	Return a list of all available group entries, in arbitrary order.
	
	
	"""
	pass
	
