class Card():
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
    def update(self, **kwargs):
        self.__dict__.update(kwargs)

class Pool():
    def __init__(self, **kwargs):
        # grab 90 cards, sampled by rarity
        # 6 rares (1 in 8 chance replaced by mythic)
        # 18 uncommons
        # 


class Deck():
    def __init__(self, **kwargs):
        pass
