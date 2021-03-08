# Cours MPRI 17/11/2020: Reactive Probabilistic Programming

Pour suivre le TP vous aurez besoin de Python 3 et d'installer quelques packages ainsi qu'une branche experimentale de Zelus.

```
git clone https://github.com/INRIA/zelus
cd zelus
git checkout python
opam pin -k path .
cd ..
git clone https://github.com/gbdrt/2020-mpri-rppl.git
cd 2020-mpri-rppl
pip install -r requirements.txt
```

Le TP se présente sous la forme d'un notebook jupyter.
Vous pouvez demarrer le server jupyter en executant la commande suivante depuis la racine du dépot:

```
jupyter notebook
```

Cliquez ensuite sur `cours_rppl.ipynb` pour démarrer le TP.
La solution est dans `cours_rppl_solution.ipnyb`