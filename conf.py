# -*- coding: utf8 -*-

import logging

conf = {
	'name': 'Shootzemup',
	'state': 'DEBUG',
	'game_engine': {
		'update_time_step': 0.02,
		'simulate_hardware_lag': 0
	},
	'logging': {
		'log_file_level': 0,  #logging.DEBUG
		'log_console_level': 0  #logging.DEBUG
	},
	'graphx': {
		'screen_size': (1000, 1000),
		'screen_base_color': (0, 0, 0),
		'video_player': {
			'max_fps': 60
		},
		'font': 'None'
	},
	'resources': {
		'intro_video': 'resources/intro.mpg',
		'font': {
			'default': None,
			'default_size': 16
		},
		'menu': {
			'default_menu_item': 'resources/menu/default_menu_item.png',
			'default_container': 'resources/menu/default_container.png',
			'default_label_background': 'resources/menu/default_label_background.png'
		},
		'language': 'fr'
	}
}