from pydantic import BaseModel
from datetime import date

class TrainingSpec(BaseModel):
    start_date: date | None = None
    end_date: date | None = None
    stocks: list | None = None
    p_value_threshold: float | None = 0.001
    

