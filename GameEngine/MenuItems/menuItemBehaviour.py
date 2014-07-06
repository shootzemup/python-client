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
	
	def update(self, stateManager):
		logging.log(1, "Trace: MenuItemBehaviour.update(...)")
