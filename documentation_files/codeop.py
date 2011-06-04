#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Compile (possibly incomplete) Python code.
"""
def compile_command(source,filename,symbol):
	"""
	Tries to compile *source*, which should be a string of Python code and return a
	code object if *source* is valid Python code. In that case, the filename
	attribute of the code object will be *filename*, which defaults to
	``'<input>'``. Returns ``None`` if *source* is *not* valid Python code, but is a
	prefix of valid Python code.
	
	If there is a problem with *source*, an exception will be raised.
	:exc:`SyntaxError` is raised if there is invalid Python syntax, and
	:exc:`OverflowError` or :exc:`ValueError` if there is an invalid literal.
	
	The *symbol* argument determines whether *source* is compiled as a statement
	(``'single'``, the default) or as an :term:`expression` (``'eval'``).  Any
	other value will cause :exc:`ValueError` to  be raised.
	
	"""
	pass
	
class Compile:


	"""
	Instances of this class have :meth:`__call__` methods identical in signature to
	the built-in function :func:`compile`, but with the difference that if the
	instance compiles program text containing a :mod:`__future__` statement, the
	instance 'remembers' and compiles all subsequent program texts with the
	statement in force.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


