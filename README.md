# AI Personal Trainer

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

1. Clone the Repository:

bash
git clone https://github.com/yourusername/ai-personal-trainer.git

cd ai-personal-trainer

2. Install Dependencies:

bash
pip install -r requirements.txt

Key dependencies include: Gradio, Requests, Pillow, ReportLab, OpenAI, python-dotenv, fpdf.

3. Set Up API Keys:

Add your GIPHY and Hugging Face API keys in the respective files or via environment variables.

4. Run the Application:

bash

python main.py

Usage

Input your details (age, weight, height, gender, goal, injuries, available equipment, days/week, session time).

View your personalized plan with detailed exercises, sets, reps, GIF demos, and AI-generated images.

Download your plan as a PDF for offline use.

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

