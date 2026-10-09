# -*- coding: utf-8 -*-
"""Exodus Fake Balance — Rich terminal UI"""

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich.rule import Rule
from rich import box

console = Console(force_terminal=True, color_system="auto")

LOGO = r"""███████╗██╗  ██╗ ██████╗ ██████╗ ██╗   ██╗███████╗
██╔════╝╚██╗██╔╝██╔═══██╗██╔══██╗██║   ██║██╔════╝
█████╗   ╚███╔╝ ██║   ██║██║  ██║██║   ██║███████╗
██╔══╝   ██╔██╗ ██║   ██║██║  ██║██║   ██║╚════██║
███████╗██╔╝ ██╗╚██████╔╝██████╔╝╚██████╔╝███████║
╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝
    ███████╗ █████╗ ██╗  ██╗███████╗
    ██╔════╝██╔══██╗██║ ██╔╝██╔════╝
    █████╗  ███████║█████╔╝ █████╗
    ██╔══╝  ██╔══██║██╔═██╗ ██╔══╝
    ██║     ██║  ██║██║  ██╗███████╗
    ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝"""


def print_banner():
    """Print main banner."""
    panel = Panel(
        Text.from_markup(
            f"[bold magenta]{LOGO}[/]\n\n"
            "[bold white]N A T I V E   B A L A N C E   O V E R L A Y[/]\n"
            "[dim]Exodus Wallet  |  200+ Assets  |  Persistent Hooks  |  Screenshot-Safe[/]"
        ),
        box=box.ROUNDED,
        border_style="magenta",
        padding=(0, 2),
        title="[bold white on magenta] EXODUS FAKE BALANCE [/]",
        title_align="center",
    )
    console.print(panel)


def show_menu_table(menu_items: list) -> str:
    """Display menu."""
    console.print()
    console.print(Rule("[bold magenta]MENU[/]", style="magenta"))
    table = Table(
        show_header=True,
        header_style="bold magenta",
        border_style="dim",
        box=box.SIMPLE,
        expand=True,
    )
    table.add_column("[#]", style="bold", justify="center", width=4)
    table.add_column("Action", style="green")
    table.add_column("Description", style="dim")

    for key, action, desc in menu_items:
        table.add_row(key, action, desc)

    console.print(table)
    return console.input("\n[bold magenta]Select action [#]: [/]").strip()


def show_load_status_table(config: dict):
    """Display load status."""
    console.print()
    console.print(Rule("[bold magenta]STATUS[/]", style="magenta"))
    table = Table(
        show_header=True,
        header_style="bold magenta",
        border_style="dim",
        box=box.SIMPLE,
    )
    table.add_column("Parameter", style="green")
    table.add_column("Value", justify="center")
    table.add_column("Status", justify="center", style="bold")

    exodus_path = config.get("exodus_path", "auto")
    balances = config.get("target_balances", {})
    table.add_row("Exodus Path", str(exodus_path), "[green]AUTO[/]" if exodus_path == "auto" else "[cyan]CUSTOM[/]")
    table.add_row("Target Assets", str(len(balances)), "[green]OK[/]" if balances else "[red]NONE[/]")
    table.add_row("Hook Mode", config.get("hook_mode", "memory"), "[green]READY[/]")
    table.add_row("Persistence", "ON" if config.get("persist_on_restart") else "OFF", "[green]✓[/]" if config.get("persist_on_restart") else "[dim]—[/]")

    console.print(table)
    console.print()


def show_balance_table(balances: list):
    """Display balance configuration."""
    console.print()
    console.print(Rule("[bold magenta]TARGET BALANCES[/]", style="magenta"))
    table = Table(
        show_header=True,
        header_style="bold magenta",
        border_style="dim",
        box=box.SIMPLE,
    )
    table.add_column("#", style="dim", justify="right", width=3)
    table.add_column("Asset", style="cyan")
    table.add_column("Amount", style="green", justify="right")
    table.add_column("USD Value", style="yellow", justify="right")

    for i, row in enumerate(balances):
        table.add_row(str(i + 1), *row)

    console.print(table)
    console.print()


def show_hook_status_table(status_rows: list):
    """Display hook status."""
    console.print()
    console.print(Rule("[bold magenta]HOOK STATUS[/]", style="magenta"))
    table = Table(
        show_header=True,
        header_style="bold magenta",
        border_style="dim",
        box=box.SIMPLE,
    )
    table.add_column("Component", style="green")
    table.add_column("PID", justify="center", style="cyan")
    table.add_column("State", justify="center")

    for row in status_rows:
        table.add_row(*row)

    console.print(table)
    console.print()


def print_success(msg: str):
    console.print(f"[green]✓[/] {msg}")


def print_error(msg: str):
    console.print(f"[red]✗[/] {msg}")


def print_info(msg: str):
    console.print(f"[cyan]i[/] {msg}")


def print_warning(msg: str):
    console.print(f"[yellow]![/] {msg}")


def separator(char: str = "─", length: int = 58):
    """Rich Rule-style separator."""
    console.print(Rule(style="dim"))


def progress_bar(current: int, total: int, width: int = 30, prefix: str = ""):
    """Display progress bar."""
    filled = int(width * current / total) if total > 0 else 0
    pct = (current / total * 100) if total > 0 else 0
    bar = "█" * filled + "░" * (width - filled)
    console.print(f"\r{prefix}[magenta]{bar}[/] [dim]{pct:.0f}%[/]", end="")
