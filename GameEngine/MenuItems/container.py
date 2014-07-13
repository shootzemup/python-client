# -*- coding: utf8 -*-

import logging
from menuItem import MenuItem
from conf import conf
from Graphx import graphx

from containerBehaviour import ContainerBehaviour
from containerView import ContainerView
from containerModel import ContainerModel


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
		logging.log(1, "Trace: Container.__init__(%s, %s)" 
						% (image, kwargs))
		model = ContainerModel(image=image, **kwargs)
		behaviour = ContainerBehaviour(model)
		view = ContainerView(model)
		super(Container, self).__init__(menuItemModel=model,
			menuItemView=view, menuItemBehaviour=behaviour)

	def addMenuItem(self, item):
		"""
		Add a menu item to this container.
		item -- either a MenuItem or a list of MenuItems
		"""
		self._model.addMenuItem(item)


	def computeSize(self, parentPos=None, parentSize=None):
		"""
		Override the MenuItem computeSize function to make
		parentPos and parentSize facultative, as a container can be the 
		root of the menuItem tree
		"""
		self._behaviour.computeSize(parentPos, parentSize)