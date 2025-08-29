# weewx-ws90

This is a weewx extension to enable data provided by the Ecowitt ws90 to be imported into WeeWx.

## Design decisions
* Underlying data to be stored unambiguously. This means extending the schema wview_extended.py, creating a new superset wview_extended_ws90.py
* Bundle attached ecowitt devices into the same ws90 extension, since the data is provided by the ws90 and this aligns with adding to the same schema.
* Where there are different device groups, these are found in different bin/user files for convenience
* naming to align to both weewx and ws90. For example, piezo rain is "rainPiezo" (analagous to standard "rain")
* include configuration settings in the extension

The intent is to retain the ws90 piezo rain as a separate data set from rain and allow additional soil sensors (WH51) which are available through the ecowitt reporting platform

Currently, this does not update the weewx database or extend the database schema.

*Currently in TEST*

This should be used in conjunction with an appropriate input driver or service, such as weewx-interceptor ([Fork to support the Ecowitt]( https://github.com/erudita/weewx-interceptor)) or better still, https://github.com/bellrichm/WeeWX-MQTTSubscribe

## WH51:
* additional soil sensors (10 in total), e.g. soilMoist5, soilMoist6, .. all having 'group_percent'
* new - soilBatteryVoltage? (10 in total), e.g. soilBatteryVoltage3 having "group_volt"

## WS90piezo:
* rainPiezo
* rainPiezoRate
