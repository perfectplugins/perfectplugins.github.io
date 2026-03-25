import os

SITE = "c:/Users/Lenny/AppData/Roaming/Hytale/UserData/Mods/dev/perfectplugins.github.io"

def nav_html(active):
    links = [("../../", "Home"), ("../perfectportals/", "Portals"), ("../perfectnpc/", "NPC"),
             ("../perfectspawner/", "Spawner"), ("../perfectautomation/", "Automation")]
    items = []
    for href, label in links:
        cls = ' class="active"' if label == active else ""
        items.append(f'      <li><a href="{href}"{cls}>{label}</a></li>')
    return "\n".join(items)

def make_page(title, active_nav, sidebar, content):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} -- Wiki | Perfect Plugins</title>
  <link rel="stylesheet" href="../../assets/css/style.css">
</head>
<body>
<nav><div class="nav-inner">
  <a href="../../" class="nav-logo"><span>Perfect</span>Plugins</a>
  <ul class="nav-links">
{nav_html(active_nav)}
  </ul>
</div></nav>
<div class="wiki-layout">
  <aside class="wiki-sidebar">
{sidebar}
  </aside>
  <main class="wiki-content">
{content}
  </main>
</div>
<footer><p>Made by <a href="https://github.com/katsuyatvcontact-ops">KatsuyaTV</a> -- Perfect Plugins 2026</p></footer>
</body>
</html>"""

pages = {}

# ── PerfectItemManager ──
pages["perfectitemmanager"] = make_page("PerfectItemManager", "Home",
    """    <h3>PerfectItemManager</h3>
    <ul><li><a href="#overview">Overview</a></li><li><a href="#installation">Installation</a></li>
    <li><a href="#features">Features</a></li><li><a href="#commands">Commands</a></li>
    <li><a href="#permissions">Permissions</a></li><li><a href="#config">Configuration</a></li><li><a href="#faq">FAQ</a></li></ul>""",
    """    <h1 id="overview">PerfectItemManager</h1>
    <p>The most powerful item management tool for Hytale servers. Override stats, crafting recipes, quality levels, drop rules, and more for any item.</p>
    <table><tr><th>Version</th><td>1.5</td></tr><tr><th>Platform</th><td>Hytale Server Plugin</td></tr><tr><th>Languages</th><td>EN, FR, ES, IT, DE, PT</td></tr></table>
    <h2 id="installation">Installation</h2>
    <ol><li>Drop <code>PerfectItemManager-1.5.jar</code> in <code>mods/</code></li><li>Start the server</li><li>Use <code>/itemmanager menu</code></li></ol>
    <h2 id="features">Features</h2>
    <ul><li><strong>Item Stats Override</strong> -- Modify damage, armor, attributes</li><li><strong>Crafting Override</strong> -- Change or remove recipes</li><li><strong>Quality Override</strong> -- Custom quality levels</li><li><strong>Block Drop Rules</strong> -- Customize block drops</li><li><strong>Entity Drop Rules</strong> -- Customize mob drops</li><li><strong>Weapon Tooltips</strong> -- Display damage in tooltips</li><li><strong>Bulk Edit</strong> -- Apply changes to multiple items</li><li><strong>Global Multipliers</strong> -- Scale stats globally</li></ul>
    <h2 id="commands">Commands</h2>
    <table><tr><th>Command</th><th>Description</th></tr><tr><td><code>/itemmanager help</code></td><td>Display help</td></tr><tr><td><code>/itemmanager menu</code></td><td>Open item management UI</td></tr><tr><td><code>/itemmanager drops</code></td><td>Open drop rules UI</td></tr><tr><td><code>/itemmanager reload</code></td><td>Reload overrides</td></tr><tr><td><code>/itemmanager setlang &lt;code&gt;</code></td><td>Set language</td></tr></table>
    <h2 id="permissions">Permissions</h2>
    <table><tr><th>Permission</th><th>Description</th></tr><tr><td><code>perfectitemmanager.command</code></td><td>Base access</td></tr><tr><td><code>perfectitemmanager.admin</code></td><td>Reload, setlang</td></tr><tr><td><code>perfectitemmanager.menu</code></td><td>Access UI</td></tr><tr><td><code>perfectitemmanager.menu.stats</code></td><td>Edit stats</td></tr><tr><td><code>perfectitemmanager.menu.crafts</code></td><td>Edit crafting</td></tr><tr><td><code>perfectitemmanager.menu.quality</code></td><td>Edit quality</td></tr><tr><td><code>perfectitemmanager.menu.drops</code></td><td>Drop rules</td></tr></table>
    <h2 id="config">Configuration</h2>
    <pre><code>{"lang": "EN", "weaponTooltips": true}</code></pre>
    <h2 id="faq">FAQ</h2>
    <h3>Changes don't appear?</h3><p>Use <code>/itemmanager reload</code>.</p>
    <h3>Can I override vanilla items?</h3><p>Yes, any item in the game.</p>""")

# ── PerfectGuard ──
pages["perfectguard"] = make_page("PerfectGuard", "Home",
    """    <h3>PerfectGuard</h3>
    <ul><li><a href="#overview">Overview</a></li><li><a href="#installation">Installation</a></li>
    <li><a href="#anticheat">Anti-Cheat</a></li><li><a href="#moderation">Moderation</a></li>
    <li><a href="#commands">Commands</a></li><li><a href="#config">Configuration</a></li><li><a href="#faq">FAQ</a></li></ul>""",
    """    <h1 id="overview">PerfectGuard</h1>
    <p>All-in-one anti-cheat and moderation solution. 7 detection types, violation tracking, bans, mutes, reports, staff tools and admin UI.</p>
    <table><tr><th>Version</th><td>2.1</td></tr><tr><th>Platform</th><td>Hytale Server Plugin</td></tr><tr><th>Languages</th><td>EN, FR, ES, DE, IT</td></tr></table>
    <h2 id="installation">Installation</h2>
    <ol><li>Drop <code>PerfectGuard-2.1.jar</code> in <code>mods/</code></li><li>Start the server</li><li>Use <code>/pg menu</code></li></ol>
    <h2 id="anticheat">Anti-Cheat Engine</h2>
    <table><tr><th>Check</th><th>Description</th></tr><tr><td>Speed</td><td>Detects abnormal movement speed</td></tr><tr><td>Fly</td><td>Detects unauthorized flight</td></tr><tr><td>FastBreak</td><td>Impossibly fast block breaking</td></tr><tr><td>FastPlace</td><td>Impossibly fast block placing</td></tr><tr><td>Reach</td><td>Attacks beyond normal range</td></tr><tr><td>Nuker</td><td>Mass block destruction</td></tr><tr><td>AutoClick</td><td>Inhuman click rates</td></tr></table>
    <p>Violations accumulate (VL). Auto-freeze at threshold, auto-jail at higher threshold. VL decays over time.</p>
    <h2 id="moderation">Moderation Tools</h2>
    <ul><li><strong>Bans</strong> -- Permanent + temporary with reasons</li><li><strong>IP Bans</strong> -- Block IP addresses</li><li><strong>Mutes</strong> -- Permanent + temporary</li><li><strong>Warnings</strong> -- Issue and track per player</li><li><strong>Jail</strong> -- Teleport cheaters to jail</li><li><strong>Freeze</strong> -- Freeze player movement</li><li><strong>Vanish</strong> -- Invisible staff mode</li><li><strong>Inventory Inspect</strong> -- View player inventory</li><li><strong>Player Notes</strong> -- Private notes per player</li><li><strong>Reports</strong> -- Player-submitted reports</li><li><strong>Word Blacklist</strong> -- Block words in chat</li><li><strong>Announcements</strong> -- Title, notification, chat</li></ul>
    <h2 id="commands">Commands</h2>
    <table><tr><th>Command</th><th>Description</th></tr><tr><td><code>/pg help</code></td><td>All commands</td></tr><tr><td><code>/pg menu</code></td><td>Moderation UI</td></tr><tr><td><code>/pg alerts</code></td><td>Toggle alerts</td></tr><tr><td><code>/pg vanish</code></td><td>Toggle vanish</td></tr><tr><td><code>/pg freeze &lt;player&gt;</code></td><td>Freeze</td></tr><tr><td><code>/pg ban &lt;player&gt; &lt;reason&gt;</code></td><td>Permanent ban</td></tr><tr><td><code>/pg tempban &lt;player&gt; &lt;dur&gt; &lt;reason&gt;</code></td><td>Temp ban</td></tr><tr><td><code>/pg unban &lt;player&gt;</code></td><td>Unban</td></tr><tr><td><code>/pg mute &lt;player&gt; &lt;reason&gt;</code></td><td>Mute</td></tr><tr><td><code>/pg unmute &lt;player&gt;</code></td><td>Unmute</td></tr><tr><td><code>/pg kick &lt;player&gt; &lt;reason&gt;</code></td><td>Kick</td></tr><tr><td><code>/pg jail &lt;player&gt;</code></td><td>Send to jail</td></tr><tr><td><code>/pg setjail</code></td><td>Set jail location</td></tr><tr><td><code>/pg warn &lt;player&gt; &lt;reason&gt;</code></td><td>Warn</td></tr><tr><td><code>/pg tp &lt;player&gt;</code></td><td>Teleport to</td></tr><tr><td><code>/pg invsee &lt;player&gt;</code></td><td>View inventory</td></tr><tr><td><code>/pg report &lt;player&gt; &lt;reason&gt;</code></td><td>Report (player)</td></tr><tr><td><code>/pg reload</code></td><td>Reload config</td></tr></table>
    <h2 id="config">Configuration</h2>
    <pre><code>{"lang":"EN","speedEnabled":true,"speedThreshold":12.0,"flyEnabled":true,"autoFreezeVL":50,"autoJailVL":100,"vlDecaySeconds":60}</code></pre>
    <h2 id="faq">FAQ</h2>
    <h3>False positives?</h3><p>Increase thresholds in config.</p>
    <h3>Where is jail?</h3><p>Use <code>/pg setjail</code> at your desired location.</p>""")

# ── PerfectKits ──
pages["perfectkits"] = make_page("PerfectKits", "Home",
    """    <h3>PerfectKits</h3>
    <ul><li><a href="#overview">Overview</a></li><li><a href="#installation">Installation</a></li>
    <li><a href="#features">Features</a></li><li><a href="#commands">Commands</a></li>
    <li><a href="#config">Configuration</a></li><li><a href="#faq">FAQ</a></li></ul>""",
    """    <h1 id="overview">PerfectKits</h1>
    <p>Create, distribute, and manage kits with full UI support. Cooldowns, permissions, auto-give on first join, broadcast notifications, and command execution.</p>
    <table><tr><th>Version</th><td>1.1</td></tr><tr><th>Platform</th><td>Hytale Server Plugin</td></tr><tr><th>Languages</th><td>EN, FR, ES, DE, IT</td></tr></table>
    <h2 id="installation">Installation</h2>
    <ol><li>Drop <code>PerfectKits-1.1.jar</code> in <code>mods/</code></li><li>Start the server</li><li>Use <code>/kit admin</code></li></ol>
    <h2 id="features">Features</h2>
    <ul><li><strong>Kit Builder</strong> -- Create kits via inventory picker UI</li><li><strong>Cooldowns</strong> -- Per-player cooldown tracking</li><li><strong>Permissions</strong> -- Optional permission per kit</li><li><strong>Auto-give</strong> -- Give kits on first join</li><li><strong>Broadcast</strong> -- Announce kit claims</li><li><strong>Commands</strong> -- Execute commands on claim</li><li><strong>Custom Icons</strong> -- Per-kit display icons</li><li><strong>Priority Sorting</strong> -- Control display order</li></ul>
    <h2 id="commands">Commands</h2>
    <h3>Player</h3>
    <table><tr><th>Command</th><th>Description</th></tr><tr><td><code>/kit list</code></td><td>List kits</td></tr><tr><td><code>/kit claim &lt;kit&gt;</code></td><td>Claim kit</td></tr><tr><td><code>/kit menu</code></td><td>Kit menu</td></tr></table>
    <h3>Admin</h3>
    <table><tr><th>Command</th><th>Description</th></tr><tr><td><code>/kit create &lt;name&gt;</code></td><td>Create kit</td></tr><tr><td><code>/kit delete &lt;name&gt;</code></td><td>Delete kit</td></tr><tr><td><code>/kit additem &lt;kit&gt; [item] [qty]</code></td><td>Add item</td></tr><tr><td><code>/kit setcooldown &lt;kit&gt; &lt;sec&gt;</code></td><td>Set cooldown</td></tr><tr><td><code>/kit setperm &lt;kit&gt; &lt;perm&gt;</code></td><td>Set permission</td></tr><tr><td><code>/kit setautogive &lt;kit&gt; &lt;bool&gt;</code></td><td>Auto-give</td></tr><tr><td><code>/kit give &lt;player&gt; &lt;kit&gt;</code></td><td>Give to player</td></tr><tr><td><code>/kit admin</code></td><td>Admin UI</td></tr><tr><td><code>/kit reload</code></td><td>Reload</td></tr></table>
    <h2 id="config">Configuration</h2>
    <pre><code>{"lang": "EN", "maxKitsPerPlayer": 0}</code></pre>
    <p><code>maxKitsPerPlayer: 0</code> = unlimited.</p>
    <h2 id="faq">FAQ</h2>
    <h3>Cooldown not working?</h3><p>Set in seconds: <code>/kit setcooldown starter 3600</code> = 1 hour.</p>""")

# ── PerfectLootbox ──
pages["perfectlootbox"] = make_page("PerfectLootbox", "Home",
    """    <h3>PerfectLootbox</h3>
    <ul><li><a href="#overview">Overview</a></li><li><a href="#installation">Installation</a></li>
    <li><a href="#features">Features</a></li><li><a href="#items">Variants</a></li>
    <li><a href="#commands">Commands</a></li><li><a href="#permissions">Permissions</a></li><li><a href="#faq">FAQ</a></li></ul>""",
    """    <h1 id="overview">PerfectLootbox</h1>
    <p>Create, customize, and distribute lootboxes with stunning 3D opening animations. 10 chest + 10 key models, weighted drop pools, holograms.</p>
    <table><tr><th>Version</th><td>1.0</td></tr><tr><th>Platform</th><td>Hytale Server Plugin</td></tr><tr><th>Languages</th><td>EN, FR, ES, DE, IT</td></tr></table>
    <h2 id="installation">Installation</h2>
    <ol><li>Drop <code>PerfectLootbox-1.0.jar</code> in <code>mods/</code></li><li>Start the server</li><li>Use <code>/plb menu</code></li></ol>
    <h2 id="features">Features</h2>
    <ul><li><strong>Custom Lootboxes</strong> -- Unlimited types with custom names</li><li><strong>Drop Pools</strong> -- Weighted random drops</li><li><strong>3D Models</strong> -- 10 chests + 10 keys included</li><li><strong>Holograms</strong> -- Display above placed lootboxes</li><li><strong>Animations</strong> -- Opening animation</li><li><strong>Key System</strong> -- Matching key required</li><li><strong>Protection</strong> -- Placed lootboxes protected</li></ul>
    <h2 id="items">Chest &amp; Key Variants</h2>
    <p><strong>Chests (10):</strong> Gold (Blue, Green, Pink, Red, Silver) + Silver (Blue, Green, Pink, Red, Yellow)</p>
    <p><strong>Keys (10):</strong> Gold (Blue, Green, Pink, Red, Silver) + Silver (Blue, Green, Pink, Red, Yellow)</p>
    <h2 id="commands">Commands</h2>
    <table><tr><th>Command</th><th>Description</th></tr><tr><td><code>/plb list</code></td><td>List lootboxes</td></tr><tr><td><code>/plb claim &lt;name&gt;</code></td><td>Claim with key</td></tr><tr><td><code>/plb menu</code></td><td>Admin UI</td></tr><tr><td><code>/plb create &lt;name&gt;</code></td><td>Create lootbox</td></tr><tr><td><code>/plb adddrop &lt;name&gt; &lt;item&gt; [weight] [qty]</code></td><td>Add drop</td></tr><tr><td><code>/plb get &lt;name&gt; [qty]</code></td><td>Give lootbox</td></tr><tr><td><code>/plb getkey &lt;name&gt; [qty]</code></td><td>Give key</td></tr><tr><td><code>/plb givekey &lt;player&gt; &lt;key&gt; [qty]</code></td><td>Give key to player</td></tr><tr><td><code>/plb reload</code></td><td>Reload</td></tr></table>
    <h2 id="permissions">Permissions</h2>
    <table><tr><th>Permission</th><th>Description</th></tr><tr><td><code>perfectlootbox.command</code></td><td>Base (list, claim)</td></tr><tr><td><code>perfectlootbox.admin</code></td><td>Admin commands</td></tr><tr><td><code>perfectlootbox.place</code></td><td>Place lootboxes</td></tr></table>
    <h2 id="faq">FAQ</h2>
    <h3>Player can't open?</h3><p>They need the matching key in inventory.</p>""")

# ── PerfectSellChest ──
pages["perfectsellchest"] = make_page("PerfectSellChest", "Home",
    """    <h3>PerfectSellChest</h3>
    <ul><li><a href="#overview">Overview</a></li><li><a href="#installation">Installation</a></li>
    <li><a href="#features">Features</a></li><li><a href="#commands">Commands</a></li>
    <li><a href="#config">Configuration</a></li><li><a href="#economy">Economy</a></li><li><a href="#faq">FAQ</a></li></ul>""",
    """    <h1 id="overview">PerfectSellChest</h1>
    <p>Automatic item selling from chests. Place a SellChest, items sell every 30 seconds. No commands, no menus, no hassle.</p>
    <table><tr><th>Version</th><td>1.1</td></tr><tr><th>Platform</th><td>Hytale Server Plugin</td></tr><tr><th>Dependencies</th><td>Economy plugin</td></tr></table>
    <h2 id="installation">Installation</h2>
    <ol><li>Drop <code>PerfectSellChest-1.1.jar</code> in <code>mods/</code></li><li>Install a compatible economy plugin</li><li>Start the server</li><li>Place a SellChest and <code>/sellchest</code></li></ol>
    <h2 id="features">Features</h2>
    <ul><li><strong>Auto-Sell</strong> -- Every 30 seconds</li><li><strong>Multipliers</strong> -- 1x and 2x chest variants</li><li><strong>Per-Player Limits</strong> -- Max chests per player</li><li><strong>Notifications</strong> -- Toggleable sale messages</li><li><strong>Holograms</strong> -- Info display above chest</li></ul>
    <h2 id="commands">Commands</h2>
    <table><tr><th>Command</th><th>Description</th></tr><tr><td><code>/sellchest</code></td><td>Register nearby chest</td></tr><tr><td><code>/sellchest notify</code></td><td>Toggle notifications</td></tr><tr><td><code>/sellchest info</code></td><td>View stats</td></tr></table>
    <h2 id="config">Configuration</h2>
    <pre><code>{"economyPlugin":"HTSkyBlock","defaultChestLimit":5}</code></pre>
    <h2 id="economy">Compatible Economy Plugins</h2>
    <ul><li>HTSkyBlock (native)</li><li>EconomySystem</li><li>Ecotale</li><li>Economy/Ryukazan</li></ul>
    <h2 id="faq">FAQ</h2>
    <h3>Items not selling?</h3><p>Register with <code>/sellchest</code> and check economy plugin is installed.</p>""")

# ── PerfectCasino ──
pages["perfectcasino"] = make_page("PerfectCasino", "Home",
    """    <h3>PerfectCasino</h3>
    <ul><li><a href="#overview">Overview</a></li><li><a href="#installation">Installation</a></li>
    <li><a href="#features">Features</a></li><li><a href="#commands">Commands</a></li>
    <li><a href="#config">Configuration</a></li><li><a href="#faq">FAQ</a></li></ul>""",
    """    <h1 id="overview">PerfectCasino</h1>
    <p>Slot machine gambling with player balances, configurable betting, and a shared rainbow pool jackpot announced hourly.</p>
    <table><tr><th>Version</th><td>1.0</td></tr><tr><th>Platform</th><td>Hytale Server Plugin</td></tr><tr><th>Languages</th><td>EN, FR, ES, DE, IT</td></tr></table>
    <h2 id="installation">Installation</h2>
    <ol><li>Drop <code>PerfectCasino-1.0.jar</code> in <code>mods/</code></li><li>Start the server</li><li>Place a Slot Machine and interact</li></ol>
    <h2 id="features">Features</h2>
    <ul><li><strong>Slot Machines</strong> -- Place and spin</li><li><strong>Player Balances</strong> -- Per-player currency</li><li><strong>Betting</strong> -- Min/max/default configurable</li><li><strong>Rainbow Pool</strong> -- Shared jackpot, hourly announcements</li><li><strong>Starting Balance</strong> -- New players get starting amount</li><li><strong>Animation</strong> -- Spin animation</li></ul>
    <h2 id="commands">Commands</h2>
    <table><tr><th>Command</th><th>Description</th></tr><tr><td><code>/casino balance</code></td><td>View balance</td></tr><tr><td><code>/casino pool</code></td><td>View jackpot</td></tr><tr><td><code>/casino give &lt;player&gt; &lt;amt&gt;</code></td><td>Add balance (admin)</td></tr><tr><td><code>/casino take &lt;player&gt; &lt;amt&gt;</code></td><td>Remove balance (admin)</td></tr><tr><td><code>/casino setpool &lt;amt&gt;</code></td><td>Set jackpot (admin)</td></tr><tr><td><code>/casino reload</code></td><td>Reload (admin)</td></tr></table>
    <h2 id="config">Configuration</h2>
    <pre><code>{"lang":"EN","startingBalance":100,"minBet":1,"maxBet":100,"defaultBet":10,"initialPool":1000}</code></pre>
    <h2 id="faq">FAQ</h2>
    <h3>How does the rainbow pool work?</h3><p>A portion of each bet grows the pool. Lucky spins can win it. Announced hourly.</p>""")

# Write all
for slug, html in pages.items():
    path = f"{SITE}/wiki/{slug}/index.html"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  Created wiki/{slug}/index.html")

print(f"\nDone! {len(pages)} wiki pages created.")
