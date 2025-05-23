# Tech Context

## 1. Technologies Used

*   **Primary Language:** Python (version 3.10+)
*   **LLM API:** Google Gemini API. Access will be through the official Google Python SDK (e.g., `google-generativeai`).
*   **Dependency Management:** Poetry is the preferred tool. Pip with a `requirements.txt` file is an acceptable alternative if Poetry presents issues.
*   **CLI Framework:** Typer is preferred due to its ease of use and Pydantic integration. Click is an alternative.
*   **Data Validation (especially for Tool Schemas):** Pydantic will be used for defining and validating the structure of inputs and outputs for the mock tools (and later, real tools).
*   **Version Control:** Git. All code will be managed in a Git repository.
*   **Development Environment:** Cursor IDE is the specified IDE for development.

## 2. Development Setup

1.  **Clone Repository:** The project will be hosted in a Git repository. The first step will be to clone this repository.
2.  **Python Environment:**
    *   Ensure Python 3.10 or newer is installed.
    *   **Poetry (Preferred):**
        *   Install Poetry if not already present (`curl -sSL https://install.python-poetry.org | python3 -`).
        *   Navigate to the project directory and run `poetry install` to create a virtual environment and install dependencies specified in `pyproject.toml`.
        *   Activate the virtual environment using `poetry shell`.
    *   **Pip (Alternative):**
        *   Create a virtual environment (e.g., `python3 -m venv .venv`).
        *   Activate it (e.g., `source .venv/bin/activate`).
        *   Install dependencies from `requirements.txt` (e.g., `pip install -r requirements.txt`).
3.  **API Key Configuration:**
    *   Obtain a Google Gemini API Key (refer to [Google AI Studio](https://aistudio.google.com/app/apikey) or Google Cloud Console).
    *   The application will likely expect the API key to be set as an environment variable (e.g., `GOOGLE_API_KEY`). Specifics of how the SDK picks this up will be confirmed during implementation, but environment variables are standard.
4.  **IDE Setup:** Open the project directory in Cursor IDE.

## 3. Technical Constraints

*   **Local Execution:** The dev/test environment must run entirely locally, without requiring cloud deployment or complex external services beyond the Gemini API itself.
*   **Mock Tools Initially:** For this phase, actual LLM-powered tools are out of scope. Mock tools returning predefined JSON are required to simulate behavior and allow focus on Orchestrator logic.
*   **In-Memory State:** Game state will be managed in-memory within Python data structures. No persistent database is required for this initial project.
*   **Python Standard Library & Specified Packages:** Rely primarily on the Python standard library and the packages chosen (Gemini SDK, Poetry/Pip, Typer/Click, Pydantic).

## 4. Dependencies

*   `google-generativeai`: The official Python SDK for the Google Gemini API.
*   `poetry` (development dependency, if used)
*   `typer` (or `click`): For the CLI.
*   `pydantic`: For data validation and schema definition.
*   Other minor dependencies might be added as needed (e.g., for logging or utility functions).

    *Note: A `pyproject.toml` (for Poetry) or `requirements.txt` (for Pip) will be the source of truth for exact dependencies and versions.*

## 5. Tool Usage Patterns

*   **LLM API (Gemini):** Used by the Orchestrator Harness to send prompts (including system prompt, user input, and context from game state/tool responses) and receive responses. Crucially, it will leverage Gemini's function calling capabilities.
*   **Pydantic:** Used to define strict schemas for:
    *   The expected input arguments for each mock tool.
    *   The expected JSON structure of the responses from mock tools.
    *   This ensures that the Orchestrator knows what data to send to tools and what to expect back, and helps in validating the mock tools' behavior.
*   **Typer/Click:** Used to build the developer-facing CLI, defining commands to trigger Orchestrator cycles, inspect state, view logs, etc.
*   **Poetry/Pip:** Used to manage project dependencies and ensure a reproducible development environment.
*   **Git:** Used for all version control tasks (committing, branching, etc.). 