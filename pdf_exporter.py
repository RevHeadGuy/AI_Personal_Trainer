from fpdf import FPDF
import os

class PDFWorkout(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "AI Personal Trainer Workout Plan", ln=True, align="C")

    def add_day(self, day, exercises):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, f"Day {day}", ln=True)
        for ex in exercises:
            self.set_font("Arial", "", 12)
            self.multi_cell(0, 10, f"{ex.name} - {ex.sets} sets of {ex.reps}")
            if ex.image and os.path.exists(ex.image):
                self.image(ex.image, w=50)
        self.ln(5)

def create_pdf(plan, filename="workout_plan.pdf"):
    pdf = PDFWorkout()
    pdf.add_page()
    for day_plan in plan:
        pdf.add_day(day_plan.day, day_plan.exercises)
    pdf.output(filename)
    return filename
