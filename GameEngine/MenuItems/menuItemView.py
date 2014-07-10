# -*- coding: utf8 -*-

import logging

from Graphx import graphx


class MenuItemView(object):
	"""
    View of the menu item. It handles the drawing of a menu item
	"""
	def __init__(self, model):
		super(MenuItemView, self).__init__()
		self._model = model


	def render(self, interpolation):
		logging.log(1, "Trace: MenuItemView.render(%.5f)" % 
					(interpolation))
		logging.debug("Rendering using model: %s" % self._model)
		graphx.draw(self._model.surface, self._model.rect)



