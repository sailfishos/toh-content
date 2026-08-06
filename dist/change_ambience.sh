#!/bin/sh
# SPDX-FileCopyrightText: 2026 Jolla Mobile Ltd
#
# SPDX-License-Identifier: BSD-3-Clause
#
# Set ambience unless disabled by user

if [ x"$(dconf read /desktop/jolla/theme/activate_on_toh)" != x"false" ]
then
    exec dbus-send --print-reply \
        --session --dest=com.jolla.ambienced /com/jolla/ambienced \
        com.jolla.ambienced.setAmbience "string:$1" > /dev/null
fi
