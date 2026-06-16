import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM

# Load environment variables for API keys
load_dotenv()

def run_study_crew():
    print("=== Study Assistant Crew (Gemini Edition) ===")
    print("Note: This system requires Google Gemini API configured via environment variables.")
    print("Ensure GOOGLE_API_KEY is set in your .env file or environment.\n")
    
    topic = input("Enter the academic topic you'd like to study: ")

    # Initialize Gemini LLM
    # Using gemini-2.5-flash-lite for speed and reliability
    google_api_key = os.getenv("GOOGLE_API_KEY")
    os.environ["GOOGLE_API_KEY"] = google_api_key
    os.environ["GEMINI_API_KEY"] = google_api_key

    llm = LLM(
        model="gemini/gemini-2.5-flash-lite",
        api_key=google_api_key
    )

    # 1. Study Manager — coordinates the workflow.
    study_manager = Agent(
        role='Study Manager',
        goal=f'Coordinate the creation of a comprehensive study guide for {topic}.',
        backstory=(
            "You are a seasoned educational project manager. Your job is to define the "
            "structure of the study guide and ensure all specialists are working towards "
            "a cohesive educational goal. You oversee the entire process."
        ),
        verbose=True,
        allow_delegation=True,
        llm=llm,
        tools=[]
    )

    # 2. Summary Specialist — creates a structured topic summary.
    summary_specialist = Agent(
        role='Summary Specialist',
        goal=f'Create a structured and detailed summary of {topic}.',
        backstory=(
            "You are an academic researcher with a talent for synthesizing complex information. "
            "You focus on clarity, accuracy, and highlighting the most important concepts "
            "for a student to master."
        ),
        verbose=True,
        allow_delegation=False,
        llm=llm,
        tools=[]
    )

    # 3. Quiz Creator — creates practice questions.
    quiz_creator = Agent(
        role='Quiz Creator',
        goal=f'Create practice questions based on the topic summary of {topic}.',
        backstory=(
            "You are an expert in pedagogical assessment. You design questions that "
            "challenge students and reinforce their learning, ranging from basic recall "
            "to critical thinking."
        ),
        verbose=True,
        allow_delegation=False,
        llm=llm,
        tools=[]
    )

    # 4. Quality Reviewer — reviews accuracy, clarity, and completeness.
    quality_reviewer = Agent(
        role='Quality Reviewer',
        goal='Review the summary and quiz for accuracy, clarity, and completeness.',
        backstory=(
            "You are a meticulous academic editor. You ensure that all content is factually "
            "correct, free of errors, and provides the best possible learning experience "
            "for the student."
        ),
        verbose=True,
        allow_delegation=False,
        llm=llm,
        tools=[]
    )

    # --- Task Definitions ---

    # Task for the Manager to set the stage
    planning_task = Task(
        description=(
            f"Define the scope and key focus areas for a study guide on {topic}. "
            "Provide a brief outline that the Summary Specialist should follow."
        ),
        expected_output="A structured outline for the study guide.",
        agent=study_manager
    )

    # Task for summary generation
    summary_task = Task(
        description=(
            f"Based on the manager's outline, write a comprehensive and structured summary of {topic}. "
            "Include key definitions, main theories, and important context."
        ),
        expected_output="A structured Markdown summary of the topic.",
        agent=summary_specialist,
        context=[planning_task]
    )

    # Task for quiz generation
    quiz_task = Task(
        description=(
            "Using the summary as a reference, create a practice quiz. "
            "Include 5 multiple-choice questions and 3 open-ended questions with an answer key."
        ),
        expected_output="A Markdown practice quiz with an answer key.",
        agent=quiz_creator,
        context=[summary_task]
    )

    # Task for quality review
    review_task = Task(
        description=(
            "Perform a final review of the summary and the quiz. "
            "Ensure everything is accurate, pedagogically sound, and well-formatted. "
            "Combine them into a single cohesive study guide."
        ),
        expected_output="The final, verified study guide in Markdown format.",
        agent=quality_reviewer,
        context=[planning_task, summary_task, quiz_task]
    )

    # Create a Crew with sequential process
    study_crew = Crew(
        agents=[study_manager, summary_specialist, quiz_creator, quality_reviewer],
        tasks=[planning_task, summary_task, quiz_task, review_task],
        process=Process.sequential,
        verbose=True
    )

    print(f"\n--- Starting Workflow for: {topic} ---\n")
    
    # Check for API Key before kickoff
    api_key = os.getenv("GOOGLE_API_KEY")
    
    if api_key and api_key != "your_google_api_key_here":
        # Run the real CrewAI workflow
        result = study_crew.kickoff()
    else:
        # Local Demo Fallback
        print("WARNING: No valid GOOGLE_API_KEY found.")
        print("CrewAI requires an LLM provider to execute real agent logic.")
        print("\n--- Simulating Local Demo Workflow ---")
        print("1. [Study Manager] -> Defining guide scope and focus areas...")
        print("2. [Summary Specialist] -> Synthesizing topic information...")
        print("3. [Quiz Creator] -> Designing practice assessments...")
        print("4. [Quality Reviewer] -> Auditing content and finalizing guide...")
        
        result = f"""# Study Guide: {topic} (DEMO)

## Executive Summary
This is a simulated study guide for **{topic}**. In a live environment with an API key, the agents would perform deep research and synthesis.

## Key Concepts
- **Concept A**: Foundational element of {topic}.
- **Concept B**: Secondary theoretical framework.

## Practice Quiz
1. What is the primary focus of {topic}?
   - A) Option 1
   - B) Option 2
   - Answer: A

## Quality Assurance
Verified for structure and clarity by the Quality Reviewer (Simulation).
"""

    print("\n" + "="*30)
    print("FINAL STUDY GUIDE")
    print("="*30 + "\n")
    print(result)

    # Save the output to a file
    os.makedirs('output', exist_ok=True)
    filename = f"output/{topic.replace(' ', '_').lower()}_guide.md"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(str(result))
    print(f"\nStudy guide saved to {filename}")

if __name__ == "__main__":
    run_study_crew()
