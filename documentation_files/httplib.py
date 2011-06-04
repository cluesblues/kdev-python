#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: HTTP and HTTPS protocol client (requires sockets).

"""
class HTTPConnection:


	"""
	An :class:`HTTPConnection` instance represents one transaction with an HTTP
	server.  It should be instantiated passing it a host and optional port
	number.  If no port number is passed, the port is extracted from the host
	string if it has the form ``host:port``, else the default HTTP port (80) is
	used.  When True, the optional parameter *strict* (which defaults to a false
	value) causes ``BadStatusLine`` to
	be raised if the status line can't be parsed as a valid HTTP/1.0 or 1.1
	status line.  If the optional *timeout* parameter is given, blocking
	operations (like connection attempts) will timeout after that many seconds
	(if it is not given, the global default timeout setting is used).
	The optional *source_address* parameter may be a tuple of a (host, port)
	to use as the source address the HTTP connection is made from.
	
	For example, the following calls all create instances that connect to the server
	at the same host and port::
	
	>>> h1 = httplib.HTTPConnection('www.cwi.nl')
	>>> h2 = httplib.HTTPConnection('www.cwi.nl:80')
	>>> h3 = httplib.HTTPConnection('www.cwi.nl', 80)
	>>> h3 = httplib.HTTPConnection('www.cwi.nl', 80, timeout=10)
	
	"""
	
	
	def __init__(self, host,port,strict,timeout,source_address):
		pass
	
	


class HTTPSConnection:


	"""
	A subclass of :class:`HTTPConnection` that uses SSL for communication with
	secure servers.  Default port is ``443``. *key_file* is the name of a PEM
	formatted file that contains your private key. *cert_file* is a PEM formatted
	certificate chain file.
	
	"""
	
	
	def __init__(self, host,port,key_file,cert_file,strict,timeout,source_address):
		pass
	
	


class HTTPResponse:


	"""
	Class whose instances are returned upon successful connection.  Not instantiated
	directly by user.
	
	"""
	
	
	def __init__(self, sock,debuglevel=0,strict=0):
		pass
	
	


class HTTPMessage:


	"""
	An :class:`HTTPMessage` instance is used to hold the headers from an HTTP
	response. It is implemented using the :class:`mimetools.Message` class and
	provides utility functions to deal with HTTP Headers. It is not directly
	instantiated by the users.
	
	
	The following exceptions are raised as appropriate:
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	"""
	The default port for the HTTP protocol (always ``80``).
	
	
	"""
	HTTP_PORT = None
	"""
	The default port for the HTTPS protocol (always ``443``).
	
	and also the following constants for integer status codes:
	
	+------------------------------------------+---------+-----------------------------------------------------------------------+
	| Constant                                 | Value   | Definition                                                            |
	+==========================================+=========+=======================================================================+
	| :const:`CONTINUE`                        | ``100`` | HTTP/1.1, `RFC 2616, Section                                          |
	|                                          |         | 10.1.1                                                                |
	|                                          |         | <http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.1.1>`_  |
	+------------------------------------------+---------+-----------------------------------------------------------------------+
	| :const:`SWITCHING_PROTOCOLS`             | ``101`` | HTTP/1.1, `RFC 2616, Section                                          |
	|                                          |         | 10.1.2                                                                |
	|                                          |         | <http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.1.2>`_  |
	+------------------------------------------+---------+-----------------------------------------------------------------------+
	| :const:`PROCESSING`                      | ``102`` | WEBDAV, `RFC 2518, Section 10.1                                       |
	|                                          |         | <http://www.webdav.org/specs/rfc2518.html#STATUS_102>`_               |
	+------------------------------------------+---------+-----------------------------------------------------------------------+
	| :const:`OK`                              | ``200`` | HTTP/1.1, `RFC 2616, Section                                          |
	|                                          |         | 10.2.1                                                                |
	|                                          |         | <http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1>`_  |
	+------------------------------------------+---------+-----------------------------------------------------------------------+
	| :const:`CREATED`                         | ``201`` | HTTP/1.1, `RFC 2616, Section                                          |
	|                                          |         | 10.2.2                                                                |
	|                                          |         | <http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2>`_  |
	+------------------------------------------+---------+-----------------------------------------------------------------------+
	| :const:`ACCEPTED`                        | ``202`` | HTTP/1.1, `RFC 2616, Section                                          |
	|                                          |         | 10.2.3                                                                |
	|                                          |         | <http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3>`_  |
	+------------------------------------------+---------+-----------------------------------------------------------------------+
	| :const:`NON_AUTHORITATIVE_INFORMATION`   | ``203`` | HTTP/1.1, `RFC 2616, Section                                          |
	|                                          |         | 10.2.4                                                                |
	|                                          |         | <http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.4>`_  |
	+------------------------------------------+---------+-----------------------------------------------------------------------+
	| :const:`NO_CONTENT`                      | ``204`` | HTTP/1.1, `RFC 2616, Section                                          |
	|                                          |         | 10.2.5                                                                |
	|                                          |         | <http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.5>`_  |
	+------------------------------------------+---------+-----------------------------------------------------------------------+
	| :const:`RESET_CONTENT`                   | ``205`` | HTTP/1.1, `RFC 2616, Section                                          |
	|                                          |         | 10.2.6                                                                |
	|                                          |         | <http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.6>`_  |
	+------------------------------------------+---------+-----------------------------------------------------------------------+
	| :const:`PARTIAL_CONTENT`                 | ``206`` | HTTP/1.1, `RFC 2616, Section                                          |
	|                                          |         | 10.2.7                                                                |
	|                                          |         | <http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.7>`_  |
	+------------------------------------------+---------+-----------------------------------------------------------------------+
	| :const:`MULTI_STATUS`                    | ``207`` | WEBDAV `RFC 2518, Section 10.2                                        |
	|                                          |         | <http://www.webdav.org/specs/rfc2518.html#STATUS_207>`_               |
	+------------------------------------------+---------+-----------------------------------------------------------------------+
	| :const:`IM_USED`                         | ``226`` | Delta encoding in HTTP,                                               |
	|                                          |         | :rfc:`3229`, Section 10.4.1                                           |
	+------------------------------------------+---------+-----------------------------------------------------------------------+
	| :const:`MULTIPLE_CHOICES`                | ``300`` | HTTP/1.1, `RFC 2616, Section                                          |
	|                                          |         | 10.3.1                                                                |
	|                                          |         | <http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.3.1>`_  |
	+------------------------------------------+---------+-----------------------------------------------------------------------+
	| :const:`MOVED_PERMANENTLY`               | ``301`` | HTTP/1.1, `RFC 2616, Section                                          |
	|                                          |         | 10.3.2                                                                |
	|                                          |         | <http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.3.2>`_  |
	+------------------------------------------+---------+-----------------------------------------------------------------------+
	| :const:`FOUND`                           | ``302`` | HTTP/1.1, `RFC 2616, Section                                          |
	|                                          |         | 10.3.3                                                                |
	|                                          |         | <http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.3.3>`_  |
	+------------------------------------------+---------+-----------------------------------------------------------------------+
	| :const:`SEE_OTHER`                       | ``303`` | HTTP/1.1, `RFC 2616, Section                                          |
	|                                          |         | 10.3.4                                                                |
	|                                          |         | <http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.3.4>`_  |
	+------------------------------------------+---------+-----------------------------------------------------------------------+
	| :const:`NOT_MODIFIED`                    | ``304`` | HTTP/1.1, `RFC 2616, Section                                          |
	|                                          |         | 10.3.5                                                                |
	|                                          |         | <http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.3.5>`_  |
	+------------------------------------------+---------+-----------------------------------------------------------------------+
	| :const:`USE_PROXY`                       | ``305`` | HTTP/1.1, `RFC 2616, Section                                          |
	|                                          |         | 10.3.6                                                                |
	|                                          |         | <http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.3.6>`_  |
	+------------------------------------------+---------+-----------------------------------------------------------------------+
	| :const:`TEMPORARY_REDIRECT`              | ``307`` | HTTP/1.1, `RFC 2616, Section                                          |
	|                                          |         | 10.3.8                                                                |
	|                                          |         | <http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.3.8>`_  |
	+------------------------------------------+---------+-----------------------------------------------------------------------+
	| :const:`BAD_REQUEST`                     | ``400`` | HTTP/1.1, `RFC 2616, Section                                          |
	|                                          |         | 10.4.1                                                                |
	|                                          |         | <http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1>`_  |
	+------------------------------------------+---------+-----------------------------------------------------------------------+
	| :const:`UNAUTHORIZED`                    | ``401`` | HTTP/1.1, `RFC 2616, Section                                          |
	|                                          |         | 10.4.2                                                                |
	|                                          |         | <http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2>`_  |
	+------------------------------------------+---------+-----------------------------------------------------------------------+
	| :const:`PAYMENT_REQUIRED`                | ``402`` | HTTP/1.1, `RFC 2616, Section                                          |
	|                                          |         | 10.4.3                                                                |
	|                                          |         | <http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.3>`_  |
	+------------------------------------------+---------+-----------------------------------------------------------------------+
	| :const:`FORBIDDEN`                       | ``403`` | HTTP/1.1, `RFC 2616, Section                                          |
	|                                          |         | 10.4.4                                                                |
	|                                          |         | <http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4>`_  |
	+------------------------------------------+---------+-----------------------------------------------------------------------+
	| :const:`NOT_FOUND`                       | ``404`` | HTTP/1.1, `RFC 2616, Section                                          |
	|                                          |         | 10.4.5                                                                |
	|                                          |         | <http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.5>`_  |
	+------------------------------------------+---------+-----------------------------------------------------------------------+
	| :const:`METHOD_NOT_ALLOWED`              | ``405`` | HTTP/1.1, `RFC 2616, Section                                          |
	|                                          |         | 10.4.6                                                                |
	|                                          |         | <http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.6>`_  |
	+------------------------------------------+---------+-----------------------------------------------------------------------+
	| :const:`NOT_ACCEPTABLE`                  | ``406`` | HTTP/1.1, `RFC 2616, Section                                          |
	|                                          |         | 10.4.7                                                                |
	|                                          |         | <http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.7>`_  |
	+------------------------------------------+---------+-----------------------------------------------------------------------+
	| :const:`PROXY_AUTHENTICATION_REQUIRED`   | ``407`` | HTTP/1.1, `RFC 2616, Section                                          |
	|                                          |         | 10.4.8                                                                |
	|                                          |         | <http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.8>`_  |
	+------------------------------------------+---------+-----------------------------------------------------------------------+
	| :const:`REQUEST_TIMEOUT`                 | ``408`` | HTTP/1.1, `RFC 2616, Section                                          |
	|                                          |         | 10.4.9                                                                |
	|                                          |         | <http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.9>`_  |
	+------------------------------------------+---------+-----------------------------------------------------------------------+
	| :const:`CONFLICT`                        | ``409`` | HTTP/1.1, `RFC 2616, Section                                          |
	|                                          |         | 10.4.10                                                               |
	|                                          |         | <http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.10>`_ |
	+------------------------------------------+---------+-----------------------------------------------------------------------+
	| :const:`GONE`                            | ``410`` | HTTP/1.1, `RFC 2616, Section                                          |
	|                                          |         | 10.4.11                                                               |
	|                                          |         | <http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.11>`_ |
	+------------------------------------------+---------+-----------------------------------------------------------------------+
	| :const:`LENGTH_REQUIRED`                 | ``411`` | HTTP/1.1, `RFC 2616, Section                                          |
	|                                          |         | 10.4.12                                                               |
	|                                          |         | <http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.12>`_ |
	+------------------------------------------+---------+-----------------------------------------------------------------------+
	| :const:`PRECONDITION_FAILED`             | ``412`` | HTTP/1.1, `RFC 2616, Section                                          |
	|                                          |         | 10.4.13                                                               |
	|                                          |         | <http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.13>`_ |
	+------------------------------------------+---------+-----------------------------------------------------------------------+
	| :const:`REQUEST_ENTITY_TOO_LARGE`        | ``413`` | HTTP/1.1, `RFC 2616, Section                                          |
	|                                          |         | 10.4.14                                                               |
	|                                          |         | <http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.14>`_ |
	+------------------------------------------+---------+-----------------------------------------------------------------------+
	| :const:`REQUEST_URI_TOO_LONG`            | ``414`` | HTTP/1.1, `RFC 2616, Section                                          |
	|                                          |         | 10.4.15                                                               |
	|                                          |         | <http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.15>`_ |
	+------------------------------------------+---------+-----------------------------------------------------------------------+
	| :const:`UNSUPPORTED_MEDIA_TYPE`          | ``415`` | HTTP/1.1, `RFC 2616, Section                                          |
	|                                          |         | 10.4.16                                                               |
	|                                          |         | <http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.16>`_ |
	+------------------------------------------+---------+-----------------------------------------------------------------------+
	| :const:`REQUESTED_RANGE_NOT_SATISFIABLE` | ``416`` | HTTP/1.1, `RFC 2616, Section                                          |
	|                                          |         | 10.4.17                                                               |
	|                                          |         | <http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.17>`_ |
	+------------------------------------------+---------+-----------------------------------------------------------------------+
	| :const:`EXPECTATION_FAILED`              | ``417`` | HTTP/1.1, `RFC 2616, Section                                          |
	|                                          |         | 10.4.18                                                               |
	|                                          |         | <http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.18>`_ |
	+------------------------------------------+---------+-----------------------------------------------------------------------+
	| :const:`UNPROCESSABLE_ENTITY`            | ``422`` | WEBDAV, `RFC 2518, Section 10.3                                       |
	|                                          |         | <http://www.webdav.org/specs/rfc2518.html#STATUS_422>`_               |
	+------------------------------------------+---------+-----------------------------------------------------------------------+
	| :const:`LOCKED`                          | ``423`` | WEBDAV `RFC 2518, Section 10.4                                        |
	|                                          |         | <http://www.webdav.org/specs/rfc2518.html#STATUS_423>`_               |
	+------------------------------------------+---------+-----------------------------------------------------------------------+
	| :const:`FAILED_DEPENDENCY`               | ``424`` | WEBDAV, `RFC 2518, Section 10.5                                       |
	|                                          |         | <http://www.webdav.org/specs/rfc2518.html#STATUS_424>`_               |
	+------------------------------------------+---------+-----------------------------------------------------------------------+
	| :const:`UPGRADE_REQUIRED`                | ``426`` | HTTP Upgrade to TLS,                                                  |
	|                                          |         | :rfc:`2817`, Section 6                                                |
	+------------------------------------------+---------+-----------------------------------------------------------------------+
	| :const:`INTERNAL_SERVER_ERROR`           | ``500`` | HTTP/1.1, `RFC 2616, Section                                          |
	|                                          |         | 10.5.1                                                                |
	|                                          |         | <http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1>`_  |
	+------------------------------------------+---------+-----------------------------------------------------------------------+
	| :const:`NOT_IMPLEMENTED`                 | ``501`` | HTTP/1.1, `RFC 2616, Section                                          |
	|                                          |         | 10.5.2                                                                |
	|                                          |         | <http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.2>`_  |
	+------------------------------------------+---------+-----------------------------------------------------------------------+
	| :const:`BAD_GATEWAY`                     | ``502`` | HTTP/1.1 `RFC 2616, Section                                           |
	|                                          |         | 10.5.3                                                                |
	|                                          |         | <http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.3>`_  |
	+------------------------------------------+---------+-----------------------------------------------------------------------+
	| :const:`SERVICE_UNAVAILABLE`             | ``503`` | HTTP/1.1, `RFC 2616, Section                                          |
	|                                          |         | 10.5.4                                                                |
	|                                          |         | <http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.4>`_  |
	+------------------------------------------+---------+-----------------------------------------------------------------------+
	| :const:`GATEWAY_TIMEOUT`                 | ``504`` | HTTP/1.1 `RFC 2616, Section                                           |
	|                                          |         | 10.5.5                                                                |
	|                                          |         | <http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.5>`_  |
	+------------------------------------------+---------+-----------------------------------------------------------------------+
	| :const:`HTTP_VERSION_NOT_SUPPORTED`      | ``505`` | HTTP/1.1, `RFC 2616, Section                                          |
	|                                          |         | 10.5.6                                                                |
	|                                          |         | <http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.6>`_  |
	+------------------------------------------+---------+-----------------------------------------------------------------------+
	| :const:`INSUFFICIENT_STORAGE`            | ``507`` | WEBDAV, `RFC 2518, Section 10.6                                       |
	|                                          |         | <http://www.webdav.org/specs/rfc2518.html#STATUS_507>`_               |
	+------------------------------------------+---------+-----------------------------------------------------------------------+
	| :const:`NOT_EXTENDED`                    | ``510`` | An HTTP Extension Framework,                                          |
	|                                          |         | :rfc:`2774`, Section 7                                                |
	+------------------------------------------+---------+-----------------------------------------------------------------------+
	
	
	"""
	HTTPS_PORT = None
	"""
	This dictionary maps the HTTP 1.1 status codes to the W3C names.
	
	Example: ``httplib.responses[httplib.NOT_FOUND]`` is ``'Not Found'``.
	
	"""
	responses = None
	


