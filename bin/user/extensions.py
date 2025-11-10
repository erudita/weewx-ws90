import weewx.units
# units not delivered by the GW2000
# typical weewx.conf sections are
# [Accumulator]
#    [[rainPiezo]] 
#        extractor = sum
#    [[irrigationVolume1]] 
#        extractor = sum
#    [[irrigationVolume2]]
#        extractor = sum

# for the WFC01 (irrigation).
# I include here for convenience
weewx.units.obs_group_dict['irrigationVolume1'] = 'group_volume'
weewx.units.obs_group_dict['irrigationVolume2'] = 'group_volume'

# units delivered by the GW2000

# for the WS90 (all-in-1)

# Voltages are reported, so ...
# option 1 was to change groups of existing measure, e.g.
#    change rainBatteryStatus to group_volt
# option 2 create new measures, e.g.
#    rainPiezeoBattery - group_volt
## weewx.units.obs_group_dict['rainPiezoBatteryVoltage'] = 'group_volt'
## weewx.units.obs_group_dict['rainBatteryVoltage'] = 'group_volt'
# chosen to use option 1 and change labels in weewx.conf

# This configuration sets "piezo" types, which are used in the loop 
# for clarity.
# they are assigned to database types for archive records in the 
# [StdCalibrate] [[Corrections]] section

weewx.units.obs_group_dict['rainPiezo'] = 'group_rain'
weewx.units.obs_group_dict['rainPiezoRate'] = 'group_rainrate'
weewx.units.obs_group_dict['eventRain'] = 'group_rain'
weewx.units.obs_group_dict['eventRainPiezo'] = 'group_rain'

# some addons to be used in the loop and MQTT generation but not database
# without these, the unit conversion will fail
weewx.units.obs_group_dict['rain24'] = 'group_rain'
weewx.units.obs_group_dict['rainPiezo24'] = 'group_rain'
weewx.units.obs_group_dict['monthRainPiezo'] = 'group_rain'
weewx.units.obs_group_dict['dayRainPiezo'] = 'group_rain'

# WS 90 gives options for wind direction.
weewx.units.obs_group_dict['windDirAvg10m'] = 'group_direction'
weewx.units.obs_group_dict['windDirInstant'] = 'group_direction'

# WS 90 provides summary fields
weewx.units.obs_group_dict['windGustMax'] = 'group_speed'

# for the WH51 (soil moisture)
weewx.units.obs_group_dict['soilMoist1']		= 'group_percent'
weewx.units.obs_group_dict['soilMoist2']		= 'group_percent'
weewx.units.obs_group_dict['soilMoist3']		= 'group_percent'
weewx.units.obs_group_dict['soilMoist4']		= 'group_percent'
weewx.units.obs_group_dict['soilMoist5']		= 'group_percent'
weewx.units.obs_group_dict['soilMoist6']		= 'group_percent'
weewx.units.obs_group_dict['soilMoist7']		= 'group_percent'
weewx.units.obs_group_dict['soilMoist8']		= 'group_percent'
weewx.units.obs_group_dict['soilMoist9']		= 'group_percent'
weewx.units.obs_group_dict['soilMoist10']		= 'group_percent'
weewx.units.obs_group_dict['soilBatteryVoltage1']	= 'group_volt'
weewx.units.obs_group_dict['soilBatteryVoltage2']	= 'group_volt'
weewx.units.obs_group_dict['soilBatteryVoltage3']	= 'group_volt'
weewx.units.obs_group_dict['soilBatteryVoltage4']	= 'group_volt'
weewx.units.obs_group_dict['soilBatteryVoltage5']	= 'group_volt'
weewx.units.obs_group_dict['soilBatteryVoltage6']	= 'group_volt'
weewx.units.obs_group_dict['soilBatteryVoltage7']	= 'group_volt'
weewx.units.obs_group_dict['soilBatteryVoltage8']	= 'group_volt'
weewx.units.obs_group_dict['soilBatteryVoltage9']	= 'group_volt'
weewx.units.obs_group_dict['soilBatteryVoltage10']	= 'group_volt'

