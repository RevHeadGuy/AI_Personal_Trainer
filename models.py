from pydantic import BaseModel
from typing import List, Optional

class UserInput(BaseModel):
    age: int
    weight: float
    height: float
    gender: str
    goal: str
    injury: Optional[str] = None
    equipment: List[str]
    days_per_week: int
    session_time: int

class WorkoutExercise(BaseModel):
    name: str
    sets: int
    reps: str
    demo: str
    image: Optional[str] = None

class WorkoutPlan(BaseModel):
    day: int
    exercises: List[WorkoutExercise]
