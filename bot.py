import discord
from discord.ext import commands
from discord import app_commands
import os

# ── Config ──────────────────────────────────────────────────
TOKEN = os.environ.get("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# ── Filtre de mots blacklistés ───────────────────────────────
BLACKLISTED_WORDS = [
    "cheat", "spoof", "spoofer", "hack", "hacker", "aimbot",
    "triggerbot", "wallhack", "esp", "cheatbreaker", "inject",
    "bypass", "crack", "keygen", "exploit"
]


def normalize(text: str) -> str:
    return (
        text.lower()
        .replace("4", "a").replace("@", "a")
        .replace("3", "e")
        .replace("1", "i").replace("!", "i")
        .replace("0", "o")
        .replace("5", "s").replace("$", "s")
        .replace("7", "t")
        .replace("+", "t")
        .replace("ph", "f")
    )


@bot.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return
    if message.guild and message.author.guild_permissions.administrator:
        await bot.process_commands(message)
        return

    normalized = normalize(message.content)
    found = next((w for w in BLACKLISTED_WORDS if w in normalized), None)

    if found:
        try:
            await message.delete()
        except discord.Forbidden:
            pass

        await message.channel.send(
            f"Oops {message.author.mention}! One or more words you've typed out are blacklisted from the server. Edit the word/s to \"bypass\" this filter.\n\n"
            "**Examples:**\n"
            "• cheat = chair\n"
            "• spoof = woof\n"
            "• spoofer = woofer\n"
            "• hack = h4ck",
            delete_after=10
        )

    await bot.process_commands(message)

EMBED_COLOR = 0x2ecc71  # vert


# ── Slash command /send ──────────────────────────────────────
@bot.tree.command(name="send", description="Envoie un message dans un salon")
@app_commands.describe(
    message="Contenu du message à envoyer",
    salon="Salon où envoyer le message (laisser vide = salon actuel)",
    titre="Titre du message (optionnel)"
)
async def send_message(
    interaction: discord.Interaction,
    message: str,
    salon: discord.TextChannel = None,
    titre: str = "Etroqz Shop"
):
    if not interaction.user.guild_permissions.administrator:
        await interaction.response.send_message("❌ Tu n'as pas la permission d'utiliser cette commande.", ephemeral=True)
        return

    target = salon or interaction.channel

    embed = discord.Embed(
        title=titre,
        description=message,
        color=EMBED_COLOR
    )
    embed.set_footer(text="Etroqz Shop • discord.gg/pYZbAKqN")

    await target.send(embed=embed)
    await interaction.response.send_message(f"✅ Message envoyé dans {target.mention} !", ephemeral=True)


# ── Slash command /offres ────────────────────────────────────
@bot.tree.command(name="offres", description="Envoie le message des offres Etroqz")
@app_commands.describe(salon="Salon où envoyer le message (laisser vide = salon actuel)")
async def send_offres(interaction: discord.Interaction, salon: discord.TextChannel = None):
    if not interaction.user.guild_permissions.administrator:
        await interaction.response.send_message("❌ Tu n'as pas la permission d'utiliser cette commande.", ephemeral=True)
        return

    target = salon or interaction.channel

    embed = discord.Embed(
        title="💜 ETROQZ CHEAT — NOS OFFRES",
        color=0x2ecc71
    )

    embed.add_field(name="⬛ Standard — 15€", value=(
        "➜ Point de restauration avant toute modification\n"
        "➜ Installation Atlas OS\n"
        "➜ Suppression de toutes les apps inutiles ( +30 apps )\n"
        "➜ Optimisation des apps de démarrage\n"
        "➜ Sysinternals configuré\n"
        "➜ Plan d'alimentation custom\n"
        "➜ Nettoyage complet du disque\n"
        "➜ Mises à jour Windows gérées\n"
        "➜ Paramètres écran optimisés\n"
        "➜ Optimisation graphique écran\n"
        "➜ Désactivation des notifications\n"
        "➜ Suppression des fichiers temporaires\n"
        "➜ Bluetooth désactivé\n"
        "➜ Paramètres souris optimisés\n"
        "➜ Désactivation Game Bar\n"
        "➜ Mode jeu configuré\n"
        "➜ Clavier optimisé\n"
        "➜ Confidentialité renforcée\n"
        "➜ Service WalletService désactivé\n"
        "➜ Paramètres GPU optimisés\n"
        "➜ Optimisation CPU\n"
        "➜ Optimisation Discord\n"
        "➜ Désactivation carte graphique secondaire\n"
        "➜ Optimisation connexion réseau\n"
        "➜ Chris Titus Tool appliqué\n"
        "➜ Etroqz Optimizer appliqué\n"
        "➜ Suppression complète OneDrive, Edge, Cortana, Copilot\n"
        "➜ Télémétrie Windows & NVIDIA supprimée\n"
        "➜ Sécurité renforcée ( TLS, SMB, protocoles )\n"
        "➜ SFC /scannow + DISM RestoreHealth"
    ), inline=False)

    embed.add_field(name="✦ Premium — 20€", value=(
        "➜ Tout ce qui est inclus dans le Standard\n"
        "➜ Réinstallation parfaite des pilotes graphiques\n"
        "➜ Optimisation complète des drivers carte graphique"
    ), inline=False)

    embed.add_field(name="📋 Comment commander ?", value=(
        "① Ouvre un ticket sur le Discord\n"
        "② Choisis ton offre\n"
        "③ Paie via PayPal ou carte bancaire\n"
        "④ On prend la main via AnyDesk ou TeamViewer\n"
        "⑤ PC boosté ✓\n\n"
        "🔗 https://etroqz-optimizer.netlify.app/"
    ), inline=False)

    embed.set_footer(text="Etroqz Shop • discord.gg/pYZbAKqN")

    await target.send(embed=embed)
    await target.send("<#1480018356261355611>")
    await interaction.response.send_message(f"✅ Offres envoyées dans {target.mention} !", ephemeral=True)


# ── Slash command /spoof ─────────────────────────────────────
@bot.tree.command(name="spoof", description="Envoie le message des offres Spoof Etroqz")
@app_commands.describe(salon="Salon où envoyer le message (laisser vide = salon actuel)")
async def send_spoof(interaction: discord.Interaction, salon: discord.TextChannel = None):
    if not interaction.user.guild_permissions.administrator:
        await interaction.response.send_message("❌ Tu n'as pas la permission d'utiliser cette commande.", ephemeral=True)
        return

    target = salon or interaction.channel

    embed = discord.Embed(
        title="🖥️ ETROQZ SHOP — SPOOF",
        color=0x2ecc71
    )

    embed.add_field(name="⬛ Spoof Intégral — 15€ • One Time", value=(
        "➜ Flash du BIOS\n"
        "➜ Réinstallation complète de Windows\n"
        "➜ RAID du SSD (effectué en simultané avec la réinstallation)\n"
        "➜ Spoof intégral du système\n"
        "➜ Vérification du résultat final avec toi\n"
        "⚠️ **Paiement unique — valable une seule fois**"
    ), inline=False)

    embed.add_field(name="♾️ Spoof Permanent — 45€ • Lifetime", value=(
        "➜ Tout ce qui est inclus dans le Spoof Intégral\n"
        "➜ Re-spoof illimité à vie en cas de re-ban\n"
        "➜ Support prioritaire à vie\n"
        "➜ Aucun frais supplémentaire, pour toujours ✓\n"
        "✨ **Accès à vie — un seul paiement, pour toujours**"
    ), inline=False)

    embed.add_field(name="📋 Comment ça marche ?", value=(
        "① Ouvre un ticket sur ce Discord\n"
        "② Choisis ton offre (Intégral ou Permanent)\n"
        "③ Paie via PayPal ou carte bancaire\n"
        "④ Prise en main via AnyDesk / TeamViewer\n"
        "⑤ Spoof effectué en direct sous tes yeux ✓"
    ), inline=False)

    embed.add_field(name="🔧 Compatibilité RAID", value=(
        "➜ **Ryzen (AMD)** — RAID supporté nativement\n"
        "➜ **Intel** — RAID dispo avec 2 SSD minimum"
    ), inline=False)

    embed.add_field(name="🛡️ Garantie remboursement", value=(
        "En cas de problème ou si le spoof n'a pas fonctionné, **tu es remboursé intégralement**. Aucun risque.\n\n"
        "🔗 https://etroqz-optimizer.netlify.app/"
    ), inline=False)

    embed.set_footer(text="Etroqz Shop • discord.gg/pYZbAKqN")

    await target.send(embed=embed)
    await target.send("<#1480018356261355611>")
    await interaction.response.send_message(f"✅ Offre Spoof envoyée dans {target.mention} !", ephemeral=True)


# ── Slash command /open ──────────────────────────────────────
@bot.tree.command(name="open", description="Annonce que les services sont ouverts")
@app_commands.describe(salon="Salon où envoyer le message (laisser vide = salon actuel)")
async def send_open(interaction: discord.Interaction, salon: discord.TextChannel = None):
    if not interaction.user.guild_permissions.administrator:
        await interaction.response.send_message("❌ Tu n'as pas la permission d'utiliser cette commande.", ephemeral=True)
        return

    target = salon or interaction.channel

    embed = discord.Embed(
        title="🟢 SERVICES OUVERTS",
        description="Les commandes sont **ouvertes** !\nOuvre un ticket pour passer ta commande !",
        color=0x57F287
    )
    embed.set_footer(text="Etroqz Shop • discord.gg/pYZbAKqN")

    await target.send(embed=embed)
    await target.send("@everyone")
    await interaction.response.send_message(f"✅ Message envoyé dans {target.mention} !", ephemeral=True)


# ── Slash command /update ────────────────────────────────────
@bot.tree.command(name="update", description="Annonce une mise à jour des services")
@app_commands.describe(salon="Salon où envoyer le message (laisser vide = salon actuel)")
async def send_update(interaction: discord.Interaction, salon: discord.TextChannel = None):
    if not interaction.user.guild_permissions.administrator:
        await interaction.response.send_message("❌ Tu n'as pas la permission d'utiliser cette commande.", ephemeral=True)
        return

    target = salon or interaction.channel

    embed = discord.Embed(
        title="🟠 MISE À JOUR EN COURS",
        description="Les services sont actuellement en cours de mise à jour.\nMerci de patienter, nous revenons très vite !",
        color=0xE67E22
    )
    embed.set_footer(text="Etroqz Shop • discord.gg/pYZbAKqN")

    await target.send(embed=embed)
    await target.send("@everyone")
    await interaction.response.send_message(f"✅ Message envoyé dans {target.mention} !", ephemeral=True)


# ── Slash command /close ─────────────────────────────────────
@bot.tree.command(name="close", description="Annonce que les services sont fermés")
@app_commands.describe(salon="Salon où envoyer le message (laisser vide = salon actuel)")
async def send_close(interaction: discord.Interaction, salon: discord.TextChannel = None):
    if not interaction.user.guild_permissions.administrator:
        await interaction.response.send_message("❌ Tu n'as pas la permission d'utiliser cette commande.", ephemeral=True)
        return

    target = salon or interaction.channel

    embed = discord.Embed(
        title="🔴 SERVICES FERMÉS",
        description="Les commandes sont **fermées** pour le moment.\nRevenez plus tard !",
        color=0xED4245
    )
    embed.set_footer(text="Etroqz Shop • discord.gg/pYZbAKqN")

    await target.send(embed=embed)
    await target.send("@everyone")
    await interaction.response.send_message(f"✅ Message envoyé dans {target.mention} !", ephemeral=True)


# ── Slash command /fortnite_updating ────────────────────────
@bot.tree.command(name="fortnite_updating", description="Passe Fortnite en Updating")
@app_commands.describe(salon="Salon où envoyer le message (laisser vide = salon actuel)")
async def fortnite_updating(interaction: discord.Interaction, salon: discord.TextChannel = None):
    if not interaction.user.guild_permissions.administrator:
        await interaction.response.send_message("❌ Tu n'as pas la permission d'utiliser cette commande.", ephemeral=True)
        return

    target = salon or interaction.channel

    embed = discord.Embed(title="📗 Etroqz Cheat", color=0x3498db)
    embed.add_field(name="Fortnite", value="🟢 **Undetected** → 🔵 **Updating**", inline=False)
    embed.add_field(name="📋 Details", value='Fortnite status changed from "Undetected" to "Updating"', inline=False)
    embed.set_footer(text=f"Etroqz Status Update • Aujourd'hui à {discord.utils.utcnow().strftime('%H:%M')}")

    await target.send(embed=embed)
    await interaction.response.send_message(f"✅ Fortnite → Updating envoyé dans {target.mention} !", ephemeral=True)


# ── Slash command /fortnite_undetected ──────────────────────
@bot.tree.command(name="fortnite_undetected", description="Passe Fortnite en Undetected")
@app_commands.describe(salon="Salon où envoyer le message (laisser vide = salon actuel)")
async def fortnite_undetected(interaction: discord.Interaction, salon: discord.TextChannel = None):
    if not interaction.user.guild_permissions.administrator:
        await interaction.response.send_message("❌ Tu n'as pas la permission d'utiliser cette commande.", ephemeral=True)
        return

    target = salon or interaction.channel

    embed = discord.Embed(title="📗 Etroqz Cheat", color=0x2ecc71)
    embed.add_field(name="Fortnite", value="🔵 **Updating** → 🟢 **Undetected**", inline=False)
    embed.add_field(name="📋 Details", value='Fortnite status changed from "Updating" to "Undetected"', inline=False)
    embed.set_footer(text=f"Etroqz Status Update • Aujourd'hui à {discord.utils.utcnow().strftime('%H:%M')}")

    await target.send(embed=embed)
    await interaction.response.send_message(f"✅ Fortnite → Undetected envoyé dans {target.mention} !", ephemeral=True)


# ── Slash command /cheat ─────────────────────────────────────
@bot.tree.command(name="cheat", description="Affiche les features et le pricing du cheat")
@app_commands.describe(salon="Salon où envoyer le message (laisser vide = salon actuel)")
async def send_cheat(interaction: discord.Interaction, salon: discord.TextChannel = None):
    if not interaction.user.guild_permissions.administrator:
        await interaction.response.send_message("❌ Tu n'as pas la permission d'utiliser cette commande.", ephemeral=True)
        return

    target = salon or interaction.channel

    embed = discord.Embed(
        title="✦ ETROQZ CHEAT",
        color=EMBED_COLOR
    )

    embed.add_field(name="🎯 Aimbot", value=(
        "🟢 Memory Aimbot\n"
        "🟢 Smooth Natural Draw\n"
        "🟢 Crosshair Fov"
    ), inline=False)

    embed.add_field(name="👁️ Visuals", value=(
        "🟢 Box ESP\n"
        "🟢 Skeleton ESP\n"
        "🟢 Snaplines\n"
        "🟢 Player Name ESP\n"
        "🟢 Player Distance ESP\n"
        "🟢 Player Kill ESP\n"
        "🟢 Player Rank ESP\n"
        "🟢 Player Count ESP"
    ), inline=False)

    embed.add_field(name="⚡ Exploit", value=(
        "🟢 Silent Aim\n"
        "🟢 Triggerbot\n"
        "🟢 Speedhack\n"
        "🟢 Save / Load Config"
    ), inline=False)

    embed.add_field(name="💎 Pricing", value=(
        "✉️ Etroqz Cheat | 1 Day: **$4.99**\n"
        "✉️ Etroqz Cheat | 1 Week: **$14.99**\n"
        "✉️ Etroqz Cheat | 1 Month: **$39.99**\n"
        "✉️ Etroqz Cheat | Lifetime: **$99.99**"
    ), inline=False)

    embed.add_field(name="🛒 Purchase", value="<#1480018356261355611>", inline=False)

    embed.set_footer(text="Etroqz Shop • discord.gg/pYZbAKqN")

    await target.send(embed=embed)
    await interaction.response.send_message(f"✅ Cheat envoyé dans {target.mention} !", ephemeral=True)


# ── Slash command /guide ─────────────────────────────────────
@bot.tree.command(name="guide", description="Affiche le guide d'installation du cheat")
@app_commands.describe(salon="Salon où envoyer le message (laisser vide = salon actuel)")
async def send_guide(interaction: discord.Interaction, salon: discord.TextChannel = None):
    if not interaction.user.guild_permissions.administrator:
        await interaction.response.send_message("❌ Tu n'as pas la permission d'utiliser cette commande.", ephemeral=True)
        return

    target = salon or interaction.channel

    embed = discord.Embed(
        title="📖 GUIDE D'INSTALLATION — ETROQZ CHEAT",
        color=0x9B59B6,
        description=(
            "**✅ Prérequis**\n"
            "① Être sous **Windows 10/11** (privilégier Windows 10)\n"
            "② Avoir **désactivé le Secure Boot** dans le BIOS\n"
            "\n"
            "**📦 Installation des dépendances**\n"
            "① **Visual C++ Redistributable** :\n"
            "https://aka.ms/vc14/vc_redist.x64.exe\n"
            "\n"
            "② **DirectX** :\n"
            "https://www.microsoft.com/fr-fr/download/details.aspx?id=35\n"
            "\n"
            "**⚙️ Étapes d'installation**\n"
            "① Fermer **Epic Games Launcher** et **Fortnite**\n"
            "② Lancer le **loader en tant qu'administrateur**\n"
            "③ Entrer votre **clé (key)**\n"
            "④ Taper **1** pour charger le driver\n"
            "⑤ Taper à nouveau **1** pour le mode standard\n"
            "⑥ Appuyer sur **Entrée**\n"
            "\n"
            "**🔧 Manipulation supplémentaire**\n"
            "① Ne touchez **plus au loader**\n"
            "② Lancer **Fortnite**\n"
            "③ Créer un fichier **`temp`** à la racine du disque Windows\n"
            "\n"
            "**🚀 Lancement du cheat**\n"
            "① Une fois dans le **lobby**, retourner sur le loader\n"
            "② Taper **2**, entrer votre clé si demandé\n"
            "③ Appuyer sur **Entrée**, puis retaper **2**\n"
            "\n"
            "✅ **Le cheat devrait maintenant être actif !**"
        )
    )

    embed.set_footer(text="Etroqz Shop • discord.gg/pYZbAKqN")

    await target.send(embed=embed)
    await interaction.response.send_message(f"✅ Guide envoyé dans {target.mention} !", ephemeral=True)


# ── Démarrage ────────────────────────────────────────────────
@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"✅ Bot connecté en tant que {bot.user} !")
    await bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching,
        name="Etroqz Shop"
    ))


bot.run(TOKEN)
