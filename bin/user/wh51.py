## The ecowitt WH51 reports moisture as a percentage
##

import weewx
import weewx.units
from weewx.wxengine import StdService

class WH51(StdService):
    """WeeWX service for initialising data for WH51 compatibility (soil moisture as a percentage """

    def __init__(self, engine, config_dict):
        # Initialize my superclass:
        super(WH51, self).__init__(engine, config_dict)

        
        weewx.units.obs_group_dict['soilMoist1'] = 'group_percent'
        weewx.units.obs_group_dict['soilMoist2'] = 'group_percent'
        weewx.units.obs_group_dict['soilMoist3'] = 'group_percent'
        weewx.units.obs_group_dict['soilMoist4'] = 'group_percent'
        weewx.units.obs_group_dict['soilMoist5'] = 'group_percent'
        weewx.units.obs_group_dict['soilMoist6'] = 'group_percent'
        weewx.units.obs_group_dict['soilMoist7'] = 'group_percent'
        weewx.units.obs_group_dict['soilMoist8'] = 'group_percent'
        

        loginf("Setup WH51 obs_group")
