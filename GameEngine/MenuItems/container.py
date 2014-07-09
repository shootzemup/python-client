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
	def __init__(self, imageLink=None, **kwargs):
		"""
		Initialize the container
		**kwargs -- arguments given the the menuItem constructor
		"""
		# default the imageLink parameter
		if imageLink is None:
			imageLink = conf['resources']['menu']['default_container']
		super(Container, self).__init__(imageLink=imageLink, **kwargs)
		self._menuItems = []
		logging.log(1, "Trace: Container.__init__(%s, %s)" 
						% (imageLink, kwargs))

	def addMenuItem(self, item):
		self._menuItems.append(item)

	def update(self, stateManager):
		logging.log(1, "Trace: Container.update(...)")
		# call mother class updating function
		MenuItem.update(self, stateManager)
		# successively update all the children items
		for item in self._menuItems:
			item.update(stateManager)

	def render(self, interpolation, parentPos=None, parentSize=None):
		logging.log(1, "Trace: Container.render(%.5f, %s, %s)" 
						% (interpolation, parentPos, parentSize))

		# the first container of the tree has the screen as a parent
		if parentSize is None:
			parentSize = graphx.getScreenSize()
		if parentPos is None:
			parentPos = (graphx.getScreenSize()[0] / 2, 
						 graphx.getScreenSize()[1] / 2)
		# call mother class rendering function
		MenuItem.render(self, interpolation, parentPos, parentSize)
		# successively render all the children elements
		for item in self._menuItems:
			item.render(interpolation, self._model.realPosition,
						self._model.realSize)


