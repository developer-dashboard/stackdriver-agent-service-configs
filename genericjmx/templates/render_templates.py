#!/usr/bin/python

import jinja2
import os.path
import sys

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(sys.argv[0]) or "."),
    trim_blocks=True,
    lstrip_blocks=True,
    extensions=['jinja2.ext.do'])

print env.get_template(sys.argv[1]).render()
