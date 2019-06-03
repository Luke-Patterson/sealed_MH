import pandas as pd
import numpy as np
class Set():
    def __init__(self, df_path):
        self.df = pd.read_excel(df_path)

class Card():
    def __init__(self, attrib_dict):
        self.__dict__.update(attrib_dict)

    def update_attrib(self, attrib_dict):
        self.__dict__.update(attrib_dict)

    def update_score(self):
        pass

class Pool():
    def __init__(self, Set):
        self.Set = Set
        df = pd.DataFrame()
        # grab 90 cards from set, sampled by rarity
        # 6 rares (1 in 8 chance replaced by mythic)
        mythics = np.random.binomial(n=6,p=.125)
        df = df.append(self.Set.df.loc[self.Set.df['rarity']=='rare',:]
            .sample(6-mythics, replace=True))
        df = df.append(self.Set.df.loc[self.Set.df['rarity']=='mythic',:]
            .sample(mythics, replace=True))
        # 18 uncommons
        df = df.append(self.Set.df.loc[self.Set.df['rarity']=='uncommon',:]
            .sample(18, replace=True))
        # 60 commons
        df = df.append(self.Set.df.loc[self.Set.df['rarity']=='uncommon',:]
            .sample(60, replace=True))
        # 6 basic snow-lands
        df = df.append(self.Set.df.loc[self.Set.df['rarity']=='basic',:]
            .sample(6, replace=True))

        self.df = df

class Deck():
    def __init__(self):
        self.df = pd.DataFrame()
