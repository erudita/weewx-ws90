# installer for the weewx-ws90 soil additions
# Distributed under the terms of the GNU Public License (GPLv3)

import configobj
from weecfg.extension import ExtensionInstaller

try:
    # Python 3
    from io import StringIO
except ImportError:
    # Python 2
    from StringIO import StringIO
    
# WeeWX imports
import weewx

from setup import ExtensionInstaller

REQUIRED_VERSION = "4.5.0"


# define our config as a multiline string so we can preserve comments
ws90_config = u"""

[Accumulator]
    [[rainPiezo]]
        extractor = sum

"""
# obtain our config string as a configobj dict
ws90_dict = configobj.ConfigObj(StringIO(ws90_config))

def loader():
    return WSInstaller()

class WSInstaller(ExtensionInstaller):
    def __init__(self):
        super(WSInstaller, self).__init__(
            version="0.1.6",
            name='ws90',
            config=ws90_dict,
            description='schema updates for ws90 and wh51 soil sensors',
            author="Erudita",
            author_email="erudita<@>ankubis.com",
            process_services='user.wh51.WH51',
            files=[('bin/user', ['bin/user/ws90piezo.py',
                                 'bin/user/wh51.py'])
                  ]
            )
