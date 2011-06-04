#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Support for asynchronous command/response protocols.
"""
class async_chat:


	"""
	This class is an abstract subclass of :class:`asyncore.dispatcher`. To make
	practical use of the code you must subclass :class:`async_chat`, providing
	meaningful :meth:`collect_incoming_data` and :meth:`found_terminator`
	methods.
	The :class:`asyncore.dispatcher` methods can be used, although not all make
	sense in a message/response context.
	
	Like :class:`asyncore.dispatcher`, :class:`async_chat` defines a set of
	events that are generated by an analysis of socket conditions after a
	:cfunc:`select` call. Once the polling loop has been started the
	:class:`async_chat` object's methods are called by the event-processing
	framework with no action on the part of the programmer.
	
	Two class attributes can be modified, to improve performance, or possibly
	even to conserve memory.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	"""
	The asynchronous input buffer size (default ``4096``).
	
	
	"""
	ac_in_buffer_size = None
	"""
	The asynchronous output buffer size (default ``4096``).
	
	Unlike :class:`asyncore.dispatcher`, :class:`async_chat` allows you to
	define a first-in-first-out queue (fifo) of *producers*. A producer need
	have only one method, :meth:`more`, which should return data to be
	transmitted on the channel.
	The producer indicates exhaustion (*i.e.* that it contains no more data) by
	having its :meth:`more` method return the empty string. At this point the
	:class:`async_chat` object removes the producer from the fifo and starts
	using the next producer, if any. When the producer fifo is empty the
	:meth:`handle_write` method does nothing. You use the channel object's
	:meth:`set_terminator` method to describe how to recognize the end of, or
	an important breakpoint in, an incoming transmission from the remote
	endpoint.
	
	To build a functioning :class:`async_chat` subclass your  input methods
	:meth:`collect_incoming_data` and :meth:`found_terminator` must handle the
	data that the channel receives asynchronously. The methods are described
	below.
	
	
	"""
	ac_out_buffer_size = None
	


class fifo:


	"""
	A :class:`fifo` holding data which has been pushed by the application but
	not yet popped for writing to the channel.  A :class:`fifo` is a list used
	to hold data and/or producers until they are required.  If the *list*
	argument is provided then it should contain producers or data items to be
	written to the channel.
	
	
	"""
	
	
	def __init__(self, list=None):
		pass
	
	


