# -*- coding: utf8 -*-

import logging

import pygame

from conf import conf
from menuItemModel import MenuItemModel


class ContainerModel(MenuItemModel):
	"""Represents the model of a basic container"""
	def __init__(self, image=None, **kwargs):
		"""
		Initialize the model
		**kwargs -- arguments given the the menuItemModel constructor
		"""
		# defaults
		if image is None:
			image = conf['resources']['menu']['default_container']
		super(ContainerModel, self).__init__(image=image, **kwargs)

		self._menuItems = []
		self._focusedItem = -1

	def get_menuItem(self, index):
	    return self._menuItems[index]
	def set_menuItem(self, index, value):
	    self._menuItems[index] = value

	@property
	def menuItems(self):
	    return self._menuItems

	@property
	def focusedItem(self):
	    return self._focusedItem
	@focusedItem.setter
	def focusedItem(self, value):
	    self._focusedItem = value
	

	def addMenuItem(self, item):
		"""
		Add a menu item to this container.
		item -- either a MenuItem or a list of MenuItems
		"""
		if type(item) is list:
			self._menuItems += item
		else:
			self._menuItems.append(item)
		# if no item is focused, focus the first focusable
		if self._focusedItem == -1:
			for i, item in enumerate(self.menuItems):
				if item.focus():
					self._focusedItem = i
					break