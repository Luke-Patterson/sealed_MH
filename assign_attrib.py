# assign additional attributes to cards
import pandas as pd
df = pd.read_excel('input/raw_MH_file_rankings.xlsx')

# clean up text
df['text'] = df.text.str.lower()
df['text'] = df['text'].str.replace('\n',' ')

# common condition statements
def IsName(str):
    return df['name'] == str
IsCreature = df['types'].apply(lambda x: 'Creature' in x)
def TextContains(str):
    return(df['text'].str.contains(str))

# creatures, or spells that are effectively creatures
df['creature_like'] = False
df.loc[IsCreature, 'creature_like'] = True

# evasive creatures (0-1 scale)
df['evasive'] = 0
df.loc[IsCreature & TextContains('menace'), 'evasive'] = .5
df.loc[IsCreature & TextContains('flying'), 'evasive'] = 1
df.loc[IsCreature & TextContains("can't be blocked"), 'evasive'] = 1

# manual modifications of attributes specific to MH cards
# creatures that conditionally gain flying get evasive .5
df.loc[IsName('Chillerpillar'),'evasive'] = .5
df.loc[IsName('Bogardan Dragonheart'),'evasive'] = .5
