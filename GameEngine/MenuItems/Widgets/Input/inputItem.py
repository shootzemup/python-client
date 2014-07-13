# -*- coding: utf8 -*-

import logging

from inputItemModel import InputItemModel
from inputItemBehaviour import InputItemBehaviour
from inputItemView import InputItemView
from GameEngine.MenuItems.menuItem import MenuItem
# from GameEngine.MenuItems.Widgets.Label.labelItem import LabelItem


class InputItem(MenuItem):
	"""Represent a menu item that display a string"""
	def __init__(self, **kwargs):
		"""
		Initialize a new InputItem
		**kwargs -- all the arguments will be given to the InputItemModel
		"""
		# a label item is made of a label model, view and behaviour
		model = InputItemModel(**kwargs)
		behaviour = InputItemBehaviour(model)
		view = InputItemView(model)
		super(InputItem, self).__init__(
			menuItemModel=model, menuItemBehaviour=behaviour,
			menuItemView=view)
		logging.log(1, "Trace: InputItem.__init__(%s)" 
						% (kwargs))

	def focus(self):
		""" Let the behaviour make the model focused """
		return self._behaviour.focus()

	def unfocus(self):
		""" Let the behaviour make the model unfocused """
		self._behaviour.unfocus()
