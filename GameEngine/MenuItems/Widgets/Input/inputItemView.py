# -*- coding: utf8 -*-

import logging
import pygame
from pprint import pformat

from Graphx import graphx

from conf import conf
from GameEngine.MenuItems.menuItemView import MenuItemView


class InputItemView(MenuItemView):
	"""
	View of the input item. It draws the text on the current surface before 
	rendering it.
	"""

	def render(self, interpolation):
		logging.log(1, "Trace: MenuItemView.render(%.5f)" % 
					(interpolation))
		logging.debug("Rendering using model: %s" % self._model)
		super(InputItemView, self).render(interpolation)
		# position at the middle of the item, on the left
		pos = (
			self._model.realPosition[0] - self._model.realSize[0] / 2 + 5,
			self._model.realPosition[1] - self._model.textSurfaceSize[1] / 2
		)
		# The drawing area shows the 
		# the last part of the text if the textsurface in longer than the 
		# background surface
		if self._model.realSize[0] > self._model.textSurfaceSize[0]:
			clip_size = self._model.textSurfaceSize
			clip_pos = (0, 0)
		else:
			clip_size = (self._model.realSize[0] - 
				2 * conf['resources']['menu']['input']['margins'][0],
				self._model.realSize[1] - 
				2 * conf['resources']['menu']['input']['margins'][1])
			clip_pos = (self._model.textSurfaceSize[0] - clip_size[0],
				self._model.textSurfaceSize[1] - clip_size[1])

		graphx.draw(self._model.textSurface, pos, clip_pos, clip_size)
