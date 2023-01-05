## The ecowitt WH51 reports moisture as a percentage
##

import weewx
import weewx.units
from weewx.wxengine import StdService

import weeutil.logger
import logging
log = logging.getLogger(__name__)

class WS90(StdService):
    """WeeWX service for initialising data for WH51 compatibility (soil moisture as a percentage """

    def __init__(self, engine, config_dict):
        # Initialize my superclass:
        super(WS90, self).__init__(engine, config_dict)

        weewx.units.obs_group_dict['rainPiezoRate'] = 'group_rainrate'
        weewx.units.obs_group_dict['rainPiezo'] = 'group_rain'
        
        log.debug("Setup WS90 obs_group_dict rainPiezo")
