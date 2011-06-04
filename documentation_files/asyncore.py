#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: A base class for developing asynchronous socket handling
services.
"""
def loop(timeout,use_poll,map,count):
	"""
	Enter a polling loop that terminates after count passes or all open
	channels have been closed.  All arguments are optional.  The *count*
	parameter defaults to None, resulting in the loop terminating only when all
	channels have been closed.  The *timeout* argument sets the timeout
	parameter for the appropriate :func:`select` or :func:`poll` call, measured
	in seconds; the default is 30 seconds.  The *use_poll* parameter, if true,
	indicates that :func:`poll` should be used in preference to :func:`select`
	(the default is ``False``).
	
	The *map* parameter is a dictionary whose items are the channels to watch.
	As channels are closed they are deleted from their map.  If *map* is
	omitted, a global map is used. Channels (instances of
	:class:`asyncore.dispatcher`, :class:`asynchat.async_chat` and subclasses
	thereof) can freely be mixed in the map.
	
	
	"""
	pass
	
class dispatcher:


	"""
	The :class:`dispatcher` class is a thin wrapper around a low-level socket
	object. To make it more useful, it has a few methods for event-handling
	which are called from the asynchronous loop.   Otherwise, it can be treated
	as a normal non-blocking socket object.
	
	The firing of low-level events at certain times or in certain connection
	states tells the asynchronous loop that certain higher-level events have
	taken place.  For example, if we have asked for a socket to connect to
	another host, we know that the connection has been made when the socket
	becomes writable for the first time (at this point you know that you may
	write to it with the expectation of success).  The implied higher-level
	events are:
	
	+----------------------+----------------------------------------+
	| Event                | Description                            |
	+======================+========================================+
	| ``handle_connect()`` | Implied by the first read or write     |
	|                      | event                                  |
	+----------------------+----------------------------------------+
	| ``handle_close()``   | Implied by a read event with no data   |
	|                      | available                              |
	+----------------------+----------------------------------------+
	| ``handle_accept()``  | Implied by a read event on a listening |
	|                      | socket                                 |
	+----------------------+----------------------------------------+
	
	During asynchronous processing, each mapped channel's :meth:`readable` and
	:meth:`writable` methods are used to determine whether the channel's socket
	should be added to the list of channels :cfunc:`select`\ ed or
	:cfunc:`poll`\ ed for read and write events.
	
	Thus, the set of channel events is larger than the basic socket events.  The
	full set of methods that can be overridden in your subclass follows:
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def handle_read(self, ):
		"""
		Called when the asynchronous loop detects that a :meth:`read` call on the
		channel's socket will succeed.
		
		
		"""
		pass
		
	def handle_write(self, ):
		"""
		Called when the asynchronous loop detects that a writable socket can be
		written.  Often this method will implement the necessary buffering for
		performance.  For example::
		
		def handle_write(self):
		sent = self.send(self.buffer)
		self.buffer = self.buffer[sent:]
		
		
		"""
		pass
		
	def handle_expt(self, ):
		"""
		Called when there is out of band (OOB) data for a socket connection.  This
		will almost never happen, as OOB is tenuously supported and rarely used.
		
		
		"""
		pass
		
	def handle_connect(self, ):
		"""
		Called when the active opener's socket actually makes a connection.  Might
		send a "welcome" banner, or initiate a protocol negotiation with the
		remote endpoint, for example.
		
		
		"""
		pass
		
	def handle_close(self, ):
		"""
		Called when the socket is closed.
		
		
		"""
		pass
		
	def handle_error(self, ):
		"""
		Called when an exception is raised and not otherwise handled.  The default
		version prints a condensed traceback.
		
		
		"""
		pass
		
	def handle_accept(self, ):
		"""
		Called on listening channels (passive openers) when a connection can be
		established with a new remote endpoint that has issued a :meth:`connect`
		call for the local endpoint.
		
		
		"""
		pass
		
	def readable(self, ):
		"""
		Called each time around the asynchronous loop to determine whether a
		channel's socket should be added to the list on which read events can
		occur.  The default method simply returns ``True``, indicating that by
		default, all channels will be interested in read events.
		
		
		"""
		pass
		
	def writable(self, ):
		"""
		Called each time around the asynchronous loop to determine whether a
		channel's socket should be added to the list on which write events can
		occur.  The default method simply returns ``True``, indicating that by
		default, all channels will be interested in write events.
		
		
		In addition, each channel delegates or extends many of the socket methods.
		Most of these are nearly identical to their socket partners.
		
		
		"""
		pass
		
	def create_socket(self, family,type):
		"""
		This is identical to the creation of a normal socket, and will use the
		same options for creation.  Refer to the :mod:`socket` documentation for
		information on creating sockets.
		
		
		"""
		pass
		
	def connect(self, address):
		"""
		As with the normal socket object, *address* is a tuple with the first
		element the host to connect to, and the second the port number.
		
		
		"""
		pass
		
	def send(self, data):
		"""
		Send *data* to the remote end-point of the socket.
		
		
		"""
		pass
		
	def recv(self, buffer_size):
		"""
		Read at most *buffer_size* bytes from the socket's remote end-point.  An
		empty string implies that the channel has been closed from the other end.
		
		
		"""
		pass
		
	def listen(self, backlog):
		"""
		Listen for connections made to the socket.  The *backlog* argument
		specifies the maximum number of queued connections and should be at least
		1; the maximum value is system-dependent (usually 5).
		
		
		"""
		pass
		
	def bind(self, address):
		"""
		Bind the socket to *address*.  The socket must not already be bound.  (The
		format of *address* depends on the address family --- refer to the
		:mod:`socket` documentation for more information.)  To mark
		the socket as re-usable (setting the :const:`SO_REUSEADDR` option), call
		the :class:`dispatcher` object's :meth:`set_reuse_addr` method.
		
		
		"""
		pass
		
	def accept(self, ):
		"""
		Accept a connection.  The socket must be bound to an address and listening
		for connections.  The return value can be either ``None`` or a pair
		``(conn, address)`` where *conn* is a *new* socket object usable to send
		and receive data on the connection, and *address* is the address bound to
		the socket on the other end of the connection.
		When ``None`` is returned it means the connection didn't take place, in
		which case the server should just ignore this event and keep listening
		for further incoming connections.
		
		
		"""
		pass
		
	def close(self, ):
		"""
		Close the socket.  All future operations on the socket object will fail.
		The remote end-point will receive no more data (after queued data is
		flushed).  Sockets are automatically closed when they are
		garbage-collected.
		
		"""
		pass
		
	


class dispatcher_with_send:


	"""
	A :class:`dispatcher` subclass which adds simple buffered output capability,
	useful for simple clients. For more sophisticated usage use
	:class:`asynchat.async_chat`.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class file_dispatcher:


	"""
	A file_dispatcher takes a file descriptor or file object along with an
	optional map argument and wraps it for use with the :cfunc:`poll` or
	:cfunc:`loop` functions.  If provided a file object or anything with a
	:cfunc:`fileno` method, that method will be called and passed to the
	:class:`file_wrapper` constructor.  Availability: UNIX.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


