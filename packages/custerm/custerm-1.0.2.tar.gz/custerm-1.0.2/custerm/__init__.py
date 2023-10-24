from requests import get
from .terminal import *
from .log import *
from .ansi import *

__title__: str = 'custerm'
__author__: str = 'cxstles'
__version__: str = '1.0.2'

VERSION: str = get('https://pypi.org/pypi/custerm/json').json()['info']['version']
if VERSION != __version__:
    Terminal.print(
        '**custerm** | New Version | pip install -U custerm',
        markdown=True
    )
