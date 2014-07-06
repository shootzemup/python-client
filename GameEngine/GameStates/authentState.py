# -*- coding: utf8 -*-

import logging
from state import State
from GameEngine.MenuItems.container import Container
from GameEngine.MenuItems.menuItem import MenuItem


class AuthentState(State):
	"""
	Represent the main authentification page of the game.
	The purpose of this state is to display the authentication menu
	and allow the user to connect
	"""
	def __init__(self):
		super(AuthentState, self).__init__()
		logging.log(1, "Trace: AuthentState.__init__()")
		self._page = Container(initSize=(1.0, 1.0), initPos=(0, 0), 
							   itemName="Container")
		menuItem = MenuItem(initSize=(0.25, 0.1), initPos=(0, 0),
							itemName="MenuItem")
		self._page.addMenuItem(menuItem)

	def update(self, stateManager):
		logging.log(1, "Trace: AuthentState.update(%s)" % stateManager)
		self._page.update(stateManager)

	def render(self, interpolation):
		logging.log(1, "Trace: AuthentState.render(%.5f)" % interpolation)
		self._page.render(interpolation)
		import sys
		# sys.exit()
		