# Presentator #

Presentator permet de transformer un fichier markdown en présentation prête à l'emploi, qu'on lance dans un navigateur, et qui n'a rien à reprocher aux machines de guerre type P\*\*\*\*r Po\*\*t ou K\*\*\*\*te.

## Créer le contenu ##

On créera d'abord un fichier texte, dans lequel on séparera chaque slide par un séparateur `---`

``` markdown
## Le contenu de ma page 1 ##

---

Le contenu de ma page 2

--- 

Ma page 3 est *très* élégante avec tous ces **styles**

---
```

> On veillera à bien fermer la dernière section/slide avec un séparateur

## Couleurs ##

Pour définir des couleurs de polices et de fond, on ajoutera des instructions `background` et `color` dans chaque slide. Par défaut, le fond a une valeur de `#000000` et les textes `#FFFFFF`.

``` markdown
background: #FFCC00
color: #0000FF
{Le contenu qui sera affiché dans la page}
---
background: blue
color: green
{Contenu}
---
```

## Création du fichier html ##

Puis, une fois fait cela, on lance le script python, dans son terminal par exemple

``` bash
$ python3 presentator.py
```

Et on doit se trouver avec un fichier HTML `index.html` tout beau, que l'on lance dans son navigateur. Si on a Firefox, on peut appuyer sur F11 (sur Linux) pour être en full-screen comme dans la vraie vie des présentations. Et là, on clique partout sur l'écran pour passer de slide en slide.

## Exemple vivant ##

https://www.thomasguesnon.net/assets/files/convivialite_low_tech_design_presentation/

[Le fichier de base](https://www.thomasguesnon.net/assets/files/convivialite_low_tech_design_presentation/presentation.md)

## Améliorations ##

- ~~Encore des aspects visuels à améliorer (CSS)~~
- ~~possibilité de spécifier une couleur de fond pour une slide~~
- Revenir au début du slideshow, une fois arrivé au bout
