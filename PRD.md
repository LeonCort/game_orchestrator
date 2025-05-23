# Product Requirements Document: LLM Game Orchestrator - Dev/Test Environment

## 1. Introduction & Overview

This document outlines the requirements for the "LLM Game Orchestrator - Dev/Test Environment." The project aims to create a **local Python-based development and testing environment** for an **LLM Game Orchestrator**. This Orchestrator is envisioned as the central AI "brain" for a future dynamic LitRPG web game. Its primary role is to manage game flow by understanding game context, interpreting player intentions (simulated in this environment), and delegating tasks to specialized "LLM Tools" (modular AI agents with specific functions) via function calling.

This dev/test environment is a foundational step to enable rapid iteration, robust testing, and focused development of the Orchestrator's logic, its system prompt, its interaction with mock tools, and its handling of simulated game state, *before* undertaking full game development or integrating real LLM-powered tools.

It addresses critical issues faced in previous monolithic LLM approaches, such as context window limitations, inefficient history management, and unstable system prompts, by promoting a modular, state-aware LLM architecture.

(Reference: `memory-bank/projectbrief.md` for more details)

## 2. Goals and Objectives

*   **Primary Goal:** Enable rapid iteration, robust testing, and focused development of the LLM Game Orchestrator's core logic and its interactions within a controlled local environment.
*   **Secondary Goals:**
    *   Establish a clear, modular architecture for the future game's AI.
    *   Develop and refine the Orchestrator's system prompt.
    *   Define and test interfaces (schemas) for various game logic tools.
    *   Simulate game state management and observe its impact on Orchestrator behavior.
    *   Provide a developer-friendly CLI for interaction, observation, and debugging.

(Reference: `memory-bank/projectbrief.md` - Section 1, 6; `memory-bank/productContext.md` - Section 1, 2)

## 3. Target Audience

*   The primary target user for this dev/test environment is the **developer(s)** building and iterating on the LLM Game Orchestrator.

(Reference: `memory-bank/projectbrief.md` - Section 1)

## 4. Proposed Features & Requirements

### 4.1. LLM Game Orchestrator Harness
*   **Requirement 1.1:** Manage the Orchestrator's main system prompt (loadable from a file).
*   **Requirement 1.2:** Handle direct interaction with the Google Gemini API (via Python SDK).
    *   Authentication (API Key management, likely via environment variable).
    *   Sending well-formed requests (prompt, tool declarations).
    *   Receiving and parsing responses.
*   **Requirement 1.3:** Process LLM responses to identify and handle requests for function calls (tool invocation).
    *   Extract tool name and arguments from the LLM response.
    *   Dispatch to the appropriate mock tool.
    *   Return tool response to the LLM for further processing.

### 4.2. Modular Tool System (Mocked)
*   **Requirement 2.1:** Define Pydantic schemas for the inputs and outputs of at least 2-3 core game logic tools (e.g., `NarrativeEngine`, `PlayerActionResolver`, `ProgressionStatsManager`).
*   **Requirement 2.2:** Implement mock Python functions for these tools.
    *   Mocks must adhere to their Pydantic schemas.
    *   Mocks will return predefined, structured JSON-like responses (Pydantic models).
    *   Mocks should be able to read from and potentially write to the Simulated Game State Manager.
*   **Requirement 2.3:** The system must allow for easy registration of new mock tools and, in the future, facilitate swapping mock tools with real implementations.

### 4.3. Simulated Game State Manager
*   **Requirement 3.1:** Implement an in-memory Python representation of essential game state.
    *   Examples: player stats (e.g., HP, XP), basic inventory, current location description, short narrative log.
    *   Use Pydantic models to define the structure of game state elements.
*   **Requirement 3.2:** Provide an API for mock tools to read from and write to this simulated state.
*   **Requirement 3.3:** The Orchestrator should be able to use (parts of) this state to build its context for LLM calls.

### 4.4. Developer Interaction Interface (CLI)
*   **Requirement 4.1:** Develop a command-line interface (using Typer or Click).
*   **Requirement 4.2:** Allow developers to initiate Orchestrator cycles by providing simulated player inputs or game events (e.g., `run-cycle --input "Player attacks goblin"`).
*   **Requirement 4.3:** Provide commands to view detailed logs of the Orchestrator's process (see Logging System).
*   **Requirement 4.4:** Provide commands to inspect the current simulated game state.

### 4.5. Prompt Management
*   **Requirement 5.1:** Implement a system for storing and loading system prompts, particularly for the Orchestrator (e.g., from a `.txt` or `.md` file).
*   **Requirement 5.2:** (Optional/Future) Consider a simple versioning or selection mechanism if multiple prompt variations are to be tested.

### 4.6. Logging System
*   **Requirement 6.1:** Implement clear and detailed logging throughout the application.
*   **Requirement 6.2:** Logs should capture:
    *   The exact prompt sent to the Gemini API (including system prompt, context, and tool definitions).
    *   The raw response from the Gemini API.
    *   Identification of tool calls requested by the LLM.
    *   Data passed to mock tools.
    *   Responses received from mock tools.
    *   Changes made to the simulated game state.
    *   Final output of an orchestrator cycle.
*   **Requirement 6.3:** Logs should be easily viewable by the developer, potentially via the CLI or by outputting to a log file.

(Reference: `memory-bank/projectbrief.md` - Section 3, 4; `memory-bank/systemPatterns.md`)

## 5. Out of Scope (for this Initial Project)

*   Full game UI (the CLI is for developer use only).
*   Actual LLM-powered tool implementations (mocks are sufficient for now).
*   Persistent database integration (in-memory simulation is sufficient).
*   Deployment or cloud infrastructure.
*   Advanced features like multi-turn conversation memory beyond simple summarization for the Orchestrator's context, unless explicitly added to scope later.

(Reference: `memory-bank/projectbrief.md` - Section 4)

## 6. Technical Requirements Summary

*   **Language:** Python (3.10+)
*   **LLM API:** Google Gemini API (via Python SDK)
*   **Dependency Management:** Poetry (preferred)
*   **CLI Framework:** Typer (preferred)
*   **Data Validation:** Pydantic
*   **Version Control:** Git

(Reference: `memory-bank/techContext.md` - Section 1)

## 7. Success Criteria & Metrics

*   A developer can successfully run a simulated game turn via the CLI, providing input and receiving a plausible output from the Orchestrator.
*   The Orchestrator correctly interprets a simple scenario and, based on its system prompt and available tools, attempts to call the appropriate mock tool(s) via function calling.
*   Mock tools receive correctly formatted data (matching their Pydantic schemas).
*   Mock tools' responses are successfully returned to and processed by the Orchestrator.
*   The Orchestrator processes tool responses to generate a plausible next step, narrative update, or await further input.
*   Logs clearly show the end-to-end flow: initial input -> prompt construction -> LLM call -> tool call request -> mock tool execution -> tool response -> LLM processing of response -> final output.
*   The system is modular enough to easily add new mock tools (schema + function) or modify existing ones.
*   The developer can easily inspect the simulated game state and how it's affected by tool interactions.

(Reference: `memory-bank/projectbrief.md` - Section 6) 