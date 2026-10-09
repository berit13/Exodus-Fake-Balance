# Exodus-Fake-Balance
Exodus Fake Balance — Native balance overlay tool for Exodus wallet with real-time spoofing across BTC, ETH, SOL, XRP and 200+ assets, persistent hooks, and screenshot-safe display rendering
<div align="center">

```
 ███████╗██╗  ██╗ ██████╗ ██████╗ ██╗   ██╗███████╗
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
      ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
   ██████╗  █████╗ ██╗      █████╗ ███╗   ██╗ ██████╗███████╗
   ██╔══██╗██╔══██╗██║     ██╔══██╗████╗  ██║██╔════╝██╔════╝
   ██████╔╝███████║██║     ███████║██╔██╗ ██║██║     █████╗
   ██╔══██╗██╔══██║██║     ██╔══██║██║╚██╗██║██║     ██╔══╝
   ██████╔╝██║  ██║███████╗██║  ██║██║ ╚████║╚██████╗███████╗
   ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝╚══════╝
```

# Exodus Fake Balance

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Exodus](https://img.shields.io/badge/Exodus-Wallet-8B5CF6?style=for-the-badge&logo=exodus&logoColor=white)](https://www.exodus.com/)
[![Platform](https://img.shields.io/badge/Platform-Windows%20|%20macOS-0078D4?style=for-the-badge)](/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

**Native balance overlay tool for Exodus cryptocurrency wallet — display custom balances across 200+ supported assets with persistent hooks and screenshot-safe rendering**

[Features](#features) • [How It Works](#how-it-works) • [Getting Started](#getting-started) • [Configuration](#configuration) • [Usage](#usage) • [Supported Assets](#supported-assets) • [FAQ](#faq)

</div>

---

## How It Works

Exodus Fake Balance intercepts the local Electron IPC bridge used by the Exodus desktop application to render portfolio values. The tool patches the wallet's internal balance cache at the process level — no network requests are modified, no blockchain data is altered, and no private keys are accessed. The displayed values update in real-time across all wallet tabs (Portfolio, Exchange, Send/Receive) and persist through screenshots and screen recordings.

The overlay engine uses a combination of:
- **Process memory patching** for the Electron renderer process
- **Local SQLite cache injection** for persistent balance values
- **IPC message interception** to maintain values across wallet refreshes

---

## Features

<table>
<tr>
<td width="50%">

| Feature | Status |
|---------|:------:|
| Custom balance for any asset | ✅ |
| 200+ supported cryptocurrencies | ✅ |
| Persistent across wallet restarts | ✅ |
| Screenshot-safe rendering | ✅ |
| Real-time value display (USD/EUR) | ✅ |
| Portfolio pie chart updates | ✅ |
| Transaction history spoofing | ✅ |
| Multi-wallet support | ✅ |

</td>
<td width="50%">

| Feature | Status |
|---------|:------:|
| One-click apply / restore | ✅ |
| Auto-detect Exodus installation | ✅ |
| Custom fiat currency display | ✅ |
| Exchange tab balance sync | ✅ |
| Electron IPC bridge hooking | ✅ |
| Process-level memory patching | ✅ |
| No network modification | ✅ |
| Cross-platform (Win/macOS) | ✅ |

</td>
</tr>
</table>

---

## Supported Assets

| Category | Assets |
|----------|--------|
| **Top Tier** | BTC, ETH, SOL, XRP, BNB, ADA, DOGE, DOT, AVAX, MATIC |
| **DeFi** | UNI, AAVE, COMP, MKR, SNX, SUSHI, CRV, YFI, LDO, CAKE |
| **Layer 2** | ARB, OP, IMX, MATIC, LRC, METIS, ZKS, MANTA, STRK |
| **Stablecoins** | USDT, USDC, DAI, BUSD, TUSD, FRAX, LUSD, crvUSD |
| **Meme** | DOGE, SHIB, PEPE, FLOKI, BONK, WIF, BRETT, MEME |
| **Gaming** | AXS, SAND, MANA, GALA, ENJ, ILV, IMX, RONIN |
| **Privacy** | XMR, ZEC, DASH, SCRT, ARRR, BEAM, FIRO |

> All assets listed in the Exodus wallet are supported. Custom token addresses can be added via configuration.

---

## Getting Started

### Prerequisites

- **OS:** Windows 10/11 or macOS 12+
- **Python:** 3.10 or newer
- **Exodus:** Desktop wallet installed (v24.x or newer)

### Installation

```bash
git clone https://github.com/berit13/Exodus-Fake-Balance.git
cd Exodus-Fake-Balance
```

**Windows:**

```bash
run.bat
```

**macOS / Linux:**

```bash
chmod +x run.sh
./run.sh
```

### Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| rich | ≥13.0.0 | Terminal UI & formatting |
| cryptography | latest | Data encryption |
| psutil | latest | Process detection & management |
| requests | latest | API price feeds |

---

## Configuration

Edit `config.json` to set your target balances:

```json
{
    "exodus_path": "auto",
    "target_balances": {
        "BTC": 2.45891,
        "ETH": 31.8824,
        "SOL": 412.55,
        "XRP": 25000.0,
        "BNB": 18.442,
        "USDT": 148500.00,
        "DOGE": 500000.0
    },
    "display_currency": "USD",
    "persist_on_restart": true,
    "auto_update_prices": true,
    "hook_mode": "memory",
    "restore_on_exit": false
}
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `exodus_path` | string | Path to Exodus install dir. `"auto"` for auto-detect |
| `target_balances` | object | Asset ticker → desired balance amount |
| `display_currency` | string | Fiat currency for value display (USD, EUR, GBP) |
| `persist_on_restart` | bool | Keep fake balances after Exodus restart |
| `auto_update_prices` | bool | Fetch live prices for accurate USD display |
| `hook_mode` | string | `"memory"` for live patching, `"cache"` for SQLite injection |
| `restore_on_exit` | bool | Auto-restore original balances on tool exit |

---

## Usage

### Terminal Menu

```bash
python main.py
```

```
┌──────────────────────────────────────────────────────────────┐
│              EXODUS FAKE BALANCE                             │
│    Native Balance Overlay · Exodus Wallet                    │
├──────────────────────────────────────────────────────────────┤
│  #   Action                  Description                     │
│  1   Install Dependencies    pip install -r requirements.txt │
│  2   Settings                Wallet path, balances config    │
│  3   About                   Features & contact info         │
│  4   Set Custom Balances     Configure target amounts        │
│  5   Apply Balance Overlay   Hook Exodus process             │
│  6   Restore Original        Remove hooks, restore real data │
│  7   Status Check            Verify hook state               │
│  0   Exit                    Quit                            │
└──────────────────────────────────────────────────────────────┘
```

### Quick Start

1. **Install dependencies:** Select option `1`
2. **Configure balances:** Select option `4` and enter desired amounts per asset
3. **Apply overlay:** Select option `5` — the tool detects Exodus and applies hooks
4. **Verify:** Open Exodus wallet and confirm the new balances are displayed
5. **Restore:** Select option `6` to remove all hooks and restore originals

---

## Project Structure

```
Exodus-Fake-Balance/
├── main.py                    # Entry point, terminal menu
├── config.py                  # Configuration loader (config.json)
├── bot_actions.py             # Core actions (set, apply, restore, status)
├── requirements.txt
├── run.bat / run.sh
├── config.json                # Balance targets & settings
├── actions/
│   ├── about.py               # Project info display
│   ├── install.py             # Dependency installer
│   └── settings.py            # Setup instructions
├── utils/
│   ├── bootstrap.py           # Runtime initialization
│   ├── compat.py              # Platform detection
│   ├── http.py                # HTTP client
│   ├── integrity.py           # Data verification
│   └── ui.py                  # Rich terminal interface
└── release/
    └── README.md              # Pre-compiled binary info
```

---

## FAQ

<details>
<summary><b>Does this modify the blockchain?</b></summary>

No. The tool only modifies the local display rendering inside the Exodus desktop application. No transactions are created, no blockchain data is altered, and no network requests are modified. The actual wallet balance on-chain remains unchanged.
</details>

<details>
<summary><b>Does this affect my private keys?</b></summary>

No. The tool never accesses, reads, or modifies private keys or seed phrases. It operates exclusively on the UI rendering layer of the Exodus Electron application.
</details>

<details>
<summary><b>Will the fake balance persist after restarting Exodus?</b></summary>

Yes, if `persist_on_restart` is enabled in config.json. The tool patches the local SQLite cache used by Exodus, so values survive application restarts. Disable this option to require re-application after each restart.
</details>

<details>
<summary><b>Can the fake balance be detected?</b></summary>

The overlay is rendered at the process level using the same Electron IPC bridge that Exodus uses internally. Screenshots, screen recordings, and screen sharing will all show the modified balance. However, checking the actual blockchain address via a block explorer will show the real balance.
</details>

<details>
<summary><b>Which Exodus versions are supported?</b></summary>

The tool supports Exodus Desktop v24.x and newer. Older versions may work but are not tested. The auto-detection system checks the installed version and adjusts hook offsets accordingly.
</details>

<details>
<summary><b>Can I set a balance for custom tokens?</b></summary>

Yes. Any token listed in your Exodus wallet can be targeted. Add the token ticker to the `target_balances` object in config.json. For tokens not in the default list, use the exact ticker as shown in Exodus.
</details>

<details>
<summary><b>How do I restore the original balances?</b></summary>

Select option `6` (Restore Original) from the menu, or set `restore_on_exit: true` in config.json to automatically restore when the tool exits.
</details>

---

## Disclaimer

<div align="center">

⚠️ **This tool is provided for educational and demonstration purposes only.** ⚠️

The authors are not responsible for any misuse of this software. Using this tool to deceive others in financial transactions may violate local laws. Always comply with applicable regulations in your jurisdiction.

</div>

---

<div align="center">

**Support this project**

ETH: `0x9E3d7A1c82B45f06Da4e28C1F53b90d2A17cE645`

If this tool helps you, consider giving it a ⭐

</div>
