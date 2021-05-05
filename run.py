"""
Michael Patel
May 2021

Project description:

File description:

"""
################################################################################
# Imports


################################################################################
# Player object
class Player:
    def __init__(self, position="Guard"):
        self._position = position

    # ----- Position ----- #
    @property  # using property decorator
    # getter
    def position(self):
        return self._position

    # setter
    @position.setter
    def position(self, p):
        self._position = p

    # deleter
    @position.deleter
    def position(self):
        del self._position


################################################################################
# Main
if __name__ == "__main__":
    me = Player()
    print(me.position)  # get
    me.position = "Forward"  # set
    print(me.position)
