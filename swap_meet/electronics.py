from .item import Item

class Electronics(Item):

    def __init__(self, condition=0):
        super().__init__("Electronics", condition)
        # self.category = "Electronics"
        # self.condition = condition

    def __str__(self):
        return "A gadget full of buttons and secrets."

