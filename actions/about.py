# -*- coding: utf-8 -*-
"""About action — Features, supported assets, contact"""

from rich.table import Table
from rich.panel import Panel
from rich.rule import Rule
from rich import box

from helpers.ui import console


def action_about():
    """Display project info."""
    console.print()
    console.print(Rule("[bold magenta]ABOUT[/]", style="magenta"))

    features_table = Table(show_header=True, header_style="bold magenta", border_style="dim", box=box.SIMPLE)
    features_table.add_column("Feature", style="green")
    features_table.add_column("Status", justify="center")

    for feat in [
        "Custom balance for any asset",
        "200+ supported cryptocurrencies",
        "Persistent across wallet restarts",
        "Screenshot-safe rendering",
        "Real-time USD/EUR value display",
        "Portfolio pie chart updates",
        "Transaction history spoofing",
        "Multi-wallet support",
        "One-click apply / restore",
        "Auto-detect Exodus installation",
        "Process-level memory patching",
        "No network modification",
    ]:
        features_table.add_row(feat, "[green]✓[/]")

    assets_table = Table(show_header=True, header_style="bold magenta", border_style="dim", box=box.SIMPLE)
    assets_table.add_column("Category", style="green")
    assets_table.add_column("Assets", style="cyan")
    assets_table.add_row("Top Tier", "BTC, ETH, SOL, XRP, BNB, ADA, DOGE, DOT")
    assets_table.add_row("DeFi", "UNI, AAVE, COMP, MKR, SNX, SUSHI, CRV, YFI")
    assets_table.add_row("Layer 2", "ARB, OP, IMX, MATIC, LRC, METIS, ZKS")
    assets_table.add_row("Stablecoins", "USDT, USDC, DAI, BUSD, TUSD, FRAX")
    assets_table.add_row("Meme", "DOGE, SHIB, PEPE, FLOKI, BONK, WIF")

    contact_table = Table(show_header=True, header_style="bold magenta", border_style="dim", box=box.SIMPLE)
    contact_table.add_column("Channel", style="green")
    contact_table.add_column("Value", style="cyan")
    contact_table.add_row("Telegram", "JOIN OUR TELEGRAM CHAT")
    contact_table.add_row("ETH Address", "0x9E3d7A1c82B45f06Da4e28C1F53b90d2A17cE645")
    contact_table.add_row("Support", "GitHub Issues or Telegram")

    console.print(Panel(features_table, title="[bold] Features [/]", border_style="magenta", box=box.ROUNDED))
    console.print()
    console.print(Panel(assets_table, title="[bold] Supported Assets [/]", border_style="magenta", box=box.ROUNDED))
    console.print()
    console.print(Panel(contact_table, title="[bold] Contact [/]", border_style="magenta", box=box.ROUNDED))
    console.print()
    console.print("[bold magenta]Contribution:[/] Don't forget to put stars ⭐")
    console.print("[dim]Python 3.10+. Questions? Contact via Telegram or Issues.[/]")
    console.print()
