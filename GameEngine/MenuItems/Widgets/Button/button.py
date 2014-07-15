# -*- coding: utf8 -*-

import logging
from buttonBehaviour import ButtonBehaviour
from GameEngine.MenuItems.menuItemView import MenuItemView
from buttonModel import ButtonModel
from GameEngine.MenuItems.menuItem import MenuItem


class Button(MenuItem):
	"""Represents a button"""
	def __init__(self, **kwargs):
		"""
		Initialize a new button.
		**kwargs -- All the arguments will be given to the ButtonModel.
		"""
		model = ButtonModel(**kwargs)
		behaviour = ButtonBehaviour(model)
		view = MenuItemView(model)
		super(Button, self).__init__(menuItemModel=model,
			menuItemBehaviour=behaviour, menuItemView=view)
	
	def focus(self):
		""" Let the behaviour make the model focused """
		return self._behaviour.focus()

	def unfocus(self):
		""" Let the behaviour make the model unfocused """
		self._behaviour.unfocus()

	def press(self):
		""" 
		Press the button and trigger the events related to the button press
		"""
		self._behaviour.press()
		self._behaviour.release()

	def onPressed(self, callback):
		""" Add a callback to be called when to button is pressed """
		self._model.onPressed(callback)

	def offPressed(self):
		""" Remove all the callback registered to be called on button press """
		self._model.offPressed()


