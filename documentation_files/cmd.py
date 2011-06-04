#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Build line-oriented command interpreters.
"""
class Cmd:


	"""
	A :class:`Cmd` instance or subclass instance is a line-oriented interpreter
	framework.  There is no good reason to instantiate :class:`Cmd` itself; rather,
	it's useful as a superclass of an interpreter class you define yourself in order
	to inherit :class:`Cmd`'s methods and encapsulate action methods.
	
	The optional argument *completekey* is the :mod:`readline` name of a completion
	key; it defaults to :kbd:`Tab`. If *completekey* is not :const:`None` and
	:mod:`readline` is available, command completion is done automatically.
	
	The optional arguments *stdin* and *stdout* specify the  input and output file
	objects that the Cmd instance or subclass  instance will use for input and
	output. If not specified, they will default to :data:`sys.stdin` and
	:data:`sys.stdout`.
	
	If you want a given *stdin* to be used, make sure to set the instance's
	:attr:`use_rawinput` attribute to ``False``, otherwise *stdin* will be
	ignored.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def cmdloop(self, intro):
		"""
		Repeatedly issue a prompt, accept input, parse an initial prefix off the
		received input, and dispatch to action methods, passing them the remainder of
		the line as argument.
		
		The optional argument is a banner or intro string to be issued before the first
		prompt (this overrides the :attr:`intro` class member).
		
		If the :mod:`readline` module is loaded, input will automatically inherit
		:program:`bash`\ -like history-list editing (e.g. :kbd:`Control-P` scrolls back
		to the last command, :kbd:`Control-N` forward to the next one, :kbd:`Control-F`
		moves the cursor to the right non-destructively, :kbd:`Control-B` moves the
		cursor to the left non-destructively, etc.).
		
		An end-of-file on input is passed back as the string ``'EOF'``.
		
		An interpreter instance will recognize a command name ``foo`` if and only if it
		has a method :meth:`do_foo`.  As a special case, a line beginning with the
		character ``'?'`` is dispatched to the method :meth:`do_help`.  As another
		special case, a line beginning with the character ``'!'`` is dispatched to the
		method :meth:`do_shell` (if such a method is defined).
		
		This method will return when the :meth:`postcmd` method returns a true value.
		The *stop* argument to :meth:`postcmd` is the return value from the command's
		corresponding :meth:`do_\*` method.
		
		If completion is enabled, completing commands will be done automatically, and
		completing of commands args is done by calling :meth:`complete_foo` with
		arguments *text*, *line*, *begidx*, and *endidx*.  *text* is the string prefix
		we are attempting to match: all returned matches must begin with it. *line* is
		the current input line with leading whitespace removed, *begidx* and *endidx*
		are the beginning and ending indexes of the prefix text, which could be used to
		provide different completion depending upon which position the argument is in.
		
		All subclasses of :class:`Cmd` inherit a predefined :meth:`do_help`.  This
		method, called with an argument ``'bar'``, invokes the corresponding method
		:meth:`help_bar`, and if that is not present, prints the docstring of
		:meth:`do_bar`, if available.  With no argument, :meth:`do_help` lists all
		available help topics (that is, all commands with corresponding
		:meth:`help_\*` methods or commands that have docstrings), and also lists any
		undocumented commands.
		
		
		"""
		pass
		
	def onecmd(self, str):
		"""
		Interpret the argument as though it had been typed in response to the prompt.
		This may be overridden, but should not normally need to be; see the
		:meth:`precmd` and :meth:`postcmd` methods for useful execution hooks.  The
		return value is a flag indicating whether interpretation of commands by the
		interpreter should stop.  If there is a :meth:`do_\*` method for the command
		*str*, the return value of that method is returned, otherwise the return value
		from the :meth:`default` method is returned.
		
		
		"""
		pass
		
	def emptyline(self, ):
		"""
		Method called when an empty line is entered in response to the prompt. If this
		method is not overridden, it repeats the last nonempty command entered.
		
		
		"""
		pass
		
	def default(self, line):
		"""
		Method called on an input line when the command prefix is not recognized. If
		this method is not overridden, it prints an error message and returns.
		
		
		"""
		pass
		
	def completedefault(self, text,line,begidx,endidx):
		"""
		Method called to complete an input line when no command-specific
		:meth:`complete_\*` method is available.  By default, it returns an empty list.
		
		
		"""
		pass
		
	def precmd(self, line):
		"""
		Hook method executed just before the command line *line* is interpreted, but
		after the input prompt is generated and issued.  This method is a stub in
		:class:`Cmd`; it exists to be overridden by subclasses.  The return value is
		used as the command which will be executed by the :meth:`onecmd` method; the
		:meth:`precmd` implementation may re-write the command or simply return *line*
		unchanged.
		
		
		"""
		pass
		
	def postcmd(self, stop,line):
		"""
		Hook method executed just after a command dispatch is finished.  This method is
		a stub in :class:`Cmd`; it exists to be overridden by subclasses.  *line* is the
		command line which was executed, and *stop* is a flag which indicates whether
		execution will be terminated after the call to :meth:`postcmd`; this will be the
		return value of the :meth:`onecmd` method.  The return value of this method will
		be used as the new value for the internal flag which corresponds to *stop*;
		returning false will cause interpretation to continue.
		
		
		"""
		pass
		
	def preloop(self, ):
		"""
		Hook method executed once when :meth:`cmdloop` is called.  This method is a stub
		in :class:`Cmd`; it exists to be overridden by subclasses.
		
		
		"""
		pass
		
	def postloop(self, ):
		"""
		Hook method executed once when :meth:`cmdloop` is about to return. This method
		is a stub in :class:`Cmd`; it exists to be overridden by subclasses.
		
		Instances of :class:`Cmd` subclasses have some public instance variables:
		
		
		"""
		pass
		
	


