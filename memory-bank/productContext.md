# Product Context

## 1. Why This Project Exists

This project, the "LLM Game Orchestrator - Dev/Test Environment," exists to lay the foundational groundwork for a future dynamic LitRPG web game. The core idea is to move away from problematic monolithic LLM approaches for game mastering and towards a more robust, modular, and state-aware AI architecture. Previous attempts suffered from context window limitations, inefficient game history management, unstable and overly complex system prompts, and a lack of a reliable external source of truth for game state. This dev/test environment is the first step in systematically addressing these challenges.

## 2. Problems It Solves

The primary problems this dev/test environment aims to solve (and by extension, the future Orchestrator) are:

*   **Scalability and Complexity of Game Logic:** A single LLM struggles to manage all aspects of a dynamic game. This project introduces a modular approach where an Orchestrator delegates tasks to specialized tools.
*   **Context Window Limitations:** By using an Orchestrator and tools, the context provided to each LLM call can be more focused and relevant, mitigating issues with large, unwieldy contexts.
*   **State Management:** It establishes a clear mechanism for managing and updating game state, providing a source of truth that can be reliably read from and written to by different components.
*   **Development Efficiency:** It provides a controlled environment for developing and testing the core Orchestrator logic, its system prompt, and tool interactions without the overhead of a full game or real (and potentially costly) LLM tool calls during early development.
*   **Iterative Development:** Allows for rapid iteration on the Orchestrator's prompt and logic, and the definition of tool interfaces (schemas).

## 3. How It Should Work (User Experience - Developer Focus)

From the developer's perspective (the primary user of this dev/test environment), the system should work as follows:

1.  **Setup:** The developer can easily set up the Python environment, likely using Poetry, and configure it with their Google Gemini API key.
2.  **Interaction:** The developer interacts with the system via a Command Line Interface (CLI).
3.  **Initiating a Cycle:** The developer can input a simulated player action or game event through the CLI.
4.  **Orchestrator Activation:** This input triggers the LLM Game Orchestrator.
5.  **Prompting & LLM Call:** The Orchestrator uses its system prompt, the developer's input, and relevant parts of the simulated game state to make a call to the Google Gemini API.
6.  **Tool Call Identification:** The Orchestrator analyzes the LLM's response to identify any requests to call a function (i.e., use a tool).
7.  **Mock Tool Execution:** If a tool call is identified, the Orchestrator invokes the corresponding mock Python function, passing the required data (as defined by the tool's schema).
8.  **State Update & Tool Response:** The mock tool simulates its operation, potentially reading from and writing to the in-memory game state, and returns a predefined, structured JSON response.
9.  **Response Processing:** The Orchestrator receives the mock tool's response and incorporates it into its context for the next step (e.g., generating a narrative update or deciding on the next action).
10. **Logging & Observation:** Throughout this process, detailed logs are generated, showing the prompts sent to the LLM, the LLM's raw response, which tools were called, the data passed to and from tools, and any changes to the game state. The developer can inspect these logs and the game state via the CLI.
11. **Iteration:** The developer can easily modify the Orchestrator's system prompt, tool schemas, mock tool logic, or game state simulation and re-run cycles to test changes.

## 4. User Experience Goals (Developer Focus)

*   **Clarity & Transparency:** The flow of logic, data, and decision-making within the Orchestrator and its tool interactions should be extremely clear and transparent through detailed logging.
*   **Ease of Iteration:** Developers should be able to quickly make changes (to prompts, tool definitions, mock logic) and see the results without a cumbersome build or deployment process.
*   **Control & Inspectability:** Full control over simulated inputs and the ability to inspect every part of the system (prompts, responses, state) is crucial.
*   **Modularity & Extensibility:** The system should feel modular, making it straightforward to define new tools, modify existing ones, or (in the future) swap mock tools for real implementations.
*   **Rapid Feedback Loop:** The time between making a change and observing its effect should be minimal.
*   **Focused Development:** The environment should allow developers to concentrate on the Orchestrator and tool interaction logic without being bogged down by UI development, database management, or complex LLM tool implementations at this stage. 