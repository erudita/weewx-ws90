# weewx-ws90

This is a set of weews configurations to enable data provided by the Ecowitt ws90 to be imported into WeeWx.
THis is based on using MQTT Subscribe as the weewx driver.

## Design decisions
* adding observation types for new sensors effective prohits use of extensions, since the driver will always be invoked first.
* Hence, this set of configurations is based upon bin/user/extensions.py
* This needs to work as a Docker container.
* Underlying new data to be stored unambiguously. This means extending the schema wview_extended.py for database initialisation
* Reuse hail for piezo rain. 

*Currently in TEST*

This should be used in conjunction with an appropriate input driver or service, such as https://github.com/bellrichm/WeeWX-MQTTSubscribe

## WH51:
* additional soil sensors (10 in total), e.g. soilMoist5, soilMoist6, .. all having 'group_percent'
* new - soilBatteryVoltage? (10 in total), e.g. soilBatteryVoltage3 having "group_volt"

## WS90piezo:
* rainPiezo mapped to hail
* rainPiezoRate hailRate
