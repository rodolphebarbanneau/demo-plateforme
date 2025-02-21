"""
The application main entry point.

Note:
    You can also use the following syntax to define application settings:

    >>> app = Plateforme(
    ...    debug=True,
    ...    database_engines='plateforme.db',
    ...    namespaces=[
    ...        ...
    ...    ],
    ...    packages=[
    ...        ...
    ...    ],
    ...    logging={
    ...        ...
    ...    },
    ... )
"""

from plateforme import Plateforme


# Create application
app = Plateforme('server.settings')
