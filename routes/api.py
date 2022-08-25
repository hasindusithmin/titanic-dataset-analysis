
from fastapi import APIRouter
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


