class Human:
    def __init__(self, value):
        self.value = value

    def output(self):
        print('Hello! I\'m {}!'.format(self.value))


h = Human("Pei")
h.output()


# extends
class NewType:
    def say(self):
        print("見える！")


class NewTypeHuman(NewType):

    # オーバーライド
    def output(self):
        super().output()


n = NewTypeHuman()
n.say()
