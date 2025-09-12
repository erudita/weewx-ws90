#!/usr/bin/env sh

WEEWX_ROOT=/etc/weewx
WEEWX_CONF_DIST=$WEEWX_ROOT/weewx.conf
CONFIGURATION_MOUNTPOINT=/data
WEEWX_CONF_LIVE=$CONFIGURATION_MOUNTPOINT/etc/weewx.conf

if [ -f $WEEWX_CONF_LIVE ];
then
	echo "Using Live Configuration"
	WEEWX_CONF=$WEEWX_CONF_LIVE
else
	echo "Using Distribution Configuration"
	WEEWX_CONF=$WEEWX_CONF_DIST 
fi

if [ "$#" -ge 1 ] && [ "$1" = "--test" ];
then
	/bin/sh
        exit
else
	echo "num. args is $#"
fi

echo "WEEWX_CONF=$WEEWX_CONF"

while true; do
  weewxd $WEEWX_CONF > /dev/stdout
  sleep 60
done
