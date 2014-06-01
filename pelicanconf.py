#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Asif Imran'
SITENAME = u'Asif Imran'
SITEURL = 'http://aimran.github.io'
TIMEZONE = 'America/Los_Angeles'
AVATAR = '/theme/images/selfie.png'
TITLE = 'Asif Imran: Dreaming in Data'

PATH = 'content'
OUTPUT_PATH = 'output'

THEME = '../moonlake'
SUMMARY_MAX_LENGTH = 50

ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'

AUTHOR_SAVE_AS = False
CATEGORY_SAVE_AS = False

TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}.html'

DIRECT_TEMPLATES = ('blog', 'archives', 'tags')
PAGINATED_DIRECT_TEMPLATES = ('blog',)

CODE_DIR = 'code'
NOTEBOOK_DIR = 'notebooks'
EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')

#PLUGIN_PATH = '../pelican-plugins'
PLUGIN_PATH = '/Users/aimran/Code/misc/python/site/pelican-plugins'
PLUGINS = ['liquid_tags.img','liquid_tags.notebook',
            'liquid_tags.video', 'liquid_tags.include_code']



# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Github', 'http://github.com/aimran', 'fa-github'),
        ('Twitter', 'http://twitter.com/5sigma', 'fa-twitter'),
        ('LinkedIn', 'http://www.linkedin.com/pub/asif-imran/60/523/6a1',
            'fa-linkedin'))

# DEFAULTS
DEFAULT_LANG = 'en'
DEFAULT_CATEGORY = 'misc'
DEFAULT_DATE = 'fs'
DEFAULT_DATE_FORMAT = '%d %b %Y'
DEFAULT_PAGINATION = False

STATIC_PATHS = ['images', 'pdfs', 'code', 'notebooks', 'extra']


DISQUS_SITENAME = 'ailogs'
GOOGLE_ANALYTICS = "UA-47351804-1"
DOMAIN = "aimran.github.io"

# Twitter Cards
TWITTER_CARDS = True
TWITTER_NAME = "5sigma"

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False

