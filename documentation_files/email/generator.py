#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Generate flat text email messages from a message structure.


One of the most common tasks is to generate the flat text of the email message
represented by a message object structure.  You will need to do this if you want
to send your message via the :mod:`smtplib` module or the :mod:`nntplib` module,
or print the message on the console.  Taking a message object structure and
producing a flat text document is the job of the :class:`Generator` class.

Again, as with the :mod:`email.parser` module, you aren't limited to the
functionality of the bundled generator; you could write one from scratch
yourself.  However the bundled generator knows how to generate most email in a
standards-compliant way, should handle MIME and non-MIME email messages just
fine, and is designed so that the transformation from flat text, to a message
structure via the :class:`~email.parser.Parser` class, and back to flat text,
is idempotent (the input is identical to the output).  On the other hand, using
the Generator on a :class:`~email.message.Message` constructed by program may
result in changes to the :class:`~email.message.Message` object as defaults are
filled in.

Here are the public methods of the :class:`Generator` class, imported from the
:mod:`email.generator` module:


"""
class Generator:


	"""
	The constructor for the :class:`Generator` class takes a file-like object called
	*outfp* for an argument.  *outfp* must support the :meth:`write` method and be
	usable as the output file in a Python extended print statement.
	
	Optional *mangle_from_* is a flag that, when ``True``, puts a ``>`` character in
	front of any line in the body that starts exactly as ``From``, i.e. ``From``
	followed by a space at the beginning of the line.  This is the only guaranteed
	portable way to avoid having such lines be mistaken for a Unix mailbox format
	envelope header separator (see `WHY THE CONTENT-LENGTH FORMAT IS BAD
	<http://www.jwz.org/doc/content-length.html>`_ for details).  *mangle_from_*
	defaults to ``True``, but you might want to set this to ``False`` if you are not
	writing Unix mailbox format files.
	
	Optional *maxheaderlen* specifies the longest length for a non-continued header.
	When a header line is longer than *maxheaderlen* (in characters, with tabs
	expanded to 8 spaces), the header will be split as defined in the
	:class:`~email.header.Header` class.  Set to zero to disable header wrapping.
	The default is 78, as recommended (but not required) by :rfc:`2822`.
	
	The other public :class:`Generator` methods are:
	
	
	"""
	
	
	def __init__(self, outfp,mangle__from_,maxheaderlen):
		pass
	
	


class DecodedGenerator:


	"""
	This class, derived from :class:`Generator` walks through all the subparts of a
	message.  If the subpart is of main type :mimetype:`text`, then it prints the
	decoded payload of the subpart. Optional *_mangle_from_* and *maxheaderlen* are
	as with the :class:`Generator` base class.
	
	If the subpart is not of main type :mimetype:`text`, optional *fmt* is a format
	string that is used instead of the message payload. *fmt* is expanded with the
	following keywords, ``%(keyword)s`` format:
	
	* ``type`` -- Full MIME type of the non-\ :mimetype:`text` part
	
	* ``maintype`` -- Main MIME type of the non-\ :mimetype:`text` part
	
	* ``subtype`` -- Sub-MIME type of the non-\ :mimetype:`text` part
	
	* ``filename`` -- Filename of the non-\ :mimetype:`text` part
	
	* ``description`` -- Description associated with the non-\ :mimetype:`text` part
	
	* ``encoding`` -- Content transfer encoding of the non-\ :mimetype:`text` part
	
	The default value for *fmt* is ``None``, meaning ::
	
	[Non-text (%(type)s) part of message omitted, filename %(filename)s]
	
	"""
	
	
	def __init__(self, outfp,mangle__from_,maxheaderlen,fmt):
		pass
	
	


