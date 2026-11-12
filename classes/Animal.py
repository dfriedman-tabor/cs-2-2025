
class Animal:

    def __init__(self, type, sound, dangerLevel):
        self.sound = sound
        self.dangerLevel = dangerLevel
        self.type = type

    def __str__(self):
        return "I am a " + self.type

    def speak(self):
        print(self.sound)





