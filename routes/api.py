
from fastapi import APIRouter,HTTPException
from os import getcwd
import pandas as pd
import numpy as np
from random import randint
####################################

# Create `df` DataFrame 
df = pd.read_csv(f'{getcwd()}/titanic.csv')

router = APIRouter(
    prefix='/api',
    tags=['Api']
)

@router.get('/gender')
def get_gender():
    return {'Male':len(df[df['sex'] == 'male']),'Female':len(df[df['sex'] == 'female'])}


@router.get('/age-range')
def get_age_ranges():
    genColor = lambda x:f'rgb({randint(0, 255)}, {randint(0, 255)}, {randint(0, 255)},0.5)'
    color = [genColor(i) for i in range(10)]
    ages = [f'{x}-{x+10}' for x in range(0,91,10)]
    freq = [0 for x in range(10)]
    for x in [int(age) for age in df.age.to_list() if not np.isnan(age)]:
        if 0 < x <= 10:
            freq[0] += 1
        if 10 < x <= 20:
            freq[1] += 1
        if 20 < x <= 30:
            freq[2] += 1
        if 30 < x <= 40:
            freq[3] += 1
        if 40 < x <= 50:
            freq[4] += 1
        if 50 < x <= 60:
            freq[5] += 1
        if 60 < x <= 70:
            freq[6] += 1
        if 70 < x <= 80:
            freq[7] += 1
        if 80 < x <= 90:
            freq[8] += 1
        if 90 < x <= 100:
            freq[9] += 1
    return {'Age':ages,'Freq':freq,'Color':color}

@router.get('/death-survive')
def get_death_servive():
    return {'survived':len(df[df['survived'] == 1]),'deathed':len(df[df['survived'] == 0])}

@router.get('/survive-gender')
def get_survive_gender_details():
    return {'male':len(df[(df['survived'] == 1) & (df['sex'] == 'male')]),'female':len(df[(df['survived'] == 1) & (df['sex'] == 'female')])}

@router.get('/death-gender')
def get_survive_gender_details():
    return {'male':len(df[(df['survived'] == 0) & (df['sex'] == 'male')]),'female':len(df[(df['survived'] == 0) & (df['sex'] == 'female')])}

@router.get('/survived-death-by-gender')
def get_survived_death_by_gender(gender:str,alive:bool):
    isalive = 1 if alive else 0
    genColor = lambda x:f'rgb({randint(0, 255)}, {randint(0, 255)}, {randint(0, 255)},0.5)'
    colors = [genColor(i) for i in range(5)]
    Ages =  df[(df['survived'] == isalive) & (df['sex'] == gender)]['age'].to_list()
    stages = ['child','teen','young','adult','senior']
    ages = [0 for i in range(5)]
    for age in Ages:
        if 0 < age <= 12:
            ages[0] += 1
        if 12 < age <= 19:
            ages[1] += 1
        if 19 < age <= 35:
            ages[2] += 1
        if 35 < age <= 60:
            ages[3] += 1
        if 60 < age:
            ages[4] += 1 
    return {
        'stages':stages,
        'ages':ages,
        'colors':colors
    }  

@router.get('/survive-or-death-by-class')
def get_survive_or_death_by_class(survive:bool = True):
    n = 1 if survive else 0
    quantity = lambda c:len(df[(df['survived'] == n) & (df['class'] == c)])
    return [quantity(class_) for class_ in ['First','Second','Third']] 

@router.get('/survive-or-death-by-deck')
def get_survive_or_death_by_deck(survive:bool = True):
    n = 1 if survive else 0
    quantity = lambda deck:len(df[(df['survived'] == n) & (df['deck'] == deck)])
    return [quantity(deck) for deck in ['A','B','C','D','E','F','G']]