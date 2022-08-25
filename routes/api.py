
from fastapi import APIRouter
from os import getcwd
import pandas as pd
####################################

# Create `df` DataFrame 
df = pd.read_csv(f'{getcwd()}/titanic.csv')

router = APIRouter(
    prefix='/api',
    tags=['Api']
)

@router.get('/')
def root():
    return "Hello World"




