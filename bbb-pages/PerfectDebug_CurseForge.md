# PERFECT DEBUG

**Passive debug & API scanner for Hytale modders**

![Hytale](https://img.shields.io/badge/Hytale-Server%20Plugin-orange?style=for-the-badge) ![Java](https://img.shields.io/badge/Java-21-blue?style=for-the-badge) ![Free](https://img.shields.io/badge/FREE-open%20source-brightgreen?style=for-the-badge)

---

## // WHY PERFECTDEBUG?

Building Hytale plugins but can't find the API docs? PerfectDebug **automatically scans** the server API, dumps every class, method, and field to text files, sniffs events, tracks vanilla assets, and monitors performance — all in **passive mode**. Zero commands, zero config, zero impact. Just drop it in and get instant insight into Hytale's internals.

---

## // FEATURES

### API Scanner
Automatically scans **38+ server classes** using reflection:
- Full method signatures with parameter types and return types
- All fields with types and modifiers
- Class hierarchy and interfaces
- Output: one text file per class in the plugin data folder

Covers: World, PlayerRef, Entity, ItemStack, Inventory, ItemContainer, ItemModule, HytaleServer, ComponentType, and more. Scan completes in **~50ms** at startup.

### Event Sniffer
Registers listeners on all available events and logs them:
- PlayerConnectEvent
- PlayerReadyEvent
- PlayerDisconnectEvent
- PlayerChatEvent

Output saved to **events.txt**.

### Vanilla Asset Scanner
Scans the Hytale asset directory and catalogs everything:
- **581 particles** — All particle effect files
- **1,168 sounds** — All sound effect files
- **356 textures** — All block and item textures

Results saved to organized text files. Essential for finding the right particle/sound IDs for your mods.

### Performance Monitor
Periodic server health reports every **30 seconds**. Track memory usage and performance trends.

### Passive Item Tracker
Logs items seen in player inventories. Useful for discovering item IDs and understanding what's available in the game.

### Player Tracker
Logs player connections and disconnections with timestamps.

### 100% Passive
No commands needed. No configuration. No server impact. Everything runs automatically at startup and outputs to files. Drop in, start server, check the output folder.

---

## // OUTPUT FILES

All files are written to `UserData/Saves/[World]/mods/KatsuyaTV_PerfectDebug/`

| File | Content |
|------|---------|
| `api_World.txt` | World class methods and fields |
| `api_PlayerRef.txt` | PlayerRef class API |
| `api_ItemStack.txt` | ItemStack class API |
| `api_Inventory.txt` | Inventory class API |
| `api_ItemContainer.txt` | ItemContainer class API |
| `api_scan_summary.txt` | Overview of all scanned classes |
| `events.txt` | Event sniffer log |
| `vanilla_items.txt` | All registered vanilla items |
| `vanilla_blocks.txt` | All registered vanilla blocks |

---

## // INSTALLATION

1. Download **PerfectDebug-1.1.jar**
2. Place it in your server's **mods/** folder
3. Start the server — everything runs automatically
4. Check output in **UserData/Saves/[World]/mods/KatsuyaTV_PerfectDebug/**

That's it. No commands, no config, no setup.

---

## // WHO IS THIS FOR?

- **Plugin developers** — Discover undocumented API methods and build better mods
- **Server owners** — Find particle/sound/texture IDs for your custom content
- **Modders** — Understand the ECS architecture and available components
- **Content creators** — Know exactly what items, blocks, and entities exist in vanilla

---

## // TECHNICAL DETAILS

- **Platform:** Hytale Server Plugin
- **Java Version:** 21
- **Dependencies:** None
- **Price:** Free
- **Performance:** API scan ~50ms at startup. No tick loops.
- **Mode:** Fully passive — no commands, no player interaction

---

## // DOCUMENTATION

Full documentation: **[perfectplugins.github.io/wiki/perfectdebug](https://perfectplugins.github.io/wiki/perfectdebug/)**

---

*Developed by **KatsuyaTV** — Part of the [PerfectPlugins](https://perfectplugins.github.io) collection.*
