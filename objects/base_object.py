class BaseObject:

    def __init__(
        self,
        x,
        y,
        color="black"
    ):

        self.x = x
        self.y = y

        self.color = color

        self.selected = False

    def contains(self, x, y):

        return False