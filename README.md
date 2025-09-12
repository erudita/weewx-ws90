# weewx-ws90

This is a set of weews configurations to enable data provided by the Ecowitt ws90 to be imported into WeeWx.
THis is based on using MQTT Subscribe as the weewx driver.

## Constraints
* adding observation types for new sensors effectivly prohits use of extensions to define the types since the weewx driver will always be invoked prior to the extension.
* This needs to work as a Docker container.
* Data captured via the WeeWX-MQTTSubscribe from a GW2000 using ecowitt protocol.
* Must be compatible with non-US database (hence observation types are important)
* Maximise backwards compatibility by reusing database fields if appropriate.
* To use MQTT only, https://github.com/bellrichm/WeeWX-MQTTSubscribe, and https://github.com/matthewwall/weewx-mqtt
* Capture and recored from two rain devices separately (WS90 and WH40)

## How this works
* bin/user/extensions.py - modified to include all of the new observations delivered by GGW2000 from WS90/WH51
* MQTTSubscribe configured to present the observations, which are then copied, extracted and readyed for archive by
* transformations defined using [StdCalibrate] and [Accumulator] sections of weewx.conf
* All observations are presented to MQTT Service for publication
  
* Database hail fields are resued for piezo rain. 

*Currently in TEST*

## WH51:
* additional soil sensors (10 in total), e.g. soilMoist5, soilMoist6, .. all being 'group_percent'
* new - soilBatteryVoltage? (10 in total), e.g. soilBatteryVoltage3 having "group_volt"
* all of the above added to database definitions

## WS90piezo:
piezo rain is is captured as rainPiezo by using the yrain_piezo field from WS2000 GW. This is cumulative yearly rain.
various piezo rain fields are captured and defined (e.g. rainPiezo24, event rain, piezo rain rate) generally corresponding to analogue equivalent.
Transformations are defined using [StdCalibrate] and [Accumulator] sections of weewx.conf
