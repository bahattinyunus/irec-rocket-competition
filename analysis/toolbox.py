import typer
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, FloatPrompt, IntPrompt
from rich import print
import sys
import os

# Add local directory to path to import calculators
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from calculators import parachute_sizing, link_budget, thrust_analyzer

app = typer.Typer()
console = Console()

@app.command()
def main_menu():
    """
    Launches the TULPAR Engineering Toolbox Main Menu.
    """
    print(Panel.fit("🚀 [bold cyan]TULPAR[/bold cyan] [bold white]ENGINEERING TOOLBOX[/bold white] 🚀", border_style="cyan"))
    
    while True:
        console.print("\n[bold yellow]Select a Tool:[/bold yellow]")
        console.print("1. [green]Parachute Sizing Calculator[/green]")
        console.print("2. [blue]RF Link Budget Calculator[/blue]")
        console.print("3. [red]Thrust Curve Analyzer (Sim)[/red]")
        console.print("0. [white]Exit[/white]")
        
        choice = Prompt.ask("Enter choice", choices=["1", "2", "3", "0"], default="0")
        
        if choice == "1":
            run_parachute_tool()
        elif choice == "2":
            run_link_budget_tool()
        elif choice == "3":
            run_thrust_tool()
        elif choice == "0":
            console.print("[bold cyan]Goodbye! Fly Safe. 🫡[/bold cyan]")
            break

def run_parachute_tool():
    console.print("\n🪂 [bold green]PARACHUTE SIZING[/bold green]")
    mass = FloatPrompt.ask("Rocket Mass (kg)")
    velocity = FloatPrompt.ask("Target Descent Rate (m/s)", default=6.0)
    cd = FloatPrompt.ask("Drag Coefficient (Cd)", default=1.5)
    
    dia, area = parachute_sizing.calculate_parachute_diameter(mass, velocity, cd)
    
    console.print(f"\n[bold]Results:[/bold]")
    console.print(f"Required Diameter: [bold cyan]{dia:.2f} m[/bold cyan]")
    console.print(f"Required Area:     [bold cyan]{area:.2f} m²[/bold cyan]")
    
def run_link_budget_tool():
    console.print("\n📡 [bold blue]RF LINK BUDGET[/bold blue]")
    tx_p = FloatPrompt.ask("Tx Power (dBm)", default=30.0)
    tx_g = FloatPrompt.ask("Tx Antenna Gain (dBi)", default=2.1)
    rx_g = FloatPrompt.ask("Rx Antenna Gain (dBi)", default=10.0)
    freq = FloatPrompt.ask("Frequency (MHz)", default=433.0)
    dist = FloatPrompt.ask("Distance (km)", default=10.0)
    sens = FloatPrompt.ask("Rx Sensitivity (dBm)", default=-120.0)
    
    rx_p, loss = link_budget.calculate_link_budget(tx_p, tx_g, rx_g, freq, dist)
    margin = rx_p - sens
    
    console.print(f"\n[bold]Results:[/bold]")
    console.print(f"Path Loss:      [bold yellow]{loss:.2f} dB[/bold yellow]")
    console.print(f"Received Power: [bold yellow]{rx_p:.2f} dBm[/bold yellow]")
    console.print(f"Link Margin:    [bold {'green' if margin > 10 else 'red'}]{margin:.2f} dB[/bold]")

def run_thrust_tool():
    console.print("\n🔥 [bold red]THRUST ANALYZER (Demo Mode)[/bold red]")
    console.print("Running standard simulation...")
    # Using the simulation block from the original script logic
    import numpy as np
    t = np.linspace(0, 4, 100)
    thrust = np.piecewise(t, [t < 0.5, (t >= 0.5) & (t < 3.5), t >= 3.5], [lambda x: x*2000, 1000, lambda x: 1000 - (x-3.5)*2000])
    thrust = np.clip(thrust, 0, None)
    
    impulse, max_th, avg_th, burn = thrust_analyzer.analyze_thrust_curve(t, thrust)
    
    console.print(f"\n[bold]Results:[/bold]")
    console.print(f"Total Impulse: [bold magenta]{impulse:.1f} Ns[/bold magenta]")
    console.print(f"Max Thrust:    [bold magenta]{max_th:.1f} N[/bold magenta]")
    console.print(f"Burn Time:     [bold magenta]{burn:.2f} s[/bold magenta]")
    console.print("[dim]Note: Run the standalone script to generate plots.[/dim]")

if __name__ == "__main__":
    app()
