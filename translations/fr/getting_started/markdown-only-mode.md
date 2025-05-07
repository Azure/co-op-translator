<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9b1b247a8d0f1736459e0e9ede0d9c92",
  "translation_date": "2025-05-06T17:43:46+00:00",
  "source_file": "getting_started/markdown-only-mode.md",
  "language_code": "fr"
}
-->
# Mode Markdown uniquement

## Introduction  
Le mode Markdown uniquement est conçu pour traduire uniquement le contenu Markdown de votre projet. Ce mode contourne le processus de traduction des images et se concentre exclusivement sur le contenu textuel, ce qui le rend idéal dans les cas où la traduction des images n’est pas nécessaire ou lorsque les variables d’environnement requises pour la Vision par Ordinateur ne sont pas configurées.

## Quand l’utiliser  
- Lorsque les variables d’environnement liées à la Vision par Ordinateur ne sont pas configurées.  
- Lorsque vous souhaitez traduire uniquement le contenu textuel sans mettre à jour les liens des images.  
- Lorsque l’utilisateur le spécifie explicitement via l’option `-md` en ligne de commande.

## Comment l’activer  
Pour activer le mode Markdown uniquement, utilisez l’option `-md` dans votre commande. Par exemple :  
```
translate -l "ko" -md
```

Ou si les variables d’environnement liées à la Vision par Ordinateur ne sont pas configurées. L’exécution de `translate -l "ko"` basculera automatiquement en mode Markdown uniquement.

```
translate -l "ko"
```

Cette commande traduit le contenu Markdown en coréen et conserve les liens des images vers leurs chemins d’origine, au lieu de les modifier pour pointer vers des chemins d’images traduites.

## Comportement  
En mode Markdown uniquement :  
- Le processus de traduction ignore l’étape de traduction des images.  
- Les liens des images dans le Markdown restent inchangés, pointant vers leurs chemins d’origine.

## Exemples  
### Avant  
```markdown
![Image](../../../getting_started/translated/path/to/image.png)
```  
### Après utilisation du mode Markdown uniquement  
```markdown
![Image](../../../getting_started/original/path/to/image.png)
```

## Dépannage  
- Assurez-vous que l’option `-md` est correctement spécifiée dans la commande.  
- Vérifiez qu’aucune variable d’environnement liée à la Vision par Ordinateur ne perturbe le processus.

## Conclusion  
Le mode Markdown uniquement offre une méthode simplifiée pour traduire le contenu textuel sans modifier les liens des images. Il est particulièrement utile lorsque la traduction des images est superflue ou lorsque l’environnement ne dispose pas de la configuration Vision par Ordinateur.

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l'utilisation de cette traduction.