# weewx-ws90

Docker version of Weewx with some small additions to support:
* Weewx Driver MQTTSubscribe - https://github.com/bellrichm/WeeWX-MQTTSubscribe
* MQTT output using MQTT https://github.com/matthewwall/weewx-mqtt
* additions to bin/user/extensions to support Ecowitt: WH40, WS90, and WH51 through the ecowitt gateway (e.g. GW2000)
* Capture and recored from two rain devices separately (WS90 and WH40)

## How this works
* bin/user/extensions.py - modified to include most of the new observations delivered by GW2000 from WS90/WH51
* MQTTSubscribe configured to ingest the observations (weewx.conf)
* MQTT configured to present the observations (weewx.conf)

### Maximise backwards compatibility by reusing database fields where possible
* Database hail fields are resued for piezo rain.
* New definitions for soil percentage (supports the WH51)
* Database voltage fields reused for WS90 battery and capacitor voltage, and WH40 battery voltage

*Currently in TEST*
