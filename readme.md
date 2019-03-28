# Presentator #

Presentator permet de transformer un fichier markdown en présentation prête à l'emploi, qu'on lance dans un navigateur, et qui n'a rien à reprocher aux machines de guerre type P\*\*\*\*r Po\*\*t ou K\*\*\*\*te.

On créera d'abord un fichier texte, dans lequel on séparera chaque slide par un séparateur `---`

``` markdown
## Le contenu de ma page 1 ##

---

Le contenu de ma page 2

--- 

Ma page 3 est *très* élégante avec tous ces **styles**
```


Puis, une fois fait cela, on lance le script python, dans son terminal par exemple

``` bash
$ python3 presentator.py
```

Et on doit se trouver avec un fichier HTML tout beau, que l'on lance dans son navigateur. Si on a Firefox, on peut appuyer sur F11 (sur Linux) pour être en full-screen comme dans la vraie vie des présentations. Et là, on clique partout sur l'écran pour passer de slide en slide.

## Améliorations ##

- Encore des aspects visuels à améliorer (CSS)

