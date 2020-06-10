from mycroft import MycroftSkill, intent_file_handler


class RadiocohostTrollbot(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('trollbot.radiocohost.intent')
    def handle_trollbot_radiocohost(self, message):
        self.speak_dialog('trollbot.radiocohost')


def create_skill():
    return RadiocohostTrollbot()

