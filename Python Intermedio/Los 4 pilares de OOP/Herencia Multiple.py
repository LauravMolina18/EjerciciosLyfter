#To understand the things i like relating them to the music i like, Coldplay is my favorite band
class Singer:

    def sing(self):
        print("Singing a Coldplay song.")


class Pianist:

    def play_piano(self):
        print("Playing the piano.")


class ChrisMartin(Singer, Pianist):

    def introduce(self):
        print("Hi, I'm Chris Martin.")


#Example

chris = ChrisMartin()

chris.introduce()
chris.sing()
chris.play_piano()