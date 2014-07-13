# -*- coding: utf8 -*-

from menuItemView import MenuItemView


class ContainerView(MenuItemView):
	"""
	View of the container
	"""

	def render(self, interpolation):
		super(ContainerView, self).render(interpolation)
		# successively render all the children elements
		for item in self._model.menuItems:
			item.render(interpolation)
