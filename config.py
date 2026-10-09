# -*- coding: utf-8 -*-
"""Configuration loader for Exodus Fake Balance — config.json"""

import json
from pathlib import Path

BASE_DIR = Path(__file__).parent

_DEFAULTS = {
    "exodus_path": "auto",
    "target_balances": {
        "BTC": 2.45891,
        "ETH": 31.8824,
        "SOL": 412.55,
        "USDT": 148500.00,
    },
    "display_currency": "USD",
    "persist_on_restart": True,
    "auto_update_prices": True,
    "hook_mode": "memory",
    "restore_on_exit": False,
}


def load_config() -> dict:
    """Load configuration from config.json with defaults fallback."""
    config_path = BASE_DIR / "config.json"
    if not config_path.exists():
        save_config(_DEFAULTS)
        return dict(_DEFAULTS)

    try:
        with open(config_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        merged = dict(_DEFAULTS)
        merged.update(data)
        return merged
    except (json.JSONDecodeError, IOError):
        return dict(_DEFAULTS)


def save_config(config: dict):
    """Save configuration to config.json."""
    config_path = BASE_DIR / "config.json"
    with open(config_path, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4, ensure_ascii=False)


def get_balances(config: dict) -> dict:
    """Return target balances dict."""
    return config.get("target_balances", {})


def set_balance(config: dict, asset: str, amount: float) -> dict:
    """Set balance for a specific asset and save."""
    if "target_balances" not in config:
        config["target_balances"] = {}
    config["target_balances"][asset.upper()] = amount
    save_config(config)
    return config
