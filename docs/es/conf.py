import sys
sys.path.insert(0, 'docs')

from conf import *    #Import everything from the common configuration file

#language set up
#Use the right code from https://docs.readthedocs.com/platform/latest/localization.html
language = 'es'

#Modify COLUMNS headers for any other language other than English
# Define the columns and their proportional widths for the table
# Format: (field_name, width, display_name)
# Note: pillar column removed as it will be shown as section headings
# Statement and guidance columns have equal width for balance
COLUMNS = [
    ("requirement_index", 4, "Ref SATRE"),
    ("capability", 12, "Capacidad"),
    ("statement", 38, "Declaración"),
    ("guidance", 38, "Guía"),
    ("importance", 8, "Importancia"),
]


#set paths to "_static" and "_templates"
# they are shared to avoid duplication
html_static_path = ['_static', '../_static']
templates_path = ['_templates', '.._templates']