#!/usr/bin/env bash
CURR_WID=$(xdotool getwindowfocus);
CHROME_WID=$(xdotool search --name '#e11aeca0e7e00447b2d72d96cd55c32b4273ad29f1f2b48ae73d692475825979');
if [[ ${CHROME_WID} ]]
then
   xdotool windowactivate ${CHROME_WID};
   xdotool key 'ctrl+r';
   xdotool windowactivate ${CURR_WID};
fi