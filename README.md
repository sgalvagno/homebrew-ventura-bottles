# homebrew-ventura-bottles

Tap Homebrew non-officiel fournissant des **bottles précompilées pour macOS 13 Ventura (Intel x86_64)**.

Homebrew a abandonné le support des bottles pour macOS Ventura fin 2024. Ce tap permet de continuer à installer des packages sans avoir à tout recompiler depuis les sources.

## Prérequis

- macOS 13 Ventura (Intel x86_64)
- [Homebrew](https://brew.sh) installé

## Installation du tap

```bash
brew tap sgalvagno/ventura-bottles
```

## Utilisation

```bash
brew install sgalvagno/ventura-bottles/wget
```

## Packages disponibles

| Package | Version | Source |
|---------|---------|--------|
| wget | 1.25.0 | homebrew-core |

## Variables d'environnement recommandées

```bash
# À ajouter dans ~/.zshrc
export HOMEBREW_NO_AUTO_UPDATE=1
export HOMEBREW_NO_INSTALL_FROM_API=1
```

## Ajouter un package

1. Récupère la formule depuis l'historique de `homebrew-core` au dernier commit supportant Ventura
2. Édite le bloc `bottle do` pour ne garder que la ligne `ventura:` (Intel)
3. Copie le fichier dans `Formula/` et ouvre une PR

## Disclaimer

Ce tap est indépendant du projet Homebrew officiel. Les bottles sont extraites depuis l'historique de `homebrew-core` au moment où macOS 13 Ventura était encore supporté.

## Licence

MIT
