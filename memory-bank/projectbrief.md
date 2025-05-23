## Project Brief: LLM Game Orchestrator - Dev/Test Environment

**Project Title:** LLM Game Orchestrator - Dev/Test Environment

**1. Introduction & Goal 🎯**

This project aims to create a **local Python-based development and testing environment** for an **LLM Game Orchestrator**. The Orchestrator is the central AI "brain" for a future dynamic LitRPG web game. Its primary role is to manage game flow by understanding game context, interpreting player intentions (simulated in this environment), and delegating tasks to specialized "LLM Tools" (modular AI agents with specific functions like narrative generation, action resolution, etc.) via function calling.

The **primary goal** of this dev/test environment is to enable rapid iteration, robust testing, and focused development of the Orchestrator's logic, its system prompt, its interaction with mock tools, and its handling of simulated game state, *before* building the full game or integrating real LLM-powered tools.

**2. Core Problem Statement 💡**

Previous attempts using a monolithic LLM for game mastering faced critical issues: context window limitations, inefficient history management, unstable and overly complex system prompts, and no reliable external source of truth for game state. This project directly addresses these by building the foundation for a modular, state-aware LLM architecture.

**3. Key Components of the Dev/Test Environment 🏗️**

The environment will consist of the following interconnected Python components:

*   **LLM Game Orchestrator Harness:**
    *   Manages the Orchestrator's main system prompt.
    *   Handles direct interaction with the chosen LLM API (initially Google Gemini via its Python SDK).
    *   Processes LLM responses, specifically identifying and handling requests for function calls (tool invocation).
*   **Modular Tool System (Mocked):**
    *   Defines schemas (signatures) for various game logic tools (e.g., `NarrativeEngine`, `PlayerActionResolver`, `ProgressionStatsManager`, `StorySummarizer`).
    *   Implements **mock versions** of these tools as Python functions. These mocks will return predefined, structured JSON responses, simulating real tool behavior without actual LLM calls for the tools themselves initially.
    *   Allows for easy swapping between mock and potentially real (LLM-powered) tools later.
*   **Simulated Game State Manager:**
    *   An in-memory Python representation of essential game state (e.g., player stats, basic inventory, current location description, short narrative log).
    *   Mock tools will read from and write to this simulated state.
    *   The Orchestrator will use parts of this state to build its context.
*   **Developer Interaction Interface (CLI):**
    *   A command-line interface (e.g., using Typer or Click) for the developer to:
        *   Initiate Orchestrator cycles by providing simulated player inputs or game events.
        *   View detailed logs of the Orchestrator's process (prompt, LLM response, tool calls, data passed, tool responses).
        *   Inspect the simulated game state.
*   **Prompt Management:**
    *   A system for storing, loading, and versioning system prompts, especially for the Orchestrator.

**4. Scope & Deliverables for this Project  deliverables ✅**

*   A functional Python application runnable from the command line.
*   Implementation of the **LLM Game Orchestrator Harness** capable of making calls to the Gemini API and handling function call requests.
*   Implementation of **schemas and mock functions for at least 2-3 core tools** (e.g., `NarrativeEngine`, `PlayerActionResolver`).
*   A basic **in-memory Simulated Game State Manager**.
*   A **CLI** allowing developers to trigger orchestrator cycles with simple inputs and observe the detailed interaction flow (including which tools are called and what data is passed).
*   Clear logging of LLM prompts, tool interactions, and state changes.
*   Initial system prompt for the LLM Game Orchestrator.
*   Well-structured project with clear separation of concerns.

**Out of Scope for this Initial Project:**

*   Full game UI (the CLI is for developer use).
*   Actual LLM-powered tool implementations (mocks are sufficient for now).
*   Persistent database integration (in-memory simulation is sufficient).
*   Deployment or cloud infrastructure.
*   Advanced features like multi-turn conversation memory beyond simple summarization for the Orchestrator's context.

**5. Technology Stack 💻**

*   **Language:** Python (3.10+)
*   **LLM API:** Google Gemini API (via https://ai.google.dev/gemini-api/docs)
*   **Dependency Management:** Poetry (preferred) or Pip with `requirements.txt`
*   **CLI Framework:** Typer (preferred) or Click
*   **Data Validation (for tool schemas):** Pydantic (highly recommended for defining tool input/output structures)
*   **Version Control:** Git
*   **Development Environment:** Cursor IDE

**6. Success Criteria 🏆**

*   The developer can successfully run a simulated game turn via the CLI.
*   The Orchestrator correctly interprets a simple scenario and (based on its prompt) attempts to call the appropriate mock tool via function calling.
*   The mock tool receives the correct data and its (mocked) response is successfully returned to the Orchestrator.
*   The Orchestrator processes the tool's response and generates a plausible next step/narrative (even if simple).
*   Logs clearly show the end-to-end flow, including prompts, tool calls, and data.
*   The system is modular enough to easily add new mock tools or modify existing ones. 