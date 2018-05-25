#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = 'Francesc Arpí Roca'
SITENAME = 'Maria Dolors'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'ca'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Facebook', 'https://www.facebook.com/mariadolorslloret/'),
          ('Instagram', 'https://www.instagram.com/mariadolorslloret/'),
          ('Youtube', 'https://www.youtube.com/channel/UCReh9lLc9peY9hJSuNQoJnw'))

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = './theme'

PLUGIN_PATHS = ['plugins', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'plugins')]
PLUGINS = ['tables', 'letters']
GOOGLE_ANALYTICS = 'UA-119906115-1'
