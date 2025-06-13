<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9b1b247a8d0f1736459e0e9ede0d9c92",
  "translation_date": "2025-06-12T11:35:37+00:00",
  "source_file": "getting_started/markdown-only-mode.md",
  "language_code": "fr"
}
-->
# Utilisation du mode Markdown uniquement

## Introduction
Le mode Markdown uniquement est conçu pour traduire uniquement le contenu Markdown de votre projet. Ce mode contourne le processus de traduction des images et se concentre uniquement sur le contenu textuel, ce qui le rend idéal dans les cas où la traduction des images n’est pas nécessaire ou lorsque les variables d’environnement requises pour la vision par ordinateur ne sont pas configurées.

## Quand l’utiliser
- Lorsque les variables d’environnement liées à la vision par ordinateur ne sont pas configurées.
- Lorsque vous souhaitez traduire uniquement le contenu textuel sans mettre à jour les liens des images.
- Lorsque l’utilisateur le spécifie explicitement avec l’option de ligne de commande `-md`.

## Comment l’activer
Pour activer le mode Markdown uniquement, utilisez l’option `-md` dans votre commande. Par exemple :
```
translate -l "ko" -md
```

Ou si les variables d’environnement liées à la vision par ordinateur ne sont pas configurées. Exécuter `translate -l "ko"` basculera automatiquement en mode Markdown uniquement.

```
translate -l "ko"
```

Cette commande traduit le contenu Markdown en coréen et met à jour les liens des images vers leurs chemins originaux, au lieu de les modifier pour des chemins d’images traduits.

## Fonctionnement
En mode Markdown uniquement :
- Le processus de traduction ignore l’étape de traduction des images.
- Les liens des images dans le Markdown restent inchangés, pointant vers leurs chemins d’origine.

## Exemples
### Avant
```markdown
![Image](../../../translated_images/image.aa98bae4d78871bb3b23ac9f938ff86539da4cd6fb4c52dafedc4665135c3d61.fr.png)
```
### Après utilisation du mode Markdown uniquement
```markdown
![Image](../../../translated_images/image.fc8708ffe1e1ca12c38822b1a382726da4b232025d1daa8a50ab75c8635d0c4a.fr.png)
```

## Résolution des problèmes
- Assurez-vous que l’option `-md` est correctement spécifiée dans la commande.
- Vérifiez qu’aucune variable d’environnement liée à la vision par ordinateur ne perturbe le processus.

## Conclusion
Le mode Markdown uniquement offre une manière simplifiée de traduire le contenu textuel sans modifier les liens des images. Il est particulièrement utile lorsque la traduction des images n’est pas nécessaire ou lorsque vous travaillez dans des environnements sans configuration de vision par ordinateur.

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçons d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle humaine est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l'utilisation de cette traduction.