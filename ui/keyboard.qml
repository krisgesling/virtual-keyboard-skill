import QtQuick 2.4
import QtQuick.Layouts 1.4
import QtQuick.Controls 2.3

import Mycroft 1.0 as Mycroft

Mycroft.ProportionalDelegate {
    id: root
    TextArea {
        id: textArea
        placeholderText: "Tap me to bring up the virtual keyboard"
    }
}
