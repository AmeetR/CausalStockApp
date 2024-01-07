#~/CausalGraph/app/main.py


from fastapi import FastAPI
from app.training_spec import TrainingSpec


app = FastAPI()


@app.get('/')
async def index():
    return {"Real": "Python"}

@app.post('/train/')
async def train(training_spec: TrainingSpec):
    """
    Trains the CausalGraph with existing historical data on hand. 
    """
    pass