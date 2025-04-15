import random
from models import UserInput, WorkoutPlan, WorkoutExercise
from data import exercise_db
from gif_fetcher import fetch_gif_url
from sd_generator import generate_image

def generate_workout(user: UserInput) -> list[WorkoutPlan]:
    plan = []
    if user.injury and "knee" in user.injury.lower():
        available = exercise_db["knee_safe"]
    else:
        available = exercise_db["full_body"]

    for day in range(1, user.days_per_week + 1):
        daily = random.sample(available, min(3, len(available)))
        exercises = []
        for ex in daily:
            name = ex["name"]
            gif = fetch_gif_url(name)
            img = generate_image(f"{name}, fitness demonstration, clean background")
            exercises.append(WorkoutExercise(
                name=name,
                sets=random.randint(3, 5),
                reps=random.choice(["10-12", "12-15", "15-20"]),
                demo=gif,
                image=img
            ))
        plan.append(WorkoutPlan(day=day, exercises=exercises))
    return plan
