#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Tools for converting between binary and various ASCII-encoded binary
representations.


"""
def a2b_uu(string):
	"""
	Convert a single line of uuencoded data back to binary and return the binary
	data. Lines normally contain 45 (binary) bytes, except for the last line. Line
	data may be followed by whitespace.
	
	
	"""
	pass
	
def b2a_uu(data):
	"""
	Convert binary data to a line of ASCII characters, the return value is the
	converted line, including a newline char. The length of *data* should be at most
	45.
	
	
	"""
	pass
	
def a2b_base64(string):
	"""
	Convert a block of base64 data back to binary and return the binary data. More
	than one line may be passed at a time.
	
	
	"""
	pass
	
def b2a_base64(data):
	"""
	Convert binary data to a line of ASCII characters in base64 coding. The return
	value is the converted line, including a newline char. The length of *data*
	should be at most 57 to adhere to the base64 standard.
	
	
	"""
	pass
	
def a2b_qp(string,header):
	"""
	Convert a block of quoted-printable data back to binary and return the binary
	data. More than one line may be passed at a time. If the optional argument
	*header* is present and true, underscores will be decoded as spaces.
	
	
	"""
	pass
	
def b2a_qp(data,quotetabs,istext,header):
	"""
	Convert binary data to a line(s) of ASCII characters in quoted-printable
	encoding.  The return value is the converted line(s). If the optional argument
	*quotetabs* is present and true, all tabs and spaces will be encoded.   If the
	optional argument *istext* is present and true, newlines are not encoded but
	trailing whitespace will be encoded. If the optional argument *header* is
	present and true, spaces will be encoded as underscores per RFC1522. If the
	optional argument *header* is present and false, newline characters will be
	encoded as well; otherwise linefeed conversion might corrupt the binary data
	stream.
	
	
	"""
	pass
	
def a2b_hqx(string):
	"""
	Convert binhex4 formatted ASCII data to binary, without doing RLE-decompression.
	The string should contain a complete number of binary bytes, or (in case of the
	last portion of the binhex4 data) have the remaining bits zero.
	
	
	"""
	pass
	
def rledecode_hqx(data):
	"""
	Perform RLE-decompression on the data, as per the binhex4 standard. The
	algorithm uses ``0x90`` after a byte as a repeat indicator, followed by a count.
	A count of ``0`` specifies a byte value of ``0x90``. The routine returns the
	decompressed data, unless data input data ends in an orphaned repeat indicator,
	in which case the :exc:`Incomplete` exception is raised.
	
	
	"""
	pass
	
def rlecode_hqx(data):
	"""
	Perform binhex4 style RLE-compression on *data* and return the result.
	
	
	"""
	pass
	
def b2a_hqx(data):
	"""
	Perform hexbin4 binary-to-ASCII translation and return the resulting string. The
	argument should already be RLE-coded, and have a length divisible by 3 (except
	possibly the last fragment).
	
	
	"""
	pass
	
def crc_hqx(data,crc):
	"""
	Compute the binhex4 crc value of *data*, starting with an initial *crc* and
	returning the result.
	
	
	"""
	pass
	
def crc32(data,crc):
	"""
	Compute CRC-32, the 32-bit checksum of data, starting with an initial crc.  This
	is consistent with the ZIP file checksum.  Since the algorithm is designed for
	use as a checksum algorithm, it is not suitable for use as a general hash
	algorithm.  Use as follows::
	
	print binascii.crc32("hello world")
	# Or, in two pieces:
	crc = binascii.crc32("hello")
	crc = binascii.crc32(" world", crc) & 0xffffffff
	print 'crc32 = 0x%08x' % crc
	
	"""
	pass
	
def b2a_hex(data):
	"""hexlify(data)
	
	Return the hexadecimal representation of the binary *data*.  Every byte of
	*data* is converted into the corresponding 2-digit hex representation.  The
	resulting string is therefore twice as long as the length of *data*.
	
	
	"""
	pass
	
def a2b_hex(hexstr):
	"""unhexlify(hexstr)
	
	Return the binary data represented by the hexadecimal string *hexstr*.  This
	function is the inverse of :func:`b2a_hex`. *hexstr* must contain an even number
	of hexadecimal digits (which can be upper or lower case), otherwise a
	:exc:`TypeError` is raised.
	
	
	"""
	pass
	
