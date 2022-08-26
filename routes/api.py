
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
    genColor = lambda x:f'rgb({randint(0, 255)}, {randint(0, 255)}, {randint(0, 255)},0.5)'
    quantity = lambda sex:len(df[df['sex'] == sex])
    sex = ['male','female']
    return {'sex':sex,'quantity':[quantity(s) for s in sex],'colors':[genColor(i) for i in range(3)]}



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

@router.get('/man-woman-child')
def get_man_woman_child():
    genColor = lambda x:f'rgb({randint(0, 255)}, {randint(0, 255)}, {randint(0, 255)},0.5)'
    quantity = lambda who:len(df[df['who'] == who])
    who = ['man','woman','child']
    return {'person':who,'quantity':[quantity(w) for w in who],'colors':[genColor(i) for i in range(3)]}