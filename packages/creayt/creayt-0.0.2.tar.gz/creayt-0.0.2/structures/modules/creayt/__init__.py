

'''
import creayt
creayt.text ("salutations")
'''

'''
plan:
creayt.config ()
'''

'''
	creayt.__init__.py: salutations
'''

import inspect
import os

def text (text):
	caller_path = os.path.abspath ((inspect.stack ()[1])[1])
	caller_path_split = caller_path.split ("/")
	caller_path_split_last_index = len (caller_path_split) - 1	
	caller_path_abbr = (
		caller_path_split [ caller_path_split_last_index - 1 ] + 
		"." + 
		caller_path_split [ caller_path_split_last_index ] +
		":"
	)
	
	
	print (caller_path_abbr + " " + text)
	

