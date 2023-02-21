

class Noob:

    def __init__(self, noob = True):
        self.is_noob = noob

    def print_noob(self):

        if self.is_noob:
            print("I am a noob.")

if __name__ == '__main__':
    nub = Noob()
    nub.print_noob()
