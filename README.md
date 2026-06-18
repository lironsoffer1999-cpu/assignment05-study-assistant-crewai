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
## Agent Contributions

The project uses four specialized CrewAI agents that work together in a sequential workflow:

* **Study Manager** – defines the structure and scope of the study guide.
* **Summary Specialist** – creates a structured academic summary of the topic.
* **Quiz Creator** – generates practice questions and answers based on the summary.
* **Quality Reviewer** – performs a final review and combines all outputs into a cohesive study guide.

This separation of responsibilities demonstrates how multiple AI agents can collaborate to produce higher-quality educational content.

## Challenges and Fixes

During development, the main challenge was integrating CrewAI with Google Gemini. Temporary API issues such as rate limits and service availability errors (429 and 503 responses) were encountered during testing.

The project code itself remained functional throughout the process. Once API availability was restored, the workflow executed successfully and generated the final study guide output.

## Model Choice

The project uses Google Gemini through CrewAI with the model:

`gemini/gemini-2.5-flash-lite`

This model was selected because it provides a good balance between response quality, execution speed, and accessibility for educational workflows.

It is well suited for generating study summaries, practice questions, and reviewed learning materials within a multi-agent architecture.
