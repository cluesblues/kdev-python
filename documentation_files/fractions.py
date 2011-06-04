#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Rational numbers.
"""
class Fraction:


	"""Fraction(other_fraction)
	Fraction(float)
	Fraction(decimal)
	Fraction(string)
	
	The first version requires that *numerator* and *denominator* are instances
	of :class:`numbers.Rational` and returns a new :class:`Fraction` instance
	with value ``numerator/denominator``. If *denominator* is :const:`0`, it
	raises a :exc:`ZeroDivisionError`. The second version requires that
	*other_fraction* is an instance of :class:`numbers.Rational` and returns a
	:class:`Fraction` instance with the same value.  The next two versions accept
	either a :class:`float` or a :class:`decimal.Decimal` instance, and return a
	:class:`Fraction` instance with exactly the same value.  Note that due to the
	usual issues with binary floating-point (see :ref:`tut-fp-issues`), the
	argument to ``Fraction(1.1)`` is not exactly equal to 11/10, and so
	``Fraction(1.1)`` does *not* return ``Fraction(11, 10)`` as one might expect.
	(But see the documentation for the :meth:`limit_denominator` method below.)
	The last version of the constructor expects a string or unicode instance.
	The usual form for this instance is::
	
	[sign] numerator ['/' denominator]
	
	where the optional ``sign`` may be either '+' or '-' and
	``numerator`` and ``denominator`` (if present) are strings of
	decimal digits.  In addition, any string that represents a finite
	value and is accepted by the :class:`float` constructor is also
	accepted by the :class:`Fraction` constructor.  In either form the
	input string may also have leading and/or trailing whitespace.
	Here are some examples::
	
	>>> from fractions import Fraction
	>>> Fraction(16, -10)
	Fraction(-8, 5)
	>>> Fraction(123)
	Fraction(123, 1)
	>>> Fraction()
	Fraction(0, 1)
	>>> Fraction('3/7')
	Fraction(3, 7)
	[40794 refs]
	>>> Fraction(' -3/7 ')
	Fraction(-3, 7)
	>>> Fraction('1.414213 \t\n')
	Fraction(1414213, 1000000)
	>>> Fraction('-.125')
	Fraction(-1, 8)
	>>> Fraction('7e-6')
	Fraction(7, 1000000)
	>>> Fraction(2.25)
	Fraction(9, 4)
	>>> Fraction(1.1)
	Fraction(2476979795053773, 2251799813685248)
	>>> from decimal import Decimal
	>>> Fraction(Decimal('1.1'))
	Fraction(11, 10)
	
	
	The :class:`Fraction` class inherits from the abstract base class
	:class:`numbers.Rational`, and implements all of the methods and
	operations from that class.  :class:`Fraction` instances are hashable,
	and should be treated as immutable.  In addition,
	:class:`Fraction` has the following methods:
	
	"""
	
	
	def __init__(self, numerator=0,denominator=1):
		pass
	
	def gcd(a,b):
		"""
		Return the greatest common divisor of the integers *a* and *b*.  If either
		*a* or *b* is nonzero, then the absolute value of ``gcd(a, b)`` is the
		largest integer that divides both *a* and *b*.  ``gcd(a,b)`` has the same
		sign as *b* if *b* is nonzero; otherwise it takes the sign of *a*.  ``gcd(0,
		0)`` returns ``0``.
		
		
		"""
		pass
		
	


