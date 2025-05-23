# System Patterns

## 1. System Architecture Overview

The LLM Game Orchestrator Dev/Test Environment is designed as a modular, Python-based command-line application. The architecture centers around an **Orchestrator Harness** that interacts with the Gemini LLM. This Orchestrator, guided by a system prompt, interprets simulated player inputs and game context, and then delegates specific tasks to a **Modular Tool System**. These tools are initially implemented as **mock Python functions** that simulate the behavior of more complex (potentially LLM-driven) game logic components. A **Simulated Game State Manager** provides an in-memory representation of the game world, which the Orchestrator uses for context and which mock tools can read from and write to. A **Developer CLI** serves as the primary interaction point for initiating game cycles and observing system behavior.

```mermaid
flowchart TD
    DeveloperCLI[Developer CLI] -->|Simulated Input/Event| OrchestratorHarness[LLM Game Orchestrator Harness]
    OrchestratorHarness -->|Prompt + Context| GeminiAPI[Google Gemini API]
    GeminiAPI -->|Response (incl. Tool Call Request)| OrchestratorHarness
    OrchestratorHarness -->|Identified Tool Call + Data| ModularToolSystem{Modular Tool System}
    ModularToolSystem -- MockTool1 -->|Data In, Reads/Writes State| SimulatedGameState[Simulated Game State Manager]
    ModularToolSystem -- MockTool2 -->|Data In, Reads/Writes State| SimulatedGameState
    SimulatedGameState -->|State Info| OrchestratorHarness
    ModularToolSystem -->|Mocked JSON Response| OrchestratorHarness
    OrchestratorHarness -->|Logs, Output| DeveloperCLI
```

## 2. Key Technical Decisions & Design Patterns

*   **Modular Design:** The core principle is modularity. The Orchestrator, Tools, and State Manager are distinct components. This is a direct response to the problems with monolithic LLM game masters.
    *   *Pattern:* Separation of Concerns.
*   **Orchestrator Pattern:** The central LLM acts as an orchestrator, not a doer of all tasks. It decides *what* needs to be done and delegates to tools.
*   **Function Calling (Tool Use):** The Gemini API's function calling capability is a cornerstone. The Orchestrator is prompted to request function calls, and the harness executes these against the mock tool system.
    *   *This is a specific form of the Strategy Pattern, where the LLM chooses the 'strategy' (tool) to employ.*
*   **Mocking/Simulation:** Tools are mocked to allow focused development on the Orchestrator's logic and its interaction with the tool system, without the complexity or cost of real LLM tool calls at this stage.
    *   *Pattern:* Test Doubles (specifically Mocks/Stubs).
*   **Schema-Defined Interfaces:** Pydantic will be used to define strict schemas for tool inputs and outputs. This ensures clear contracts between the Orchestrator and the tools.
    *   *Pattern:* Interface-Based Design / Design by Contract.
*   **In-Memory State:** Game state is kept in Python data structures for simplicity and speed in this dev/test environment.
*   **CLI for Interaction:** A command-line interface provides a simple, scriptable way for developers to interact with and test the system.
*   **System Prompt Driven Behavior:** The Orchestrator's primary logic and decision-making process will be heavily influenced by its system prompt. Iterating on this prompt is a key development activity.

## 3. Component Relationships & Data Flow

1.  **Developer CLI to Orchestrator Harness:** The developer provides an input (e.g., "player says 'hello'") via the CLI. This input is passed to the Orchestrator Harness.
2.  **Orchestrator Harness to Gemini API:** The Harness constructs a prompt for the Gemini API. This prompt includes:
    *   The Orchestrator's main system prompt.
    *   The list of available tools (function declarations) and their schemas.
    *   The developer's input.
    *   Relevant context from the Simulated Game State Manager (e.g., recent narrative, player status).
3.  **Gemini API to Orchestrator Harness:** The Gemini API processes the prompt and returns a response. This response may include:
    *   A direct textual response.
    *   A request to call one or more functions (tools) with specific arguments.
4.  **Orchestrator Harness to Modular Tool System:** If the LLM requests a function call, the Harness identifies the target mock tool and the arguments. It then invokes the appropriate Python mock function, passing the arguments (validated against the Pydantic schema).
5.  **Modular Tool System (Mock Tool) and Simulated Game State Manager:**
    *   The mock tool executes its predefined logic.
    *   It may read data from the Simulated Game State Manager (e.g., to check a player's skill).
    *   It may write data to the Simulated Game State Manager (e.g., to update player inventory or log a narrative event).
    *   It returns a structured JSON response (as defined by its Pydantic output schema) to the Orchestrator Harness.
6.  **Modular Tool System to Orchestrator Harness:** The mock tool's response is passed back.
7.  **Orchestrator Harness (Loop or Final Response):**
    *   The Harness takes the tool's response and typically sends it back to the Gemini API along with the original request context so the LLM can process the tool's output and generate a final response or decide on the next action (which might involve another tool call).
    *   This cycle (LLM -> Tool -> LLM) may repeat multiple times in a single "turn."
8.  **Orchestrator Harness to Developer CLI:** Once the Orchestrator determines a final output for the turn (e.g., a piece of narrative, an update to the player), this is displayed on the CLI. Detailed logs of the entire interaction (prompts, LLM responses, tool calls, data passed, state changes) are also made available.

## 4. Critical Implementation Paths

*   **Orchestrator Harness - Gemini API Interaction:** Correctly formatting prompts, handling API responses, and especially managing the function calling request/response cycle.
*   **Tool Schema Definition (Pydantic):** Clearly defining the input and output structures for each tool.
*   **Mock Tool Implementation:** Ensuring mock tools adhere to their schemas and correctly simulate interactions with the game state.
*   **Simulated Game State Management:** Designing a simple yet effective in-memory representation of the game state that can be easily accessed and modified.
*   **CLI Interaction Logic:** Building intuitive CLI commands for developers to drive the system and inspect its state.
*   **Logging:** Comprehensive logging is critical for debugging and understanding the system's behavior. 