# -*- coding: utf8 -*-

import logging
from state import State


class MenuState(State):
	"""
	Represent the main menu state of the game.
	The purpose of this state is to display the authentication menu
	and the game mode choosing menu. It may also display some other stuff 
	in the future.
	"""
	def __init__(self):
		super(MenuState, self).__init__()
		logging.log(1, "Trace: MenuState.__init__()")

	def handleEvent(self, event):
		logging.log(1, "Trace: MenuState.handleEvent(%s)" % event)

	def handlePressed(self, kbs, ms):
		logging.log(1, "Trace: MenuState.handlePressed(...)")

	def update(self, stateManager):
		logging.log(1, "Trace: MenuState.update(%s)" % stateManager)

	def render(self, interpolation):
		logging.log(1, "Trace: MenuState.render(%.5f)" % interpolation)
		