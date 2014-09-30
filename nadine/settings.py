# Django settings for django_apps project.
import os
import sys

from datetime import timedelta

ROOT = os.path.dirname(os.path.abspath(__file__))
path = lambda *a: os.path.join(ROOT, *a)

TEMPLATE_DIRS = ( path('../templates/'), )
MEDIA_ROOT = path('../media/')

BACKUP_ROOT = path('../backups/')
BACKUP_COUNT = 30

STATIC_URL = '/static/'
STATICFILES_DIRS = ( 'static', )
STATICFILES_FINDERS = (
	'django.contrib.staticfiles.finders.FileSystemFinder',
	'django.contrib.staticfiles.finders.AppDirectoriesFinder',
	'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

DEBUG = False

# -- Message of the Day --
# Displayed on the iPad after sign-in
MOTD="Enjoy your day at Office Nomads!"
MOTD_TIMEOUT=5000

# Local time zone for this installation. Choices can be found here:
# http://www.postgresql.org/docs/8.1/static/datetime-keywords.html#DATETIME-TIMEZONE-SET-TABLE
# although not all variations may be possible on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Los_Angeles'
USE_TZ = True

# Language code for this installation. All choices can be found here:
# http://www.w3.org/TR/REC-html40/struct/dirlang.html#langcodes
# http://blogs.law.harvard.edu/tech/stories/storyReader$15
LANGUAGE_CODE = 'en-us'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# URL that handles the media served from MEDIA_ROOT.
# Example: "http://media.lawrence.com"
MEDIA_URL = '/media/'

# Arp Watch data directory
ARP_ROOT = path('../arp_import/')
ARP_IMPORT_LOG = ARP_ROOT + 'import.log'
ARP_IMPORT_LOCK = ARP_ROOT + 'importing.lock'
ARP_IP_PFX = '172.16.5.'

# URL that handles login
LOGIN_URL='/login/'

SITE_ID = 1

# Auth Backends
AUTHENTICATION_BACKENDS = (
	'nadine.backends.EmailOrUsernameModelBackend',
	'django.contrib.auth.backends.ModelBackend'
)

TEMPLATE_CONTEXT_PROCESSORS = (
	"django.contrib.auth.context_processors.auth",
	"django.core.context_processors.debug",
	"django.core.context_processors.i18n",
	"django.core.context_processors.media",
	"django.core.context_processors.static",
	"django.core.context_processors.request",
	"django.contrib.messages.context_processors.messages",
	"context_processors.site",
	"context_processors.nav_context",
)

MIDDLEWARE_CLASSES = (
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'urls'

INSTALLED_APPS = (
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.admin',
	'django.contrib.humanize',
	'django.contrib.staticfiles',
	'taggit_templatetags',
	'taggit',
	'djcelery',
	'staff',
	'members',
	'interlink',
	'arpwatch',
	'tablet',
	#'gather',
	#'debug_toolbar',
)

#
# Celery initialization
#
try:
   import djcelery
   djcelery.setup_loader()
except ImportError:
   pass

# USAePay Settings
USA_EPAY_URL='www.usaepay.com'
USA_EPAY_KEY='ABCDEFG'
USA_EPAY_KEY2='ABCDEFG'
USA_EPAY_PIN2='1234'
USA_EPAY_URL_KEY='ABCDEFG'

CELERYBEAT_SCHEDULER = "djcelery.schedulers.DatabaseScheduler"
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json', 'msgpack', 'yaml']
CELERY_DISABLE_RATE_LIMITS = True
CELERY_RESULT_BACKEND = "amqp"
BROKER_URL = "amqp://guest:guest@localhost:5672//"
CELERY_TIMEZONE = 'America/Los_Angeles'

# When this is True, celery tasks will be run synchronously.
# This is nice when running unit tests or in development.
# In production set this to False in your local_settings.py
CELERY_ALWAYS_EAGER = False

#MAILCHIMP_API_KEY="YourMailchimpKey"
#MAILCHIMP_NEWSLETTER_KEY="YourNewsletter"
MAILCHIMP_WEBHOOK_KEY="nadine"

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

# Logging
LOGGING = {
	'version': 1,
	'disable_existing_loggers': False,
	'formatters': {
		'verbose': {
			'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
			'datefmt' : "%d/%b/%Y %H:%M:%S"
		  },
		  'simple': {
				'format': '%(levelname)s %(message)s'
		  },
	 },
	'handlers': {
		'file': {
			'level': 'DEBUG',
			'class': 'logging.FileHandler',
			'filename': path('../django.log'),
			'formatter': 'verbose',
		},
		'mail_admins': {
			'level': 'ERROR',
			'class': 'django.utils.log.AdminEmailHandler',
			'include_html': True,
			'formatter': 'verbose',
		}
	},
	'loggers': {
		'django': {
			'handlers': ['file'],
			'level': 'INFO',
			'propagate': True,
		},
		'django.request': {
			'handlers': ['file', 'mail_admins'],
			'level': 'INFO',
			'propagate': True,
		},
		'staff': {
			'handlers': ['file'],
			'level': 'INFO',
		},
		'arpwatch': {
			'handlers': ['file'],
			'level': 'INFO',
		},
	},
}

# Import the local settings file
from local_settings import *

# Copyright 2009 Office Nomads LLC (http://www.officenomads.com/) Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
