#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":platform: Unix
:synopsis: GNU's reinterpretation of dbm.

"""
def open(filename,flag,mode):
	"""
	Open a ``gdbm`` database and return a ``gdbm`` object.  The *filename* argument
	is the name of the database file.
	
	The optional *flag* argument can be:
	
	+---------+-------------------------------------------+
	| Value   | Meaning                                   |
	+=========+===========================================+
	| ``'r'`` | Open existing database for reading only   |
	|         | (default)                                 |
	+---------+-------------------------------------------+
	| ``'w'`` | Open existing database for reading and    |
	|         | writing                                   |
	+---------+-------------------------------------------+
	| ``'c'`` | Open database for reading and writing,    |
	|         | creating it if it doesn't exist           |
	+---------+-------------------------------------------+
	| ``'n'`` | Always create a new, empty database, open |
	|         | for reading and writing                   |
	+---------+-------------------------------------------+
	
	The following additional characters may be appended to the flag to control
	how the database is opened:
	
	+---------+--------------------------------------------+
	| Value   | Meaning                                    |
	+=========+============================================+
	| ``'f'`` | Open the database in fast mode.  Writes    |
	|         | to the database will not be synchronized.  |
	+---------+--------------------------------------------+
	| ``'s'`` | Synchronized mode. This will cause changes |
	|         | to the database to be immediately written  |
	|         | to the file.                               |
	+---------+--------------------------------------------+
	| ``'u'`` | Do not lock database.                      |
	+---------+--------------------------------------------+
	
	Not all flags are valid for all versions of ``gdbm``.  The module constant
	:const:`open_flags` is a string of supported flag characters.  The exception
	:exc:`error` is raised if an invalid flag is specified.
	
	The optional *mode* argument is the Unix mode of the file, used only when the
	database has to be created.  It defaults to octal ``0666``.
	
	In addition to the dictionary-like methods, ``gdbm`` objects have the following
	methods:
	
	
	"""
	pass
	
def firstkey():
	"""
	It's possible to loop over every key in the database using this method  and the
	:meth:`nextkey` method.  The traversal is ordered by ``gdbm``'s internal hash
	values, and won't be sorted by the key values.  This method returns the starting
	key.
	
	
	"""
	pass
	
def nextkey(key):
	"""
	Returns the key that follows *key* in the traversal.  The following code prints
	every key in the database ``db``, without having to create a list in memory that
	contains them all::
	
	k = db.firstkey()
	while k != None:
	print k
	k = db.nextkey(k)
	
	
	"""
	pass
	
def reorganize():
	"""
	If you have carried out a lot of deletions and would like to shrink the space
	used by the ``gdbm`` file, this routine will reorganize the database.  ``gdbm``
	will not shorten the length of a database file except by using this
	reorganization; otherwise, deleted file space will be kept and reused as new
	(key, value) pairs are added.
	
	
	"""
	pass
	
def sync():
	"""
	When the database has been opened in fast mode, this method forces any
	unwritten data to be written to the disk.
	
	
	"""
	pass
	
