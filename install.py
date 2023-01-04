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
            version="0.1.3",
            name='ws90',
            description='schema updates for ws90 soil',
            author="Erudita",
            files=[('bin/user', ['bin/user/ws90soil.py'])],
            config=ws90_dict
            )
