import gradio as gr
from models import UserInput
from workout_logic import generate_workout
from pdf_exporter import create_pdf

def gradio_interface(age, weight, height, gender, goal, injury, equipment, days, session_time):
    user = UserInput(
        age=int(age),
        weight=float(weight),
        height=float(height),
        gender=gender,
        goal=goal,
        injury=injury,
        equipment=equipment.split(","),
        days_per_week=int(days),
        session_time=int(session_time)
    )
    plan = generate_workout(user)
    output = ""
    for day in plan:
        output += f"\n\n📅 Day {day.day}:\n"
        for ex in day.exercises:
            output += f"- {ex.name} ({ex.sets} sets of {ex.reps})\n  Demo: {ex.demo}\n"
    pdf_file = create_pdf(plan)
    return output, pdf_file

iface = gr.Interface(
    fn=gradio_interface,
    inputs=[
        gr.Number(label="Age"),
        gr.Number(label="Weight (kg)"),
        gr.Number(label="Height (cm)"),
        gr.Dropdown(["Male", "Female", "Other"], label="Gender"),
        gr.Dropdown(["Weight Loss", "Muscle Gain", "Endurance", "Rehab"], label="Goal"),
        gr.Textbox(label="Injuries (optional)"),
        gr.Textbox(label="Available Equipment (comma-separated)"),
        gr.Slider(1, 7, step=1, label="Days per Week"),
        gr.Slider(15, 90, step=5, label="Session Time (minutes)")
    ],
    outputs=["text", "file"],
    title="AI Personal Trainer",
    description="Personalized workout plans with GIFs, AI-generated visuals, and downloadable PDFs."
)

iface.launch(share=True)
