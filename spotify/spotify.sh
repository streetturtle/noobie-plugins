#! /usr/bin/sh

ARTIST=$(sp metadata | grep 'artist|' | cut -d '|' -f 2)
TITLE=$(sp metadata | grep 'title|' | cut -d '|' -f 2)
STATUS=$(sp status)

if [ "$STATUS" = "Playing" ]; then
    ICON="play"
else
    ICON="pause"
fi

echo "{ \"widget\": { \"icon\": \"$ICON\", \"text\": \"$ARTIST - $TITLE\", \"mouse_actions\": { \"on_scroll_up\": \"sp next\", \"on_scroll_down\": \"sp prev\", \"on_left_click\": \"sp play\" }}}"
