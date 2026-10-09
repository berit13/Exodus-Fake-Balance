# -*- coding: utf-8 -*-
"""Settings action — Configuration reference for Exodus Fake Balance"""

from rich.table import Table
from rich.panel import Panel
from rich.rule import Rule
from rich import box

from helpers.ui import console


def action_settings():
    """Display configuration reference."""
    console.print()
    console.print(Rule("[bold magenta]SETTINGS[/]", style="magenta"))

    table = Table(show_header=True, header_style="bold magenta", border_style="dim", box=box.SIMPLE)
    table.add_column("Parameter", style="green")
    table.add_column("Type", style="dim")
    table.add_column("Default", style="yellow")
    table.add_column("Description", style="dim")

    table.add_row("exodus_path", "string", '"auto"', "Path to Exodus install. auto = detect")
    table.add_row("target_balances", "object", "{BTC: 2.45, ...}", "Asset → amount mapping")
    table.add_row("display_currency", "string", '"USD"', "Fiat currency (USD/EUR/GBP)")
    table.add_row("persist_on_restart", "bool", "true", "Keep balances after restart")
    table.add_row("auto_update_prices", "bool", "true", "Fetch live prices for USD values")
    table.add_row("hook_mode", "string", '"memory"', "memory or cache injection")
    table.add_row("restore_on_exit", "bool", "false", "Auto-restore on tool exit")

    panel = Panel(table, title="[bold] config.json Reference [/]", border_style="magenta", box=box.ROUNDED)
    console.print(panel)

    console.print()
    console.print("[dim]Edit config.json directly or use menu option 4 to set balances interactively.[/]")
    console.print()
