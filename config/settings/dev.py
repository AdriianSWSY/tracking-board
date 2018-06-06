import os
from .base import *

DEBUG = True

SHOW_DOCS = True

INSTALLED_APPS += (
    'debug_toolbar',
    'drf_yasg'
)

MIDDLEWARE += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'core.profiling.ProfilingMiddleware',
)

DEBUG_TOOLBAR_PANEL = [
    'template_timings_panel.panels.TemplateTimings.TemplateTimings',
]

# MailTrap settings: 
EMAIL_HOST = 'smtp.mailtrap.io'
EMAIL_PORT = '2525'
EMAIL_HOST_USER = os.getenv('MAILTRAP_EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('MAILTRAP_EMAIL_HOST_PASSWORD')