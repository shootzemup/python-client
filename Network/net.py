# -*- coding: utf8 -*-

from threading import Thread
import logging


class Net(Thread):
	"""Represents a the networking client that runs on a separate thread."""
	def __init__(self):
		super(Net, self).__init__()
		self._done = False

	def run(self):
		""" Run the threading client """
		logging.info("Starting network client's thread.")
		while not self._done:
			pass

	def stop(self):
		self._done = True