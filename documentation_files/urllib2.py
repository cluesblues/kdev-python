#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Next generation URL opening library.
"""
def urlopen(url,data,timeout):
	"""
	Open the URL *url*, which can be either a string or a :class:`Request` object.
	
	"""
	pass
	
def install_opener(opener):
	"""
	Install an :class:`OpenerDirector` instance as the default global opener.
	Installing an opener is only necessary if you want urlopen to use that opener;
	otherwise, simply call :meth:`OpenerDirector.open` instead of :func:`urlopen`.
	The code does not check for a real :class:`OpenerDirector`, and any class with
	the appropriate interface will work.
	
	
	"""
	pass
	
def build_opener(handler,more):
	"""
	Return an :class:`OpenerDirector` instance, which chains the handlers in the
	order given. *handler*\s can be either instances of :class:`BaseHandler`, or
	subclasses of :class:`BaseHandler` (in which case it must be possible to call
	the constructor without any parameters).  Instances of the following classes
	will be in front of the *handler*\s, unless the *handler*\s contain them,
	instances of them or subclasses of them: :class:`ProxyHandler`,
	:class:`UnknownHandler`, :class:`HTTPHandler`, :class:`HTTPDefaultErrorHandler`,
	:class:`HTTPRedirectHandler`, :class:`FTPHandler`, :class:`FileHandler`,
	:class:`HTTPErrorProcessor`.
	
	If the Python installation has SSL support (i.e., if the :mod:`ssl` module can be imported),
	:class:`HTTPSHandler` will also be added.
	
	Beginning in Python 2.3, a :class:`BaseHandler` subclass may also change its
	:attr:`handler_order` member variable to modify its position in the handlers
	list.
	
	The following exceptions are raised as appropriate:
	
	
	"""
	pass
	
class Request:


	"""
	This class is an abstraction of a URL request.
	
	*url* should be a string containing a valid URL.
	
	*data* may be a string specifying additional data to send to the server, or
	``None`` if no such data is needed.  Currently HTTP requests are the only ones
	that use *data*; the HTTP request will be a POST instead of a GET when the
	*data* parameter is provided.  *data* should be a buffer in the standard
	:mimetype:`application/x-www-form-urlencoded` format.  The
	:func:`urllib.urlencode` function takes a mapping or sequence of 2-tuples and
	returns a string in this format.
	
	*headers* should be a dictionary, and will be treated as if :meth:`add_header`
	was called with each key and value as arguments.  This is often used to "spoof"
	the ``User-Agent`` header, which is used by a browser to identify itself --
	some HTTP servers only allow requests coming from common browsers as opposed
	to scripts.  For example, Mozilla Firefox may identify itself as ``"Mozilla/5.0
	(X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"``, while :mod:`urllib2`'s
	default user agent string is ``"Python-urllib/2.6"`` (on Python 2.6).
	
	The final two arguments are only of interest for correct handling of third-party
	HTTP cookies:
	
	*origin_req_host* should be the request-host of the origin transaction, as
	defined by :rfc:`2965`.  It defaults to ``cookielib.request_host(self)``.  This
	is the host name or IP address of the original request that was initiated by the
	user.  For example, if the request is for an image in an HTML document, this
	should be the request-host of the request for the page containing the image.
	
	*unverifiable* should indicate whether the request is unverifiable, as defined
	by RFC 2965.  It defaults to False.  An unverifiable request is one whose URL
	the user did not have the option to approve.  For example, if the request is for
	an image in an HTML document, and the user had no option to approve the
	automatic fetching of the image, this should be true.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def add_data(self, data):
		"""
		Set the :class:`Request` data to *data*.  This is ignored by all handlers except
		HTTP handlers --- and there it should be a byte string, and will change the
		request to be ``POST`` rather than ``GET``.
		
		
		"""
		pass
		
	def get_method(self, ):
		"""
		Return a string indicating the HTTP request method.  This is only meaningful for
		HTTP requests, and currently always returns ``'GET'`` or ``'POST'``.
		
		
		"""
		pass
		
	def has_data(self, ):
		"""
		Return whether the instance has a non-\ ``None`` data.
		
		
		"""
		pass
		
	def get_data(self, ):
		"""
		Return the instance's data.
		
		
		"""
		pass
		
	def add_header(self, key,val):
		"""
		Add another header to the request.  Headers are currently ignored by all
		handlers except HTTP handlers, where they are added to the list of headers sent
		to the server.  Note that there cannot be more than one header with the same
		name, and later calls will overwrite previous calls in case the *key* collides.
		Currently, this is no loss of HTTP functionality, since all headers which have
		meaning when used more than once have a (header-specific) way of gaining the
		same functionality using only one header.
		
		
		"""
		pass
		
	def add_unredirected_header(self, key,header):
		"""
		Add a header that will not be added to a redirected request.
		
		"""
		pass
		
	def has_header(self, header):
		"""
		Return whether the instance has the named header (checks both regular and
		unredirected).
		
		"""
		pass
		
	def get_full_url(self, ):
		"""
		Return the URL given in the constructor.
		
		
		"""
		pass
		
	def get_type(self, ):
		"""
		Return the type of the URL --- also known as the scheme.
		
		
		"""
		pass
		
	def get_host(self, ):
		"""
		Return the host to which a connection will be made.
		
		
		"""
		pass
		
	def get_selector(self, ):
		"""
		Return the selector --- the part of the URL that is sent to the server.
		
		
		"""
		pass
		
	def set_proxy(self, host,type):
		"""
		Prepare the request by connecting to a proxy server. The *host* and *type* will
		replace those of the instance, and the instance's selector will be the original
		URL given in the constructor.
		
		
		"""
		pass
		
	def get_origin_req_host(self, ):
		"""
		Return the request-host of the origin transaction, as defined by :rfc:`2965`.
		See the documentation for the :class:`Request` constructor.
		
		
		"""
		pass
		
	def is_unverifiable(self, ):
		"""
		Return whether the request is unverifiable, as defined by RFC 2965. See the
		documentation for the :class:`Request` constructor.
		
		
		.. penerDirector Objects
		----------------------
		
		:class:`OpenerDirector` instances have the following methods:
		
		
		"""
		pass
		
	


class OpenerDirector:


	"""
	The :class:`OpenerDirector` class opens URLs via :class:`BaseHandler`\ s chained
	together. It manages the chaining of handlers, and recovery from errors.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def add_handler(self, handler):
		"""
		*handler* should be an instance of :class:`BaseHandler`.  The following
		methods are searched, and added to the possible chains (note that HTTP errors
		are a special case).
		
		* :samp:`{protocol}_open` --- signal that the handler knows how to open
		*protocol* URLs.
		
		* :samp:`http_error_{type}` --- signal that the handler knows how to handle
		HTTP errors with HTTP error code *type*.
		
		* :samp:`{protocol}_error` --- signal that the handler knows how to handle
		errors from (non-\ ``http``) *protocol*.
		
		* :samp:`{protocol}_request` --- signal that the handler knows how to
		pre-process *protocol* requests.
		
		* :samp:`{protocol}_response` --- signal that the handler knows how to
		post-process *protocol* responses.
		
		
		"""
		pass
		
	def open(self, url,data,timeout):
		"""
		Open the given *url* (which can be a request object or a string), optionally
		passing the given *data*. Arguments, return values and exceptions raised are
		the same as those of :func:`urlopen` (which simply calls the :meth:`open`
		method on the currently installed global :class:`OpenerDirector`).  The
		optional *timeout* parameter specifies a timeout in seconds for blocking
		operations like the connection attempt (if not specified, the global default
		timeout setting will be used). The timeout feature actually works only for
		HTTP, HTTPS and FTP connections).
		
		"""
		pass
		
	def error(self, proto,arg,more):
		"""
		Handle an error of the given protocol.  This will call the registered error
		handlers for the given protocol with the given arguments (which are protocol
		specific).  The HTTP protocol is a special case which uses the HTTP response
		code to determine the specific error handler; refer to the :meth:`http_error_\*`
		methods of the handler classes.
		
		Return values and exceptions raised are the same as those of :func:`urlopen`.
		
		OpenerDirector objects open URLs in three stages:
		
		The order in which these methods are called within each stage is determined by
		sorting the handler instances.
		
		#. Every handler with a method named like :samp:`{protocol}_request` has that
		method called to pre-process the request.
		
		#. Handlers with a method named like :samp:`{protocol}_open` are called to handle
		the request. This stage ends when a handler either returns a non-\ :const:`None`
		value (ie. a response), or raises an exception (usually :exc:`URLError`).
		Exceptions are allowed to propagate.
		
		In fact, the above algorithm is first tried for methods named
		:meth:`default_open`.  If all such methods return :const:`None`, the
		algorithm is repeated for methods named like :samp:`{protocol}_open`.  If all
		such methods return :const:`None`, the algorithm is repeated for methods
		named :meth:`unknown_open`.
		
		Note that the implementation of these methods may involve calls of the parent
		:class:`OpenerDirector` instance's :meth:`~OpenerDirector.open` and
		:meth:`~OpenerDirector.error` methods.
		
		#. Every handler with a method named like :samp:`{protocol}_response` has that
		method called to post-process the response.
		
		
		.. aseHandler Objects
		-------------------
		
		:class:`BaseHandler` objects provide a couple of methods that are directly
		useful, and others that are meant to be used by derived classes.  These are
		intended for direct use:
		
		
		"""
		pass
		
	


class BaseHandler:


	"""
	This is the base class for all registered handlers --- and handles only the
	simple mechanics of registration.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def add_parent(self, director):
		"""
		Add a director as parent.
		
		
		"""
		pass
		
	def close(self, ):
		"""
		Remove any parents.
		
		The following members and methods should only be used by classes derived from
		:class:`BaseHandler`.
		
		"""
		pass
		
	def default_open(self, req):
		"""
		This method is *not* defined in :class:`BaseHandler`, but subclasses should
		define it if they want to catch all URLs.
		
		This method, if implemented, will be called by the parent
		:class:`OpenerDirector`.  It should return a file-like object as described in
		the return value of the :meth:`open` of :class:`OpenerDirector`, or ``None``.
		It should raise :exc:`URLError`, unless a truly exceptional thing happens (for
		example, :exc:`MemoryError` should not be mapped to :exc:`URLError`).
		
		This method will be called before any protocol-specific open method.
		
		
		"""
		pass
		
	def protocol_open(self, req):
		""":noindex:
		
		("protocol" is to be replaced by the protocol name.)
		
		This method is *not* defined in :class:`BaseHandler`, but subclasses should
		define it if they want to handle URLs with the given *protocol*.
		
		This method, if defined, will be called by the parent :class:`OpenerDirector`.
		Return values should be the same as for  :meth:`default_open`.
		
		
		"""
		pass
		
	def unknown_open(self, req):
		"""
		This method is *not* defined in :class:`BaseHandler`, but subclasses should
		define it if they want to catch all URLs with no specific registered handler to
		open it.
		
		This method, if implemented, will be called by the :attr:`parent`
		:class:`OpenerDirector`.  Return values should be the same as for
		:meth:`default_open`.
		
		
		"""
		pass
		
	def http_error_default(self, req,fp,code,msg,hdrs):
		"""
		This method is *not* defined in :class:`BaseHandler`, but subclasses should
		override it if they intend to provide a catch-all for otherwise unhandled HTTP
		errors.  It will be called automatically by the  :class:`OpenerDirector` getting
		the error, and should not normally be called in other circumstances.
		
		*req* will be a :class:`Request` object, *fp* will be a file-like object with
		the HTTP error body, *code* will be the three-digit code of the error, *msg*
		will be the user-visible explanation of the code and *hdrs* will be a mapping
		object with the headers of the error.
		
		Return values and exceptions raised should be the same as those of
		:func:`urlopen`.
		
		
		"""
		pass
		
	def http_error_nnn(self, req,fp,code,msg,hdrs):
		"""
		*nnn* should be a three-digit HTTP error code.  This method is also not defined
		in :class:`BaseHandler`, but will be called, if it exists, on an instance of a
		subclass, when an HTTP error with code *nnn* occurs.
		
		Subclasses should override this method to handle specific HTTP errors.
		
		Arguments, return values and exceptions raised should be the same as for
		:meth:`http_error_default`.
		
		
		"""
		pass
		
	def protocol_request(self, req):
		""":noindex:
		
		("protocol" is to be replaced by the protocol name.)
		
		This method is *not* defined in :class:`BaseHandler`, but subclasses should
		define it if they want to pre-process requests of the given *protocol*.
		
		This method, if defined, will be called by the parent :class:`OpenerDirector`.
		*req* will be a :class:`Request` object. The return value should be a
		:class:`Request` object.
		
		
		"""
		pass
		
	def protocol_response(self, req,response):
		""":noindex:
		
		("protocol" is to be replaced by the protocol name.)
		
		This method is *not* defined in :class:`BaseHandler`, but subclasses should
		define it if they want to post-process responses of the given *protocol*.
		
		This method, if defined, will be called by the parent :class:`OpenerDirector`.
		*req* will be a :class:`Request` object. *response* will be an object
		implementing the same interface as the return value of :func:`urlopen`.  The
		return value should implement the same interface as the return value of
		:func:`urlopen`.
		
		
		.. TTPRedirectHandler Objects
		---------------------------
		
		"""
		pass
		
	


class HTTPDefaultErrorHandler:


	"""
	A class which defines a default handler for HTTP error responses; all responses
	are turned into :exc:`HTTPError` exceptions.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class HTTPRedirectHandler:


	"""
	A class to handle redirections.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def redirect_request(self, req,fp,code,msg,hdrs,newurl):
		"""
		Return a :class:`Request` or ``None`` in response to a redirect. This is called
		by the default implementations of the :meth:`http_error_30\*` methods when a
		redirection is received from the server.  If a redirection should take place,
		return a new :class:`Request` to allow :meth:`http_error_30\*` to perform the
		redirect to *newurl*.  Otherwise, raise :exc:`HTTPError` if no other handler
		should try to handle this URL, or return ``None`` if you can't but another
		handler might.
		
		"""
		pass
		
	def http_error_301(self, req,fp,code,msg,hdrs):
		"""
		Redirect to the ``Location:`` or ``URI:`` URL.  This method is called by the
		parent :class:`OpenerDirector` when getting an HTTP 'moved permanently' response.
		
		
		"""
		pass
		
	def http_error_302(self, req,fp,code,msg,hdrs):
		"""
		The same as :meth:`http_error_301`, but called for the 'found' response.
		
		
		"""
		pass
		
	def http_error_303(self, req,fp,code,msg,hdrs):
		"""
		The same as :meth:`http_error_301`, but called for the 'see other' response.
		
		
		"""
		pass
		
	def http_error_307(self, req,fp,code,msg,hdrs):
		"""
		The same as :meth:`http_error_301`, but called for the 'temporary redirect'
		response.
		
		
		.. TTPCookieProcessor Objects
		---------------------------
		
		"""
		pass
		
	


class HTTPCookieProcessor:


	"""
	A class to handle HTTP Cookies.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class ProxyHandler:


	"""
	Cause requests to go through a proxy. If *proxies* is given, it must be a
	dictionary mapping protocol names to URLs of proxies. The default is to read
	the list of proxies from the environment variables
	:envvar:`<protocol>_proxy`.  If no proxy environment variables are set, in a
	Windows environment, proxy settings are obtained from the registry's
	Internet Settings section and in a Mac OS X  environment, proxy information
	is retrieved from the OS X System Configuration Framework.
	
	To disable autodetected proxy pass an empty dictionary.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def protocol_open(self, request):
		""":noindex:
		
		("protocol" is to be replaced by the protocol name.)
		
		The :class:`ProxyHandler` will have a method :samp:`{protocol}_open` for every
		*protocol* which has a proxy in the *proxies* dictionary given in the
		constructor.  The method will modify requests to go through the proxy, by
		calling ``request.set_proxy()``, and call the next handler in the chain to
		actually execute the protocol.
		
		
		.. TTPPasswordMgr Objects
		-----------------------
		
		These methods are available on :class:`HTTPPasswordMgr` and
		:class:`HTTPPasswordMgrWithDefaultRealm` objects.
		
		
		"""
		pass
		
	


class HTTPPasswordMgr:


	"""
	Keep a database of  ``(realm, uri) -> (user, password)`` mappings.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def add_password(self, realm,uri,user,passwd):
		"""
		*uri* can be either a single URI, or a sequence of URIs. *realm*, *user* and
		*passwd* must be strings. This causes ``(user, passwd)`` to be used as
		authentication tokens when authentication for *realm* and a super-URI of any of
		the given URIs is given.
		
		
		"""
		pass
		
	def find_user_password(self, realm,authuri):
		"""
		Get user/password for given realm and URI, if any.  This method will return
		``(None, None)`` if there is no matching user/password.
		
		For :class:`HTTPPasswordMgrWithDefaultRealm` objects, the realm ``None`` will be
		searched if the given *realm* has no matching user/password.
		
		
		.. bstractBasicAuthHandler Objects
		--------------------------------
		
		
		"""
		pass
		
	


class HTTPPasswordMgrWithDefaultRealm:


	"""
	Keep a database of  ``(realm, uri) -> (user, password)`` mappings. A realm of
	``None`` is considered a catch-all realm, which is searched if no other realm
	fits.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class AbstractBasicAuthHandler:


	"""
	This is a mixin class that helps with HTTP authentication, both to the remote
	host and to a proxy. *password_mgr*, if given, should be something that is
	compatible with :class:`HTTPPasswordMgr`; refer to section
	:ref:`http-password-mgr` for information on the interface that must be
	supported.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def http_error_auth_reqed(self, authreq,host,req,headers):
		"""
		Handle an authentication request by getting a user/password pair, and re-trying
		the request.  *authreq* should be the name of the header where the information
		about the realm is included in the request, *host* specifies the URL and path to
		authenticate for, *req* should be the (failed) :class:`Request` object, and
		*headers* should be the error headers.
		
		*host* is either an authority (e.g. ``"python.org"``) or a URL containing an
		authority component (e.g. ``"http://python.org/"``). In either case, the
		authority must not contain a userinfo component (so, ``"python.org"`` and
		``"python.org:80"`` are fine, ``"joe:password@python.org"`` is not).
		
		
		.. TTPBasicAuthHandler Objects
		----------------------------
		
		
		"""
		pass
		
	


class HTTPBasicAuthHandler:


	"""
	Handle authentication with the remote host. *password_mgr*, if given, should be
	something that is compatible with :class:`HTTPPasswordMgr`; refer to section
	:ref:`http-password-mgr` for information on the interface that must be
	supported.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def http_error_401(self, req,fp,code,msg,hdrs):
		"""
		Retry the request with authentication information, if available.
		
		
		.. roxyBasicAuthHandler Objects
		-----------------------------
		
		
		"""
		pass
		
	


class ProxyBasicAuthHandler:


	"""
	Handle authentication with the proxy. *password_mgr*, if given, should be
	something that is compatible with :class:`HTTPPasswordMgr`; refer to section
	:ref:`http-password-mgr` for information on the interface that must be
	supported.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def http_error_407(self, req,fp,code,msg,hdrs):
		"""
		Retry the request with authentication information, if available.
		
		
		.. bstractDigestAuthHandler Objects
		---------------------------------
		
		
		"""
		pass
		
	


class AbstractDigestAuthHandler:


	"""
	This is a mixin class that helps with HTTP authentication, both to the remote
	host and to a proxy. *password_mgr*, if given, should be something that is
	compatible with :class:`HTTPPasswordMgr`; refer to section
	:ref:`http-password-mgr` for information on the interface that must be
	supported.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def http_error_auth_reqed(self, authreq,host,req,headers):
		"""
		*authreq* should be the name of the header where the information about the realm
		is included in the request, *host* should be the host to authenticate to, *req*
		should be the (failed) :class:`Request` object, and *headers* should be the
		error headers.
		
		
		.. TTPDigestAuthHandler Objects
		-----------------------------
		
		
		"""
		pass
		
	


class HTTPDigestAuthHandler:


	"""
	Handle authentication with the remote host. *password_mgr*, if given, should be
	something that is compatible with :class:`HTTPPasswordMgr`; refer to section
	:ref:`http-password-mgr` for information on the interface that must be
	supported.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def http_error_401(self, req,fp,code,msg,hdrs):
		"""
		Retry the request with authentication information, if available.
		
		
		.. roxyDigestAuthHandler Objects
		------------------------------
		
		
		"""
		pass
		
	


class ProxyDigestAuthHandler:


	"""
	Handle authentication with the proxy. *password_mgr*, if given, should be
	something that is compatible with :class:`HTTPPasswordMgr`; refer to section
	:ref:`http-password-mgr` for information on the interface that must be
	supported.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def http_error_407(self, req,fp,code,msg,hdrs):
		"""
		Retry the request with authentication information, if available.
		
		
		.. TTPHandler Objects
		-------------------
		
		
		"""
		pass
		
	


class HTTPHandler:


	"""
	A class to handle opening of HTTP URLs.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def http_open(self, req):
		"""
		Send an HTTP request, which can be either GET or POST, depending on
		``req.has_data()``.
		
		
		.. TTPSHandler Objects
		--------------------
		
		
		"""
		pass
		
	


class HTTPSHandler:


	"""
	A class to handle opening of HTTPS URLs.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def https_open(self, req):
		"""
		Send an HTTPS request, which can be either GET or POST, depending on
		``req.has_data()``.
		
		
		.. ileHandler Objects
		-------------------
		
		
		"""
		pass
		
	


class FileHandler:


	"""
	Open local files.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def file_open(self, req):
		"""
		Open the file locally, if there is no host name, or the host name is
		``'localhost'``. Change the protocol to ``ftp`` otherwise, and retry opening it
		using :attr:`parent`.
		
		
		.. TPHandler Objects
		------------------
		
		
		"""
		pass
		
	


class FTPHandler:


	"""
	Open FTP URLs.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def ftp_open(self, req):
		"""
		Open the FTP file indicated by *req*. The login is always done with empty
		username and password.
		
		
		.. acheFTPHandler Objects
		-----------------------
		
		:class:`CacheFTPHandler` objects are :class:`FTPHandler` objects with the
		following additional methods:
		
		
		"""
		pass
		
	


class CacheFTPHandler:


	"""
	Open FTP URLs, keeping a cache of open FTP connections to minimize delays.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def setTimeout(self, t):
		"""
		Set timeout of connections to *t* seconds.
		
		
		"""
		pass
		
	def setMaxConns(self, m):
		"""
		Set maximum number of cached connections to *m*.
		
		
		.. nknownHandler Objects
		----------------------
		
		
		"""
		pass
		
	


class UnknownHandler:


	"""
	A catch-all class to handle unknown URLs.
	
	
	.. equest Objects
	---------------
	
	The following methods describe all of :class:`Request`'s public interface, and
	so all must be overridden in subclasses.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def unknown_open(self, ):
		"""
		Raise a :exc:`URLError` exception.
		
		
		.. TTPErrorProcessor Objects
		--------------------------
		
		"""
		pass
		
	


