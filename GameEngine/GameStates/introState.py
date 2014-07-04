# -*- coding: utf8 -*-

import logging

from conf import conf
from state import State
from authentState import AuthentState
from Graphx import graphx


class IntroState(State):
	"""
	Represent the introduction state of the game.
	The purpose of this state is to display introduction credit
	that are dsplayed at the beginning of the game
	"""
	def __init__(self):
		super(IntroState, self).__init__()
		logging.log(1, "Trace: IntroState.__init__()")
		self._state_manager = None
		graphx.playVideo(conf['resources']['intro_video'], self.endState)

	def handleEvent(self, event):
		logging.log(1, "Trace: IntroState.handleEvent(%s)" % event)

	def handlePressed(self, kbs, ms):
		logging.log(1, "Trace: IntroState.handlePressed(...)")

	def endState(self):
		logging.info("Changing state to AuthentState.")
		self._state_manager.changeState(AuthentState.getInstance())

	def update(self, stateManager):
		logging.log(1, "Trace: IntroState.update(%s)" % stateManager)
		self._state_manager = stateManager

	def render(self, interpolation):
		logging.log(1, "Trace: IntroState.render(%.5f)" % interpolation)
		