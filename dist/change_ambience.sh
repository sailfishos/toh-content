#!/bin/sh
# Set ambience unless disabled by user

if [ x"$(dconf read /desktop/jolla/theme/activate_on_toh)" != x"false" ]
then
    exec dbus-send --print-reply \
        --session --dest=com.jolla.ambienced /com/jolla/ambienced \
        com.jolla.ambienced.setAmbience "string:$1" > /dev/null
fi
