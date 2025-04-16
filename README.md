# AI_Personal_Trainer

AI Personal Trainer – README
Welcome to AI Personal Trainer, an AI-powered application that generates personalized workout plans, complete with GIF demonstrations, AI-generated visuals, and downloadable PDFs. This project leverages Gradio for an intuitive user interface and integrates several AI and data-driven components to deliver a holistic fitness planning experience.

Features
Personalized Workout Plans: Tailored routines based on user inputs (age, weight, height, gender, goals, injuries, equipment, days per week, and session time).

Dynamic Exercise Selection: Adapts workouts for specific needs (e.g., injury-safe routines).

Visual Demonstrations: Each exercise includes a GIF demo and an AI-generated image for clear guidance.

Downloadable PDF: Instantly generate and download a PDF version of your workout plan.

User-Friendly Interface: Built with Gradio for easy web-based interaction.

Customizable Equipment & Goals: Supports various equipment and fitness objectives.

Demo
Launch the app locally or on a supported platform. Enter your details, and receive a detailed, day-by-day workout plan with media and PDF export.

Installation
Clone the Repository:

bash
git clone https://github.com/yourusername/ai-personal-trainer.git
cd ai-personal-trainer
Install Dependencies:

bash
pip install -r requirements.txt
Key dependencies include: Gradio, Requests, Pillow, ReportLab, OpenAI, python-dotenv, fpdf.

Set Up API Keys:

Add your GIPHY and Hugging Face API keys in the respective files or via environment variables.

Run the Application:

bash
python main.py
Usage
Input your details (age, weight, height, gender, goal, injuries, available equipment, days/week, session time).

View your personalized plan with detailed exercises, sets, reps, GIF demos, and AI-generated images.

Download your plan as a PDF for offline use.

Project Structure
File/Folder	Purpose
main.py	Gradio interface and app entry point
workout_logic.py	Core logic for generating workout plans
pdf_exporter.py	PDF generation utility
models.py	Data models for user input and workout plans
data.py	Exercise database
gif_fetcher.py	Fetches exercise GIFs from GIPHY
sd_generator.py	Generates exercise images using Stable Diffusion
requirements.txt	Python dependencies
Example Output
📅 Day 1:

Jumping Jacks (5 sets of 15-20)
Demo: [GIF Link]

Push-ups (3 sets of 10-12)
Demo: [GIF Link]

Plank (4 sets of 12-15)
Demo: [GIF Link]

(PDF includes similar details with images)

Contributing
Fork the repo and create your branch.

Commit your changes.

Open a pull request describing your modifications.

License
Distributed under the MIT License.

Acknowledgments
Gradio for the UI framework.

GIPHY for exercise GIFs.

Hugging Face for AI image generation.

For more details, see the code comments and documentation in each module.

