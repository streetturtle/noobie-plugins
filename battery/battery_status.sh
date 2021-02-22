#! /usr/bin/sh

CAPACITY=$(cat /sys/class/power_supply/BAT0/capacity)
STATUS=$(cat /sys/class/power_supply/BAT0/status)

if [ "$STATUS" = "Charging" ]; then
    ICON="battery-charging"
else
    ICON="battery"
fi

echo "{ \"widget\": { \"icon_path\": \"$ICON\", \"text\": \"$CAPACITY\"}}"