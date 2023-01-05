# weewx-ws90

This is a weewx extension to enable features of the Ecowitt ws90 to be imported into WeeWx

The intent is to retain the ws90 piezo rain as a separate data set from rain and allow additional soil sensors (WH51) which are available through the ecowitt reporting platform

Currently, this does not update the weewx database or extend the database schema.

*Note that rainPiezo and rainPiezoRate are not tested - I use hail and hailRate*

## WH51:
* Set SoilMoist? to 'group_percent'
* 4 additional soil sensors (8 in total) soilMoist5, soilMoist6, ..

## Change schema units:

* rainPiezo (like rain, using the piezo sensor)
* rainPiezoRate (like rainRate, using the piezo sensor)
