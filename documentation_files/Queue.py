#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: A synchronized queue class.

"""
class Queue:


	"""
	Constructor for a FIFO queue.  *maxsize* is an integer that sets the upperbound
	limit on the number of items that can be placed in the queue.  Insertion will
	block once this size has been reached, until queue items are consumed.  If
	*maxsize* is less than or equal to zero, the queue size is infinite.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def qsize(self, ):
		"""
		Return the approximate size of the queue.  Note, qsize() > 0 doesn't
		guarantee that a subsequent get() will not block, nor will qsize() < maxsize
		guarantee that put() will not block.
		
		
		"""
		pass
		
	def empty(self, ):
		"""
		Return ``True`` if the queue is empty, ``False`` otherwise.  If empty()
		returns ``True`` it doesn't guarantee that a subsequent call to put()
		will not block.  Similarly, if empty() returns ``False`` it doesn't
		guarantee that a subsequent call to get() will not block.
		
		
		"""
		pass
		
	def full(self, ):
		"""
		Return ``True`` if the queue is full, ``False`` otherwise.  If full()
		returns ``True`` it doesn't guarantee that a subsequent call to get()
		will not block.  Similarly, if full() returns ``False`` it doesn't
		guarantee that a subsequent call to put() will not block.
		
		
		"""
		pass
		
	def put(self, item,block,timeout):
		"""
		Put *item* into the queue. If optional args *block* is true and *timeout* is
		None (the default), block if necessary until a free slot is available. If
		*timeout* is a positive number, it blocks at most *timeout* seconds and raises
		the :exc:`Full` exception if no free slot was available within that time.
		Otherwise (*block* is false), put an item on the queue if a free slot is
		immediately available, else raise the :exc:`Full` exception (*timeout* is
		ignored in that case).
		
		"""
		pass
		
	def put_nowait(self, item):
		"""
		Equivalent to ``put(item, False)``.
		
		
		"""
		pass
		
	def get(self, block,timeout):
		"""
		Remove and return an item from the queue. If optional args *block* is true and
		*timeout* is None (the default), block if necessary until an item is available.
		If *timeout* is a positive number, it blocks at most *timeout* seconds and
		raises the :exc:`Empty` exception if no item was available within that time.
		Otherwise (*block* is false), return an item if one is immediately available,
		else raise the :exc:`Empty` exception (*timeout* is ignored in that case).
		
		"""
		pass
		
	def get_nowait(self, ):
		"""
		Equivalent to ``get(False)``.
		
		Two methods are offered to support tracking whether enqueued tasks have been
		fully processed by daemon consumer threads.
		
		
		"""
		pass
		
	def task_done(self, ):
		"""
		Indicate that a formerly enqueued task is complete.  Used by queue consumer
		threads.  For each :meth:`get` used to fetch a task, a subsequent call to
		:meth:`task_done` tells the queue that the processing on the task is complete.
		
		If a :meth:`join` is currently blocking, it will resume when all items have been
		processed (meaning that a :meth:`task_done` call was received for every item
		that had been :meth:`put` into the queue).
		
		Raises a :exc:`ValueError` if called more times than there were items placed in
		the queue.
		
		"""
		pass
		
	def join(self, ):
		"""
		Blocks until all items in the queue have been gotten and processed.
		
		The count of unfinished tasks goes up whenever an item is added to the queue.
		The count goes down whenever a consumer thread calls :meth:`task_done` to
		indicate that the item was retrieved and all work on it is complete. When the
		count of unfinished tasks drops to zero, :meth:`join` unblocks.
		
		"""
		pass
		
	


class LifoQueue:


	"""
	Constructor for a LIFO queue.  *maxsize* is an integer that sets the upperbound
	limit on the number of items that can be placed in the queue.  Insertion will
	block once this size has been reached, until queue items are consumed.  If
	*maxsize* is less than or equal to zero, the queue size is infinite.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class PriorityQueue:


	"""
	Constructor for a priority queue.  *maxsize* is an integer that sets the upperbound
	limit on the number of items that can be placed in the queue.  Insertion will
	block once this size has been reached, until queue items are consumed.  If
	*maxsize* is less than or equal to zero, the queue size is infinite.
	
	The lowest valued entries are retrieved first (the lowest valued entry is the
	one returned by ``sorted(list(entries))[0]``).  A typical pattern for entries
	is a tuple in the form: ``(priority_number, data)``.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


