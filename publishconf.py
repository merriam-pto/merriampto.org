#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

AUTHOR = u'Merriam PTO'
SITENAME = u'Merriam PTO'
TIMEZONE = 'EST'

SITEURL = 'http://merriam-pto.github.io'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
# Blogroll
LINKS = (('Merriam School', 'http://merriam.abschools.org/'),
        ('Acton-Boxborough School Distric', 'http://abschools.org/'),
        ('PowerSchool Portal', 'https://absis.ab.mec.edu/public/home.html'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/merriampto'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
STATIC_PATHS = ['static', 'files']
