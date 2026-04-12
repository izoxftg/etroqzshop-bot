import discord
from discord.ext import commands
from discord import app_commands
import os

# ── Config ──────────────────────────────────────────────────
TOKEN = os.environ.get("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

EMBED_COLOR = 0x7c3aed  # violet


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
    embed.set_footer(text="Etroqz Optimizer • discord.gg/XuCSfNMC")

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
        title="💜 ETROQZ OPTIMIZER — NOS OFFRES",
        color=0x7c3aed
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

    embed.set_footer(text="Etroqz Optimizer • discord.gg/XuCSfNMC")

    await target.send(embed=embed)
    await target.send("<#1480018356261355611>")
    await interaction.response.send_message(f"✅ Offres envoyées dans {target.mention} !", ephemeral=True)


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
        description="Les commandes sont **ouvertes** !\nOuvre un ticket pour commander ton optimisation.",
        color=0x57F287
    )
    embed.set_footer(text="Etroqz Optimizer • discord.gg/XuCSfNMC")

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
    embed.set_footer(text="Etroqz Optimizer • discord.gg/XuCSfNMC")

    await target.send(embed=embed)
    await target.send("@everyone")
    await interaction.response.send_message(f"✅ Message envoyé dans {target.mention} !", ephemeral=True)


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
