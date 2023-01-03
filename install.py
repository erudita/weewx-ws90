# installer for the weewx-ws90 soil additions
# Distributed under the terms of the GNU Public License (GPLv3)

from weecfg.extension import ExtensionInstaller

# define our config as a multiline string so we can preserve comments
ws90_config = """

[Accumulator]
    [[rainPiezo]]
        extractor = sum

"""

ws90_dict = configobj.ConfigObj(StringIO(ws90_config))

def loader():
    return WS90Installer()

class WS90Installer(ExtensionInstaller):
    def __init__(self):
        super(WS90Installer, self).__init__(
            version="0.1.1",
            name='ws90',
            description='schema updates for ws90 soil',
            author="Erudita",
            files=[('bin/user', ['bin/user/ws90soil.py'])],
            config=ws90_dict
            )
