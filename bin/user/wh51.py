## The ecowitt WH51 reports moisture as a percentage
##

import weewx
import weewx.units
from weewx.wxengine import StdService

import weeutil.logger
import logging
log = logging.getLogger(__name__)

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
        weewx.units.obs_group_dict['soilMoist9'] = 'group_percent'
        weewx.units.obs_group_dict['soilMoist10'] = 'group_percent'
        
        weewx.units.obs_group_dict['soilBatteryVoltage1'] = 'group_volt'
        weewx.units.obs_group_dict['soilBatteryVoltage2'] = 'group_volt'
        weewx.units.obs_group_dict['soilBatteryVoltage3'] = 'group_volt'
        weewx.units.obs_group_dict['soilBatteryVoltage4'] = 'group_volt'
        weewx.units.obs_group_dict['soilBatteryVoltage5'] = 'group_volt'
        weewx.units.obs_group_dict['soilBatteryVoltage6'] = 'group_volt'
        weewx.units.obs_group_dict['soilBatteryVoltage7'] = 'group_volt'
        weewx.units.obs_group_dict['soilBatteryVoltage8'] = 'group_volt'
        weewx.units.obs_group_dict['soilBatteryVoltage9'] = 'group_volt'
        weewx.units.obs_group_dict['soilBatteryVoltage10'] = 'group_volt'

        log.debug("Setup WH51 obs_group_dict")
