# -*- coding: utf8 -*-

import logging
from menuItemBehaviour import MenuItemBehaviour
from menuItemView import MenuItemView
from menuItemModel import MenuItemModel
from conf import conf


class MenuItem(object):
	"""
	Represent any MenuItem of the menu. 
	Any menu item must be included in a container.
	A menu item uses a behaviour to update its internal data, a model to
	store its internal data and a view to display it.
	"""
	def __init__(self, menuItemModel=None, menuItemBehaviour=None, 
				menuItemView=None, **kwargs):
		"""
		Initialize the menu item
		menuItemModel -- a custom model for this menu item. Note that if
						 this parameter is provided, all the other (except
						 menuItemBehaviour and menuItemView) will be ignored
		menuItemBehaviour -- a custom behaviour for this menu item
		menuItemView -- a custom view for this menu item
		kwargs -- the keywords arguments are given to the menuItemModel
		"""
		super(MenuItem, self).__init__()
		logging.log(1, "Trace: MenuItem.__init__(%s)"
						% (kwargs))
		if menuItemModel is None:
			self._model = MenuItemModel(**kwargs)
		else:
			self._model = menuItemModel

		if menuItemBehaviour is None:
			self._behaviour = MenuItemBehaviour(self._model)
		else:
			self._behaviour = menuItemBehaviour

		if menuItemView is None:
			self._view = MenuItemView(self._model)
		else:
			self._view = menuItemView

	def update(self, stateManager):
		"""
		Let the behaviour of the menu item update the item
		"""
		self._behaviour.update(stateManager)

	def computeSize(self, parentPos, parentSize):
		"""
		Let the behaviour of the menuitem compute the real size of the item
		"""
		self._behaviour.computeSize(parentPos, parentSize)

	def render(self, interpolation):
		"""
		Let the view of the menu item render the item
		"""
		self._view.render(interpolation)

