from .base import *
import sys
import os


# SECRET_KEY is read from environment variable for security
SECRET_KEY = get_env_variable('SECRET_KEY')

# Debug must be off in production, ignore the environment variable
DEBUG = False

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS').split(",")

# Make links sent be HTTPS
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
# Paypal configuration
# To switch to the sandbox account, set PAYPAL_TEST = True
# and set PAYPAL_ACCOUNT to 'stephen-facilitator@triplecrownforheart.com'

PAYPAL_TEST = read_boolean(os.environ.get('PAYPAL_TEST', "TRUE").upper())
PAYPAL_ACCOUNT = os.getenv('PAYPAL_ACCOUNT')

BUSINESS_NAME = os.getenv("BUSINESS_NAME")
CURRENCY_CODE = os.getenv("CURRENCY_CODE")

