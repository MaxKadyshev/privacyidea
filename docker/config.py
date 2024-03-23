# The realm, where users are allowed to login as administrators
SUPERUSER_REALM = ['super', 'administrators']
# Your database
SQLALCHEMY_DATABASE_URI = 'sqlite:////privacyidea/data-dev.sqlite'
# Set maximum identifier length to 128
# SQLALCHEMY_ENGINE_OPTIONS = {"max_identifier_length": 128}
# This is used to encrypt the auth_token
SECRET_KEY = 'password'
# This is used to encrypt the admin passwords
PI_PEPPER = "Never know..."
# This is used to encrypt the token data and token passwords
PI_ENCFILE = '/privacyidea/tests/testdata/enckey'
# This is used to sign the audit log
PI_AUDIT_KEY_PRIVATE = '/privacyidea/tests/testdata/private.pem'
PI_AUDIT_KEY_PUBLIC = '/privacyidea/public.pem'
# PI_AUDIT_MODULE = <python audit module>
# PI_AUDIT_SQL_URI = <special audit log DB uri>
# Options passed to the Audit DB engine (supersedes SQLALCHEMY_ENGINE_OPTIONS)
# PI_AUDIT_SQL_OPTIONS = {}
# Truncate Audit entries to fit into DB columns
PI_AUDIT_SQL_TRUNCATE = True
# PI_LOGFILE = '....'
# PI_LOGLEVEL = 20
# PI_INIT_CHECK_HOOK = 'your.module.function'
# PI_CSS = '/location/of/theme.css'
# PI_UI_DEACTIVATED = True
