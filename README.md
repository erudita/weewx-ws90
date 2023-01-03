# weewx-ws90-soil

This is a weewx extension to enable features of the Ecowitt ws90 to be imported into WeeWx

The intent is to retain the ws90 piezo rain as a separate data set from rain.

Also, use the additional soil sensors

## Extend "wview_extended", adding 
* 4 soil sensors (8 in total) soilMoist5, soilMoist6, ..
* rainPiezo (like rain, using the piezo sensor)
* rainPiezoRate (like rainRate, using the piezo sensor)

## Change units:
* SoilMoist to 'group_percent'

