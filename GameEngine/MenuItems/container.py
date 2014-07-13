# -*- coding: utf8 -*-

import logging
from menuItem import MenuItem
from conf import conf
from Graphx import graphx


class Container(MenuItem):
	"""
	Represent any container of the menu. All the sizes of the menu items it
	contains will be computed from a percentage of its  size
	"""
	def __init__(self, image=None, **kwargs):
		"""
		Initialize the container
		**kwargs -- arguments given the the menuItem constructor
		"""
		# default the image parameter
		if image is None:
			image = conf['resources']['menu']['default_container']
		super(Container, self).__init__(image=image, **kwargs)
		self._menuItems = []
		logging.log(1, "Trace: Container.__init__(%s, %s)" 
						% (image, kwargs))

	def addMenuItem(self, item):
		"""
		Add a menu item to this container.
		item -- either a MenuItem or a list of MenuItems
		"""
		if type(item) is list:
			self._menuItems += item
		else:
			self._menuItems.append(item)

	def computeSize(self, parentPos=None, parentSize=None):
		# the first container of the tree has the screen as a parent
		if parentSize is None:
			parentSize = graphx.getScreenSize()
		if parentPos is None:
			parentPos = (graphx.getScreenSize()[0] / 2, 
						 graphx.getScreenSize()[1] / 2)

		MenuItem.computeSize(self, parentPos, parentSize)
		for item in self._menuItems:
			item.computeSize(self._model.realPosition, self._model.realSize)

	def update(self, stateManager):
		# call mother class updating function
		MenuItem.update(self, stateManager)
		# successively update all the children items
		for item in self._menuItems:
			item.update(stateManager)

	def render(self, interpolation):
		# call mother class rendering function
		MenuItem.render(self, interpolation)
		# successively render all the children elements
		for item in self._menuItems:
			item.render(interpolation)


