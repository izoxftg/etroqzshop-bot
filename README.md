# Etroqz Bot — Guide d'installation

## 1. Créer le bot sur Discord
1. Va sur https://discord.com/developers/applications
2. Clique **"New Application"** → nom : `Etroqz Bot`
3. Onglet **"Bot"** → clique **"Add Bot"**
4. Clique **"Reset Token"** → copie le token (garde-le secret !)
5. Active **"Message Content Intent"** (tout en bas)
6. Va dans **OAuth2 → URL Generator** :
   - Coche : `bot` + `applications.commands`
   - Permissions : `Send Messages`, `Embed Links`, `Read Message History`
   - Copie le lien et ouvre-le pour inviter le bot sur ton serveur

## 2. Déployer sur Railway (gratuit, 24/7)
1. Crée un compte sur https://railway.app
2. Clique **"New Project"** → **"Deploy from GitHub"**
   - (ou glisse les fichiers directement)
3. Dans ton projet Railway, va dans **"Variables"**
4. Ajoute une variable :
   - Nom : `DISCORD_TOKEN`
   - Valeur : ton token copié à l'étape 1
5. Railway lance le bot automatiquement !

## 3. Utiliser le bot
Une fois le bot en ligne sur ton serveur :

- **`/send`** — Envoie le message dans le salon actuel
- **`/send #salon`** — Envoie dans un salon spécifique
- **`!send`** — Version préfixe (même effet)

⚠️ Seuls les administrateurs peuvent utiliser ces commandes.

## 4. Personnaliser le message
Ouvre `bot.py` et modifie les lignes :
```
EMBED_TITLE = "..."
EMBED_DESCRIPTION = "..."
EMBED_COLOR = 0x7c3aed  # code couleur hex
```
