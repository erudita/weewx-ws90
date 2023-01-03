import schemas.wview_extended
import weewx.units

schema_with_ws90 = schemas.wview.schema_extended + [('soilMoist5', 'REAL')]
schema_with_ws90 = schemas.wview.schema_extended + [('soilMoist6', 'REAL')]
schema_with_ws90 = schemas.wview.schema_extended + [('soilMoist7', 'REAL')]
schema_with_ws90 = schemas.wview.schema_extended + [('soilMoist8', 'REAL')]
schema_with_ws90 = schemas.wview.schema_extended + [('rainPiezo', 'REAL')]
schema_with_ws90 = schemas.wview.schema_extended + [('rainPiezoRate', 'REAL')]

weewx.units.obs_group_dict['soilMoist1'] = 'group_percent'
weewx.units.obs_group_dict['soilMoist2'] = 'group_percent'
weewx.units.obs_group_dict['soilMoist3'] = 'group_percent'
weewx.units.obs_group_dict['soilMoist4'] = 'group_percent'
weewx.units.obs_group_dict['soilMoist5'] = 'group_percent'
weewx.units.obs_group_dict['soilMoist6'] = 'group_percent'
weewx.units.obs_group_dict['soilMoist7'] = 'group_percent'
weewx.units.obs_group_dict['soilMoist8'] = 'group_percent'
