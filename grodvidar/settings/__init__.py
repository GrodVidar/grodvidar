from .base import *
import environ

env = environ.Env()
environ.Env.read_env()

if env('ENVIRONMENT') == 'prod':
    from .prod import *
else:
    from .dev import *
