from mycroft import MycroftSkill, intent_file_handler


class VirtualKeyboard(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('keyboard.virtual.intent')
    def handle_keyboard_virtual(self, message):
        self.speak_dialog('keyboard.virtual')


def create_skill():
    return VirtualKeyboard()

