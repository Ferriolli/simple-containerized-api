import random

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    id: int
    name: str


@app.get('/')
def read_root():
    return {'hello': 'world'}


@app.get('/v1/item')
def get_item(name: str):
    return name


@app.post('/v1/new_item')
def new_item(item: Item):
    return f'Successfully inserted item with id: {item.id} and name: {item.name}'


@app.get('/v1/random')
def get_random_num():
    return random.randint(1, 100)
