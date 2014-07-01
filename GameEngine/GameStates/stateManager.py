# -*- coding: utf8 -*-

import logging

from conf import conf
from introState import IntroState


class StateManager(object):
	"""Manage the state stack of the game"""
	def __init__(self):
		super(StateManager, self).__init__()
		logging.log(1, "Trace: StateManager.__init__()")
		self._state_stack = []
		# when initalizing, the introstate is the first to be
		# pushed on the stack
		self.pushState(IntroState.getInstance())

	# handle a single event from the event queue
	def handleEvent(self, event):
		logging.log(1, 'Trace: StateManager.handleEvent(%s)' % event)

	# handle the keyboard and the mouse state
	def handlePressed(self, kbs, ms):
		logging.log(1, 'Trace: StateManager.handlePressed(...)')

	def update(self):
		logging.log(1, "Trace: StateManager.update()")
		for state in self._state_stack:
			state.update(self)

	def render(self, interpolation):
		logging.log(1, "Trace: StateManager.render(%.5f)" % interpolation)
		for state in self._state_stack:
			state.render(interpolation)

	def popState(self):
		logging.log(1, "Trace: StateManager.popState()")
		self._state_stack.pop()

	def pushState(self, state):
		logging.log(1, "Trace: StateManager.pushState(%s)" % state)
		self._state_stack.append(state)

	def changeState(self, state):
		logging.log(1, "Trace: StateManager.changeState(%s)" % state)
		self.popState()
		self.pushState(state)
