from crate.theme.rtd.conf import *

project = "CrateDB Enterprise Edition"
html_title = project

url_path = "docs/crate/enterprise"
html_baseurl = "https://cratedb.com/%s/" % url_path

exclude_patterns += ["_build", "Thumbs.db", ".DS_Store", "_external"]

extensions = ['myst_parser']
source_suffix = ['.rst', '.md']
