from datetime import date
import os
import sys


sys.path.append(os.path.abspath('../zhatil'))

project = 'zhatil'
author = 'Mike Canoy'
copyright = str(date.today().year) + ', ' + author
release = '0.0.1'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon'
]
source_suffix = '.rst'
master_doc = 'index'

pygments_style = 'sphinx'
html_theme = 'alabaster'
html_theme_options = {
    'description': 'A chat bot framework.'
}
