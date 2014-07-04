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
	def __init__(self, imageLink=None, initPos=(0,0), initSize=(1, 1), 
				absolute=False, itemName="Unamed"):
		"""
		Initialize the menu item
		imageLink -- link to the image corresponding to this menu item
		initPos -- the initial position of the item to set as the center of the 
				   surface. If `absolute` is `False` (default), the
				   position will be a percentage of the size of
				   the object, starting from the center.
				   eg: (1, -1) will be the upper left
		initSize -- the initial size of the item.
		absolute -- if set to `True`, the position and the size will be used as
					stated. If no, the size and the position will be computed
					from the size of the parent at render time
		itemName -- used only for debugging identification
		"""
		super(MenuItem, self).__init__()
		logging.log(1, "Trace: MenuItem.__init__(%s, %s, %s, %s)"
						% (imageLink, initPos, initSize, absolute))
		if imageLink is None:
			imageLink = conf['resources']['menu']['default_menu_item']
		self._model = MenuItemModel(imageLink, initPos, initSize, absolute, 
									itemName)
		self._behaviour = MenuItemBehaviour(self._model)
		self._view = MenuItemView(self._model)

	def handleEvent(self, event):
		"""
		Let the behaviour of the menu item handle the event
		"""
		logging.log(1, "Trace: MenuItem.handleEvent(%s)" % event)
		self._behaviour.handleEvent(event)

	def handlePressed(self, kbs, ms):
		"""
		Let the behaviour of the menu item handle the pressed keys
		"""
		logging.log(1, "Trace: MenuItem.handlePressed(...)")
		self._behaviour.handlePressed(kbs, ms)

	def update(self, stateManager):
		"""
		Let the behaviour of the menu item update the item
		"""
		logging.log(1, "Trace: MenuItem.update(...)")
		self._behaviour.update(stateManager)

	def render(self, interpolation, parentPos, parentSize):
		"""
		Let the view of the menu item render the item
		"""
		logging.log(1, "Trace: MenuItem.render(%.5f)" % interpolation)
		self._view.render(interpolation, parentPos, parentSize)

