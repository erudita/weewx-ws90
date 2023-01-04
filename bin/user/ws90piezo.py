import schemas.wview_extended
import weewx.units

schema_with_ws90 = schemas.wview.schema_extended + [('rainPiezo', 'REAL')]
schema_with_ws90 = schemas.wview.schema_extended + [('rainPiezoRate', 'REAL')]

weewx.units.obs_group_dict['rainPiezoRate'] = 'group_rainrate'
weewx.units.obs_group_dict['rainPiezo'] = 'group_rain'
