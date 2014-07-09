# -*- coding: utf8 -*-

import logging

from labelItemModel import LabelItemModel
from GameEngine.MenuItems.menuItem import MenuItem


class LabelItem(MenuItem):
	"""Represent a menu item that display a string"""
	def __init__(self, text, **kwargs):
		"""
		Initialize a new labelItem
		text -- string: the text to be displayed
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
		# a label item is made of a label model, view and behaviour
		model = LabelItemModel(text, **kwargs)
		super(LabelItem, self).__init__(menuItemModel=model)
		logging.log(1, "Trace: LabelItem.__init__(%s, %s)" % (text, kwargs))
