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

## 📋 Requirements
- Python 3.10+
- CrewAI
- Google Gemini API Key

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
   ```

## 🏁 How to Run
Execute the main script from the root directory:
```bash
python src/main.py
```

## ⚙️ Execution Modes
The system automatically detects your configuration and chooses the appropriate mode:

- **Real CrewAI Mode**: Active when a valid `GOOGLE_API_KEY` is provided in the `.env` file. This mode uses live LLM agents (Gemini 2.0 Flash) to research and generate content.
- **Local Demo Fallback Mode**: Active when no API key is found. This mode safely simulates the four-agent workflow and generates a demo study guide to demonstrate the system structure without consuming API credits.

## 🎓 Grading Checklist Compliance
- [x] At least 4 chained agents.
- [x] Manager agent included.
- [x] Sequential process implemented.
- [x] Full role/goal/backstory definitions.
- [x] `verbose=True` for full transparency.
- [x] Single terminal execution.
- [x] Documented organizational structure.
