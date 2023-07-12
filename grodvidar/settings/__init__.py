from .base import *

if env('ENVIRONMENT') == 'prod':
    from .prod import *
else:
    from .dev import *
