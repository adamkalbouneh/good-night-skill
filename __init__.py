from mycroft import MycroftSkill, intent_file_handler


class GoodNight(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('night.good.intent')
    def handle_night_good(self, message):
        self.speak_dialog('night.good')


def create_skill():
    return GoodNight()

