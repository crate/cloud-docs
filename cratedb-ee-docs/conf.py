from crate.theme.rtd.conf import *

# Disable version chooser.
html_context.update({
    "display_version": False,
    "current_version": None,
    "versions": [],
})

project = "CrateDB Enterprise Edition"
html_title = project

url_path = "docs/crate/enterprise"
html_baseurl = "https://cratedb.com/%s/" % url_path

exclude_patterns += ["_build", "Thumbs.db", ".DS_Store"]

source_suffix = ['.rst', '.md']

linkcheck_ignore = [
    # Example link only, not meant to exist
    "http://iss_hostname:8080/api/v2/meta/jwk/",
    # 403 for non-browser clients (bot protection)
    "https://www.ibm.com/docs/",
]


linkcheck_timeout = 5
