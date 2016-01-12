# Copy this file into secrets.py and set keys, secrets and scopes.

# This is a session secret key used by webapp2 framework.
# Get 'a random and long string' from here:
# http://clsc.net/tools/random-string-generator.php
# or execute this from a python shell: import os; os.urandom(64)
SESSION_KEY = "KDC24B9812CF6D2E49F52F231B26DA"

# Google APIs
GOOGLE_APP_ID = '1004465040441-fqc6jnrv6jrptkfeqaemu1p2qtmgnn7n.apps.googleusercontent.com'
GOOGLE_APP_SECRET = '2txwX26SiEl6XhgxH_deWQUA'

# Facebook auth apis
FACEBOOK_APP_ID = '136505660058729'
FACEBOOK_APP_SECRET = 'bf59bea42c64e5d0ce7ad8cdf32d0fbe'


# https://dev.twitter.com/apps
TWITTER_CONSUMER_KEY = 'Oi4c3LkPXqWCDxkaTBzekd06H'
TWITTER_CONSUMER_SECRET = 'uvhMukOwtgjjiinCYXCboyi7AsmCIYuPQnPglf2lUi7CfihyO4'


# config that summarizes the above
AUTH_CONFIG = {
  # OAuth 2.0 providers

  'googleplus': (GOOGLE_APP_ID, GOOGLE_APP_SECRET, 'profile email'),
  'facebook': (FACEBOOK_APP_ID, FACEBOOK_APP_SECRET, 'email,user_about_me,public_profile'),

  # OAuth 1.0 providers don't have scopes
  'twitter': (TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET),
  # OpenID doesn't need any key/secret
}

AUTH_OPTIONAL_PARAMS = {
  #	Provider auth init optional parameters
  # '<provider>': {'<parameter_name>': '<value>'}
  # ex. 'twitter' : {'force_login': True}
}
