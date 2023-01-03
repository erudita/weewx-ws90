# weewx-ws90-soil

This is a weewx extension to enable features of the Ecowitt ws90 to be imported into WeeWx

The intent is to use the ws90 piezo rain as a separate data set from rain.

Also, use the additional soil sensors

Define a new schema which extends wview_extended, adding 
* 4 soil sensors (8 in total)
* rainPiezo (like rain, using the piezo sensor)
* rainPiezoRate (like rainRate, using the piezo sensor)

Change units:
* SoilMoist to 'group_percent'


* change of unit for soil moisture to percentage (%)
