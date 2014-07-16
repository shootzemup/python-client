# -*- coding: utf8 -*-

from threading import Thread
import logging
import time
from functools import wraps

from authenticator import Authenticator


instance = None


def singletonize(method):
	@wraps(method)
	def wrapper(*args, **kwargs):
		return method(instance, *args, **kwargs)
	return wrapper


def init():
	global instance
	instance = Net()
	instance.start()


class Net(Thread):
	"""Represents a the networking client that runs on a separate thread."""
	def __init__(self):
		super(Net, self).__init__()
		self._done = False
		self._authent = Authenticator()
		# list of tuple query, parameters..,  callback
		self._queries = []
		self._routes = {
			'authenticate': self._authent.authenticate,
			'create_account': self._authent.createAccount
		}

	def run(self):
		""" Run the threading client """
		logging.info("Starting network client thread.")
		while not self._done:
			if len(self._queries) > 0:
				query, args, callback = self._queries.pop()
				logging.debug("Wating query found: %s, %s, %s" 
							  % (query, args, callback))
				self._routes[query](*args, callback=callback)
			else:
				time.sleep(2)

		logging.info("Stoping network client thread.")

	def stop(self):
		"""
		Stop the networking thread
		"""
		logging.info("Will stop the thread...")
		self._done = True

	def authenticate(self, username, password, callback):
		"""
		Send an authentication request the the authentication server.
		username -- name of the user to authenticate
		password -- the password of the user, it will be hashed before sending
		callback -- a function (err, data) to be called when the answer of the 
					server is retrieved.
		"""
		self._queries.append(('authenticate', (username, password), callback))

stop = singletonize(Net.stop)
authenticate = singletonize(Net.authenticate)
