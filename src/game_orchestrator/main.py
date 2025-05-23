import typer
import logging

# Configure basic logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logger = logging.getLogger(__name__)

app = typer.Typer()

@app.command()
def hello(name: str = "World"):
    """
    A simple greeting.
    """
    logger.info(f"Executing hello command with name: {name}")
    print(f"Hello {name}")

@app.command()
def run_cycle(input_text: str = typer.Option(..., "--input", "-i", help="Simulated player input.")):
    """
    Simulates a single cycle of the game orchestrator.
    (Currently a placeholder)
    """
    logger.info(f"run_cycle called with input: '{input_text}'")
    print(f"Received input: {input_text}")
    print("Orchestrator cycle (placeholder)...")
    # Future: Initialize Orchestrator, call Gemini, process response, etc.
    logger.info("run_cycle finished (placeholder).")

if __name__ == "__main__":
    app()
