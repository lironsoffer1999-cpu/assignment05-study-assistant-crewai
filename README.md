# Study Assistant Crew

A specialized CrewAI multi-agent system designed to help students master academic topics through automated summarization, assessment generation, and quality control.

## 🚀 Overview
The Study Assistant Crew automates the creation of study materials. By providing a topic, the crew orchestrates a sequential process where information is synthesized into a summary, transformed into a quiz, and rigorously reviewed for accuracy.

## 🤖 The Crew
The system employs 4 distinct agents:
1.  **Study Manager**: The conductor of the crew. Oversees the workflow and ensures the final product meets high standards.
2.  **Summary Specialist**: An expert in educational synthesis. Breaks down complex topics into digestible, structured summaries.
3.  **Quiz Creator**: A pedagogical expert who designs challenging practice questions to reinforce learning.
4.  **Quality Reviewer**: A meticulous editor who checks for factual accuracy, clarity, and educational effectiveness.

## 🛠️ Key Features
- **Sequential Execution**: Tasks are performed in a logical order to maintain context.
- **Managed Workflow**: Uses a Manager agent to coordinate efforts.
- **Verbose Tracking**: Real-time insights into agent "thoughts" and actions.
- **Standardized Output**: Generates structured Markdown files for easy reading.

## 📋 Requirements & Provider
- **Provider**: Google Gemini API
- **Model**: `gemini/gemini-2.5-flash-lite`
- **API Key**: `GOOGLE_API_KEY`
- **Language**: Python 3.10+
- **Framework**: CrewAI

## 🏗️ Installation & Setup
1. Clone the repository.
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure your `.env` file:
   ```env
   GOOGLE_API_KEY=your_api_key_here
   CREWAI_DISABLE_TELEMETRY=true
   ```

## 🏁 How to Run
Execute the main script from the root directory. The system will prompt you for a study topic and perform the full agentic workflow powered by Google Gemini:
```bash
python src/main.py
```

## 🎓 Grading Checklist Compliance
- [x] At least 4 chained agents.
- [x] Manager agent included.
- [x] Sequential process implemented.
- [x] Full role/goal/backstory definitions.
- [x] `verbose=True` for full transparency.
- [x] Single terminal execution.
- [x] Documented organizational structure.

## Proof of Run

The project was executed from the terminal using:

python src/main.py

Example input:

AI

Generated output:

output/ai_guide.md

Run logs:

logs/

Execution screenshot:

screenshots/run_proof.png