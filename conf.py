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
		'log_file_level': logging.INFO,
		'log_console_level': 0
	},
	'graphx': {
		'screen_size': (1280, 800),
		'screen_base_color': (0, 0, 0),
		'video_player': {
			'max_fps': 60
		},
		'font': 'None'
	},
	'events': {
		'key_repeat_delay': 200,
		'key_repeat_interval': 1
	},
	'resources': {
		'intro_video': 'resources/intro.mpg',
		'font': {
			'default': 'resources/font/amaranth/Amaranth-Regular.ttf',
			'system': 'bitstreamverasans',
			'use_system': True,
			'default_precision': 32
		},
		'menu': {
			'default_menu_item': 'resources/menu/default_menu_item.png',
			'default_container': 'resources/menu/default_container.png',
			'default_label_background': 'resources/menu/default_label_background.png',
			'input': {
				'default_background': 'resources/menu/input/default_background.png',
				'focused_default_background': 'resources/menu/input/focused_default_background.png',
				'margins': (5, 2),  # x, y
			}
		
		},
		'language': 'fr'
	}
}