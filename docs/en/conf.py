import sys
sys.path.insert(0, 'docs')

from conf import *    #Import everything from the common configuration file

#language set up
language = 'en'

#DO NOT modify column headers for English

#set paths to "_static" and "_templates"
# they are shared to avoid duplication
html_static_path = ['_static', '../_static']
templates_path = ['_templates', '.._templates']