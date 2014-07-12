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
		graphx.draw(self._model.surface, self._model.rect)



