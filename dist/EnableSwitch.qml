// SPDX-FileCopyrightText: 2026 Jolla Mobile Ltd
//
// SPDX-License-Identifier: BSD-3-Clause

import QtQuick 2.6
import Sailfish.Silica 1.0
import Nemo.DBus 2.0
import com.jolla.settings 1.0

SettingsToggle {
    id: root

    //: The name of the other half, so this should be just 'Inari Blue' in most languages.
    //% "Inari Blue"
    name: qsTrId("jolla-toh-configs-la-inari_blue")
    icon.source: "image://theme/icon-m-jolla"
    onToggled: toh.toggle()
    checked: false

    DBusInterface {
        id: toh

        bus: DBus.SessionBus
        service: "org.freedesktop.systemd1"
        iface: "org.freedesktop.systemd1.Manager"
        path: "/org/freedesktop/systemd1"

        signalsEnabled: true

        function update() {
            call('GetUnitFileState', "toh-leds.service", function(state) {
                root.checked = state != "masked"
            })
        }

        function toggle() {
            if (root.checked) {
                // To turn off, stop service and mask unit
                call('StopUnit', ['toh-leds.service', 'replace'], function(reply) {
                    typedCall('MaskUnitFiles', [
                        {'type': 'as', 'value': ['toh-leds.service']},
                        {'type': 'b', 'value': false},
                        {'type': 'b', 'value': false},
                    ])
                })
            } else {
                // To turn on, unmask unit and start service
                typedCall('UnmaskUnitFiles', [
                    { 'type': 'as', 'value': ['toh-leds.service'] },
                    { 'type': 'b', 'value': false }
                ], function(reply) {
                    call('StartUnit', ['toh-leds.service', 'replace'])
                })
            }
        }

        function subscribe() {
            call('Subscribe', undefined)
        }

        function unitFilesChanged() {
            // This is not very efficient but there doesn't seem to be a better way in systemd's interface
            update()
        }

        Component.onCompleted: {
            subscribe()
            update()
        }
    }
}
