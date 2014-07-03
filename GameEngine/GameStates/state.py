# -*- coding: utf8 -*-

import logging
from pprint import pformat


class State(object):
	"""Represent a base state of the game"""
 	_instance = None

	@classmethod
	def createInstance(cls, **kwargs):
		logging.log(1, "Trace: %s.createInstance(%s)" % (cls, pformat(kwargs)))
		if cls._instance is not None and isinstance(cls._instance, cls):
			logging.warning("Overriding existing instance of %s" % cls)
		cls._instance = cls(**kwargs)			

	@classmethod
	def getInstance(cls):
		logging.log(1, "Trace: %s.getInstance()" % (cls))
		if cls._instance is None or not isinstance(cls._instance, cls):
			cls._instance = cls()
		return cls._instance

	def __init__(self):
		super(State, self).__init__()
		logging.log(1, "Trace: State.__init__()")

	def handleEvent(self, event):
		logging.log(1, 'Trace: State.handleEvent(%s)' % event)

	def handlePressed(self, kbs, ms):
		logging.log(1, 'Trace: State.handlePressed(...)')

	def update(self, stateManager):
		logging.log(1, "Trace: State.update(%s)" % stateManager)

	def changeState(self, stateManager, state):
		logging.log(1, "Trace: State.changeState(%s, %s)" 
						% (stateManager, state))
		stateManager.changeState(state)

	def pushState(self, stateManager, state):
		logging.log(1, "Trace: State.pushState(%s, %s)" 
						% (stateManager, state))
		stateManager.pushState(state)

	def popState(self, stateManager):
		logging.log(1, "Trace: State.popState(%s, %s)" 
						% (stateManager))
		stateManager.popState()

	def render(self, interpolation):
		logging.log(1, "Trace: State.render(%.5f)" % interpolation)

