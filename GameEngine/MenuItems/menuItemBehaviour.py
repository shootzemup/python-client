# -*- coding: utf8 -*-

import logging


class MenuItemBehaviour(object):
	"""
        Handle the behaviour of a default menu item
	"""
	def __init__(self, model):
		"""
		Initialize the behaviour of the menu item
		model -- the model of the menu item
		"""
		super(MenuItemBehaviour, self).__init__()
		self._model = model
	
	def handleEvent(self, event):
		logging.log(1, "Trace: MenuItemBehaviour.handleEvent(%s)" % event)

	def handlePressed(self, kbs, ms):
		logging.log(1, "Trace: MenuItemBehaviour.handlePressed(...)")

	def update(self, stateManager):
		logging.log(1, "Trace: MenuItemBehaviour.update(...)")
