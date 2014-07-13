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
			
	@property
	def menuItem(self, index):
	    return self._menuItems[index]
	@menuItem.setter
	def menuItem(self, index, value):
	    self._menuItems[index] = value

	@property
	def menuItems(self):
	    return self._menuItems

	def addMenuItem(self, item):
		"""
		Add a menu item to this container.
		item -- either a MenuItem or a list of MenuItems
		"""
		if type(item) is list:
			self._menuItems += item
		else:
			self._menuItems.append(item)
