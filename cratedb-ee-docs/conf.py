from crate.theme.rtd.conf.cratedb_ee import *

# Disable version chooser.
html_context.update({
    "display_version": False,
    "current_version": None,
    "versions": [],
})

exclude_patterns += ["_build", "Thumbs.db", ".DS_Store"]

source_suffix = ['.rst', '.md']

linkcheck_ignore = [
    # Example link only, not meant to exist
    "http://iss_hostname:8080/api/v2/meta/jwk/",
    # 403 for non-browser clients (bot protection)
    "https://www.ibm.com/docs/",
]


linkcheck_timeout = 5
