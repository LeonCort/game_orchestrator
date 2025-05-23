import typer

app = typer.Typer()

@app.command()
def hello(name: str = "World"):
    """
    A simple greeting.
    """
    print(f"Hello {name}")

@app.command()
def run_cycle(input_text: str = typer.Option(..., "--input", "-i", help="Simulated player input.")):
    """
    Simulates a single cycle of the game orchestrator.
    (Currently a placeholder)
    """
    print(f"Received input: {input_text}")
    print("Orchestrator cycle (placeholder)...")
    # Future: Initialize Orchestrator, call Gemini, process response, etc.

if __name__ == "__main__":
    app()
