import pandas as pd
import json
# df = pd.read_json('input/MH1.json', encoding='utf-8')
with open('input/MH1.json', encoding='utf-8') as infile:
    data = json.load(infile)
df = pd.DataFrame(data['cards'])
df = df[['number','name','manaCost','types','subtypes','text','power','toughness',
    'rarity','colorIdentity','convertedManaCost','loyalty']]
df['number'] = df['number'].astype('int')
df = df.sort_values('number')
df.to_excel('input/raw_MH_file.xlsx')
