import os

LOGGING = {
    'version': 1,
    'loggers': {
        'py': {
            'handlers': ['file', ],
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': os.path.join('C:', 'Users', 'Infocar', 'source', 'repos', 'VeiculoDataHarvest', 'logs', 'logs.log'),
            'formatter': 'simpleRe',
        },
    },
    'formatters': {
        'simpleRe': {
            'format': '{levelname} {asctime} {message}',
            'style': '{',
        }
    }
}
