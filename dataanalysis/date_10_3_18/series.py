import pandas as pd
import numpy as np

df = pd.DataFrame({'food': ['bacon', 'pulled pork', 'bacon','Pastrami', 'corned beef', 'Bacon','pastrami', 'honey ham', 'nova lox'],
'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})

meat_to_animal = {
                    'bacon': 'pig',
                    'pulled pork': 'pig',
                    'pastrami': 'cow',
                    'corned beef': 'cow',
                    'honey ham': 'pig',
                    'nova lox': 'salmon'
                    }


df['animal'] = df.food.str.lower().map(meat_to_animal)

print(df[df.animal == 'cow'][['ounces','food']])



print(df)

'''df = df.drop(df[df.animal == 'pig'].index)
df[df.animal == 'cow']='goat'
print(df)'''