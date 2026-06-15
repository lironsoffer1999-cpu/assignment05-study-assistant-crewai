# Example Run Log - Study Assistant Crew

## Session Details
- **Command Executed**: `python src/main.py`
- **Date**: 2026-06-15
- **Environment**: Local Terminal

## Input
- **Study Topic**: `Machine Learning`

## Execution Summary
The system detected that the `OPENAI_API_KEY` was missing from the environment. To prevent a crash and demonstrate the architecture, it automatically pivoted to **Local Demo Fallback Mode**.

### Workflow Simulation
The following agents were demonstrated in sequence:
1.  **Study Manager**: Defined the scope and key focus areas for "Machine Learning".
2.  **Summary Specialist**: Synthesized the topic into a structured summary.
3.  **Quiz Creator**: Designed practice assessments based on the summary.
4.  **Quality Reviewer**: Audited the content for accuracy and finalized the package.

## Results
- **Status**: Success (Simulation)
- **Output File Created**: `output/machine_learning_guide.md`
- **Console Output**:
  ```text
  === Study Assistant Crew ===
  Note: This system requires an LLM provider (e.g., OpenAI) configured via environment variables.
  Ensure OPENAI_API_KEY is set in your .env file or environment.

  Enter the academic topic you'd like to study: Machine Learning

  --- Starting Workflow for: Machine Learning ---

  WARNING: No valid OPENAI_API_KEY found.
  CrewAI requires an LLM provider to execute real agent logic.

  --- Simulating Local Demo Workflow ---
  1. [Study Manager] -> Defining guide scope and focus areas...
  2. [Summary Specialist] -> Synthesizing topic information...
  3. [Quiz Creator] -> Designing practice assessments...
  4. [Quality Reviewer] -> Auditing content and finalizing guide...

  ==============================
  FINAL STUDY GUIDE
  ==============================
  # Study Guide: Machine Learning (DEMO)
  ... (Markdown content) ...

  Study guide saved to output/machine_learning_guide.md
  ```
