import PySimpleGUI as sg

# Add your new theme colors and settings
sg.LOOK_AND_FEEL_TABLE['MyCreatedTheme'] = {'BACKGROUND': '# 000066',
										'TEXT': '# FFCC66',
										'INPUT': '# 339966',
										'TEXT_INPUT': '# 000000',
										'SCROLL': '# 99CC99',
										'BUTTON': ('# 003333', '# FFCC66'),
										'PROGRESS': ('# D1826B', '# CC8019'),
										'BORDER': 1, 'SLIDER_DEPTH': 0,
'PROGRESS_DEPTH': 0, }

# Switch to use your newly created theme
sg.theme('MyCreatedTheme')

# Call a popup to show what the theme looks like
sg.popup_get_text('This how the MyNewTheme is created')	
