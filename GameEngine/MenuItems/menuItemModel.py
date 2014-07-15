# -*- coding: utf8 -*-

import logging
import pygame

from conf import conf


class MenuItemModel(object):
	"""
        Handle the data of a default menu item
	"""
	def __init__(self, image=None, initPos=None, initSize=None, 
				 absolutePos=False, absoluteSize=False, itemName="Unamed"):
		"""
		Initialize the model of the menu item
		image -- if string, the link to the image to be used as background for this 
				     menu item, otherwise a Surface object is expected
		initPos -- the initial position of the item
		initSize -- the initial size of the item.
		absolutePos -- If set to `True`, the position will be used 
					   as stated. If False, the position will be
					   computed from the size the parent
		absoluteSize -- If set to `True`, the the size will be used 
					   as stated. If False, the size will be
					   computed from the size the parent
		name -- the name of the menu item
		"""
		super(MenuItemModel, self).__init__()
		logging.log(1, "Trace: MenuItemModel.__init__(%s, %s, %s, %s, %s)"
						% (image, initPos, initSize, absolutePos, itemName))
		# dynamically default the parameters
		if image is None or len(image) == 0:
			image = conf['resources']['menu']['default_menu_item']
		if initPos is None:
			initPos = (0, 0)

		# load the images
		if type(image) is not list:
			image = [image]

		self._surfaces = []
		for img in image:
			if type(img) is str:
				self._surfaces.append(pygame.image.load(img))
			else:
				self._surfaces.append(img)
		self._currentSurface = 0

		if initSize is None:
			if absoluteSize:
				initSize = self.surface.get_rect().size
			else:
				initSize = (1, 1)

		self._hasFocus = False
		self._focusable = True
		self._position = initPos
		self._size = initSize
		self._absolutePos = absolutePos
		self._absoluteSize = absoluteSize
		self._itemName = itemName
		self._rect = self.surface.get_rect()

	@property
	def itemName(self):
	    return self._itemName
	@itemName.setter
	def itemName(self, value):
	    self._itemName = value


	@property
	def focusable(self):
	    return self._focusable
	@focusable.setter
	def focusable(self, value):
	    self._focusable = value
	
	@property
	def hasFocus(self):
	    return self._hasFocus
	
	def focus(self):
		"""
		Mark the item as focused. This happens when the user click on the item.
		Returns true if the item is focused, false if the item is not focusabled
		(ex: LabelMenuItems are not focusable)
		"""
		logging.debug("MenuItem %s - focus" % self.itemName)
		if self._focusable:
			self._hasFocus = True
			return True
		return False
		
	def unfocus(self):
		logging.debug("MenuItem %s - unfocus" % self.itemName)
		self._hasFocus = False


	@property
	def position(self):
	    return self._position
	@position.setter
	def position(self, value):
	    self._position = value

	@property
	def size(self):
	    return self._size
	@size.setter
	def size(self, value):
	    self._size = value

	@property
	def absolutePos(self):
	    return self._absolutePos
	@property
	def absoluteSize(self):
	    return self._absoluteSize
	

	# if the menu position is not absolutePos, realPosition will
	# contain the real position in pixel the item uses on the scren.
	# note that this property is not valid before the first
	@property
	def realPosition(self):
	    return self._rect.center
	@realPosition.setter
	def realPosition(self, value):
	    self._rect.center = value

	@property
	def realPositionTopLeft(self):
	    return self._rect.topleft
	@realPositionTopLeft.setter
	def realPositionTopLeft(self, value):
	    self._rect.topleft = value
	

	@property
	def realSize(self):
		return self._rect.size
	@realSize.setter
	def realSize(self, value):
		self._rect.size = value

	def intersect(self, point):
		return self._rect.collidepoint(point)
	

	@property
	def rect(self):
	    return self._rect

	# returns the current used surface
	@property
	def surface(self):
	    return self._surfaces[self._currentSurface]
	@surface.setter
	def surface(self, value):
	    self._surfaces[self._currentSurface] = value
	    self._rect = self.surface.get_rect()
	    if self._absoluteSize:
	    	self.size = self._rect.size

	# this will resize all the surfaces of item to keep always the same size
	def resizeSurface(self, newSize):
		logging.debug("MenuItem %s: resizing surface to %s" 
						% (self._itemName, newSize))
		for i, surf in enumerate(self._surfaces):
			self._surfaces[i] = pygame.transform.scale(surf, newSize)

	# change the current used surface
	def useSurface(self, sid):
		if sid < 0 or sid >= len(self._surfaces):
			logging.warning("Cannot use surface #%d. Only %d surfaces available"
							% (sid, len(self._surfaces)))
			sid = 0
		self._currentSurface = sid
