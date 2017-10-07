runningstuff
============

vmaestim.py
----------------
Coming very soon :-)

marathontab.py
----------------
Script Python pour calculer des **ordres de grandeur** d’objectif sur marathon en fonction de ses performances sur des distances plus courtes. Le script permet d’extrapoler des performances sur 10 km au semi et au marathon ainsi que d’extrapoler des performances au semi directement vers le marathon. Le script donne également des estimations de temps pour toutes ces distances en fonction de la VMA (vmaestim.py, ci-dessus, permet d'estimer sa VMA).

Mon retour d’expérience sur les formules utilisées (et dérivées de celles que l'on trouve dans les magazines de running) est assez bon. Grosso modo, en 2016-17, je suis parti de ~41'45 sur 10 km (VMA autour de 15.5/16 km/h) pour finir par courir un marathon pas plat (~400 m D+) en 3 h 18 **après un entrainement adéquat** (14 semaines, ciblé 3 h 15/3 h 30) - avec un test sur semi en 1 h 31'48, 5 semaines avant le marathon. Donc les valeurs ci-dessous me semblent plutôt cohérentes. En 2017/18, en partant de 40'25 sur 10 km, j'espère faire un peu mieux du coup... We'll see...

Exemple de sortie (tronquée pour raccourcir ce README, la sortie complète est [ici](marathontab.ref)) :

    Extrapolation semi vers marathon :
    ...
    1 h 25 m 00 s - 14.82 km/h ~> 2 h 58 m 30 s - 14.18 km/h
    1 h 26 m 00 s - 14.65 km/h ~> 3 h 00 m 36 s - 14.02 km/h
    1 h 27 m 00 s - 14.48 km/h ~> 3 h 02 m 42 s - 13.86 km/h
    1 h 28 m 00 s - 14.32 km/h ~> 3 h 04 m 48 s - 13.70 km/h
    1 h 29 m 00 s - 14.16 km/h ~> 3 h 06 m 54 s - 13.55 km/h
    1 h 30 m 00 s - 14.00 km/h ~> 3 h 09 m 00 s - 13.40 km/h
    1 h 31 m 00 s - 13.85 km/h ~> 3 h 11 m 06 s - 13.25 km/h
    1 h 32 m 00 s - 13.70 km/h ~> 3 h 13 m 12 s - 13.10 km/h
    1 h 33 m 00 s - 13.55 km/h ~> 3 h 15 m 18 s - 12.96 km/h
    1 h 34 m 00 s - 13.40 km/h ~> 3 h 17 m 24 s - 12.83 km/h
    1 h 35 m 00 s - 13.26 km/h ~> 3 h 19 m 30 s - 12.69 km/h
    1 h 36 m 00 s - 13.12 km/h ~> 3 h 21 m 36 s - 12.56 km/h
    1 h 37 m 00 s - 12.99 km/h ~> 3 h 23 m 42 s - 12.43 km/h
    1 h 38 m 00 s - 12.86 km/h ~> 3 h 25 m 48 s - 12.30 km/h
    1 h 39 m 00 s - 12.73 km/h ~> 3 h 27 m 54 s - 12.18 km/h
    1 h 40 m 00 s - 12.60 km/h ~> 3 h 30 m 00 s - 12.06 km/h
    1 h 41 m 00 s - 12.48 km/h ~> 3 h 32 m 06 s - 11.94 km/h
    1 h 42 m 00 s - 12.35 km/h ~> 3 h 34 m 12 s - 11.82 km/h
    1 h 43 m 00 s - 12.23 km/h ~> 3 h 36 m 18 s - 11.70 km/h
    1 h 44 m 00 s - 12.12 km/h ~> 3 h 38 m 24 s - 11.59 km/h
    1 h 45 m 00 s - 12.00 km/h ~> 3 h 40 m 30 s - 11.48 km/h
    ...
    Extrapolation 10 km vers semi vers marathon :
    ...
    35 m 00 s - 17.14 km/h ~> 1 h 17 m 10 s - 16.33 km/h ~> 2 h 42 m 03 s - 15.62 km/h
    35 m 30 s - 16.90 km/h ~> 1 h 18 m 16 s - 16.10 km/h ~> 2 h 44 m 21 s - 15.40 km/h
    36 m 00 s - 16.67 km/h ~> 1 h 19 m 22 s - 15.88 km/h ~> 2 h 46 m 40 s - 15.19 km/h
    36 m 30 s - 16.44 km/h ~> 1 h 20 m 28 s - 15.66 km/h ~> 2 h 48 m 58 s - 14.98 km/h
    37 m 00 s - 16.22 km/h ~> 1 h 21 m 35 s - 15.44 km/h ~> 2 h 51 m 19 s - 14.78 km/h
    37 m 30 s - 16.00 km/h ~> 1 h 22 m 41 s - 15.24 km/h ~> 2 h 53 m 38 s - 14.58 km/h
    38 m 00 s - 15.79 km/h ~> 1 h 23 m 47 s - 15.04 km/h ~> 2 h 55 m 56 s - 14.39 km/h
    38 m 30 s - 15.58 km/h ~> 1 h 24 m 53 s - 14.84 km/h ~> 2 h 58 m 15 s - 14.20 km/h
    39 m 00 s - 15.38 km/h ~> 1 h 25 m 59 s - 14.65 km/h ~> 3 h 00 m 33 s - 14.02 km/h
    39 m 30 s - 15.19 km/h ~> 1 h 27 m 05 s - 14.47 km/h ~> 3 h 02 m 52 s - 13.84 km/h
    40 m 00 s - 15.00 km/h ~> 1 h 28 m 12 s - 14.29 km/h ~> 3 h 05 m 13 s - 13.67 km/h
    40 m 30 s - 14.81 km/h ~> 1 h 29 m 18 s - 14.11 km/h ~> 3 h 07 m 31 s - 13.50 km/h
    41 m 00 s - 14.63 km/h ~> 1 h 30 m 24 s - 13.94 km/h ~> 3 h 09 m 50 s - 13.34 km/h
    41 m 30 s - 14.46 km/h ~> 1 h 31 m 30 s - 13.77 km/h ~> 3 h 12 m 09 s - 13.18 km/h
    42 m 00 s - 14.29 km/h ~> 1 h 32 m 36 s - 13.61 km/h ~> 3 h 14 m 27 s - 13.02 km/h
    42 m 30 s - 14.12 km/h ~> 1 h 33 m 42 s - 13.45 km/h ~> 3 h 16 m 46 s - 12.87 km/h
    43 m 00 s - 13.95 km/h ~> 1 h 34 m 48 s - 13.29 km/h ~> 3 h 19 m 04 s - 12.72 km/h
    43 m 30 s - 13.79 km/h ~> 1 h 35 m 55 s - 13.14 km/h ~> 3 h 21 m 25 s - 12.57 km/h
    44 m 00 s - 13.64 km/h ~> 1 h 37 m 01 s - 12.99 km/h ~> 3 h 23 m 44 s - 12.43 km/h
    44 m 30 s - 13.48 km/h ~> 1 h 38 m 07 s - 12.84 km/h ~> 3 h 26 m 02 s - 12.29 km/h
    45 m 00 s - 13.33 km/h ~> 1 h 39 m 13 s - 12.70 km/h ~> 3 h 28 m 21 s - 12.15 km/h
    45 m 30 s - 13.19 km/h ~> 1 h 40 m 19 s - 12.56 km/h ~> 3 h 30 m 39 s - 12.02 km/h
    46 m 00 s - 13.04 km/h ~> 1 h 41 m 25 s - 12.42 km/h ~> 3 h 32 m 58 s - 11.89 km/h
    46 m 30 s - 12.90 km/h ~> 1 h 42 m 31 s - 12.29 km/h ~> 3 h 35 m 17 s - 11.76 km/h
    47 m 00 s - 12.77 km/h ~> 1 h 43 m 38 s - 12.16 km/h ~> 3 h 37 m 37 s - 11.63 km/h
    47 m 30 s - 12.63 km/h ~> 1 h 44 m 44 s - 12.03 km/h ~> 3 h 39 m 56 s - 11.51 km/h
    48 m 00 s - 12.50 km/h ~> 1 h 45 m 50 s - 11.91 km/h ~> 3 h 42 m 15 s - 11.39 km/h
    48 m 30 s - 12.37 km/h ~> 1 h 46 m 56 s - 11.78 km/h ~> 3 h 44 m 33 s - 11.27 km/h
    49 m 00 s - 12.24 km/h ~> 1 h 48 m 02 s - 11.66 km/h ~> 3 h 46 m 52 s - 11.16 km/h
    49 m 30 s - 12.12 km/h ~> 1 h 49 m 08 s - 11.55 km/h ~> 3 h 49 m 10 s - 11.05 km/h
    50 m 00 s - 12.00 km/h ~> 1 h 50 m 15 s - 11.43 km/h ~> 3 h 51 m 31 s - 10.94 km/h
    ...
    VMA vers 10 km :
    10.00 km/h - 1 h 05 m 13 s ( 9.20 km/h ) à 1 h 06 m 40 s ( 9.00 km/h )
    10.50 km/h - 1 h 02 m 06 s ( 9.66 km/h ) à 1 h 03 m 29 s ( 9.45 km/h )
    11.00 km/h - 59 m 17 s ( 10.12 km/h ) à 1 h 00 m 36 s ( 9.90 km/h )
    11.50 km/h - 56 m 42 s ( 10.58 km/h ) à 57 m 58 s ( 10.35 km/h )
    12.00 km/h - 54 m 20 s ( 11.04 km/h ) à 55 m 33 s ( 10.80 km/h )
    12.50 km/h - 52 m 10 s ( 11.50 km/h ) à 53 m 20 s ( 11.25 km/h )
    13.00 km/h - 50 m 10 s ( 11.96 km/h ) à 51 m 16 s ( 11.70 km/h )
    13.50 km/h - 48 m 18 s ( 12.42 km/h ) à 49 m 22 s ( 12.15 km/h )
    14.00 km/h - 46 m 35 s ( 12.88 km/h ) à 47 m 37 s ( 12.60 km/h )
    14.50 km/h - 44 m 58 s ( 13.34 km/h ) à 45 m 58 s ( 13.05 km/h )
    15.00 km/h - 43 m 28 s ( 13.80 km/h ) à 44 m 26 s ( 13.50 km/h )
    15.50 km/h - 42 m 04 s ( 14.26 km/h ) à 43 m 00 s ( 13.95 km/h )
    16.00 km/h - 40 m 45 s ( 14.72 km/h ) à 41 m 40 s ( 14.40 km/h )
    16.50 km/h - 39 m 31 s ( 15.18 km/h ) à 40 m 24 s ( 14.85 km/h )
    17.00 km/h - 38 m 21 s ( 15.65 km/h ) à 39 m 12 s ( 15.31 km/h )
    17.50 km/h - 37 m 16 s ( 16.10 km/h ) à 38 m 05 s ( 15.75 km/h )
    18.00 km/h - 36 m 13 s ( 16.57 km/h ) à 37 m 02 s ( 16.20 km/h )
    18.50 km/h - 35 m 15 s ( 17.02 km/h ) à 36 m 02 s ( 16.65 km/h )
    19.00 km/h - 34 m 19 s ( 17.48 km/h ) à 35 m 05 s ( 17.10 km/h )
    19.50 km/h - 33 m 26 s ( 17.95 km/h ) à 34 m 11 s ( 17.55 km/h )
    VMA vers semi :
    10.00 km/h - 2 h 20 m 00 s ( 9.00 km/h ) à 2 h 28 m 14 s ( 8.50 km/h )
    10.50 km/h - 2 h 13 m 19 s ( 9.45 km/h ) à 2 h 21 m 10 s ( 8.93 km/h )
    11.00 km/h - 2 h 07 m 16 s ( 9.90 km/h ) à 2 h 14 m 45 s ( 9.35 km/h )
    11.50 km/h - 2 h 01 m 44 s ( 10.35 km/h ) à 2 h 08 m 54 s ( 9.78 km/h )
    12.00 km/h - 1 h 56 m 39 s ( 10.80 km/h ) à 2 h 03 m 31 s ( 10.20 km/h )
    12.50 km/h - 1 h 52 m 00 s ( 11.25 km/h ) à 1 h 58 m 35 s ( 10.63 km/h )
    13.00 km/h - 1 h 47 m 41 s ( 11.70 km/h ) à 1 h 54 m 01 s ( 11.05 km/h )
    13.50 km/h - 1 h 43 m 42 s ( 12.15 km/h ) à 1 h 49 m 48 s ( 11.48 km/h )
    14.00 km/h - 1 h 40 m 00 s ( 12.60 km/h ) à 1 h 45 m 52 s ( 11.90 km/h )
    14.50 km/h - 1 h 36 m 33 s ( 13.05 km/h ) à 1 h 42 m 13 s ( 12.33 km/h )
    15.00 km/h - 1 h 33 m 20 s ( 13.50 km/h ) à 1 h 38 m 49 s ( 12.75 km/h )
    15.50 km/h - 1 h 30 m 19 s ( 13.95 km/h ) à 1 h 35 m 38 s ( 13.18 km/h )
    16.00 km/h - 1 h 27 m 30 s ( 14.40 km/h ) à 1 h 32 m 38 s ( 13.60 km/h )
    16.50 km/h - 1 h 24 m 50 s ( 14.85 km/h ) à 1 h 29 m 50 s ( 14.03 km/h )
    17.00 km/h - 1 h 22 m 21 s ( 15.30 km/h ) à 1 h 27 m 11 s ( 14.45 km/h )
    17.50 km/h - 1 h 20 m 00 s ( 15.75 km/h ) à 1 h 24 m 42 s ( 14.88 km/h )
    18.00 km/h - 1 h 17 m 46 s ( 16.20 km/h ) à 1 h 22 m 21 s ( 15.30 km/h )
    18.50 km/h - 1 h 15 m 40 s ( 16.65 km/h ) à 1 h 20 m 07 s ( 15.73 km/h )
    19.00 km/h - 1 h 13 m 41 s ( 17.10 km/h ) à 1 h 18 m 01 s ( 16.15 km/h )
    19.50 km/h - 1 h 11 m 47 s ( 17.55 km/h ) à 1 h 16 m 01 s ( 16.58 km/h )
    VMA vers marathon :
    10.00 km/h - 4 h 57 m 50 s ( 8.50 km/h ) à 5 h 16 m 27 s ( 8.00 km/h )
    10.50 km/h - 4 h 43 m 39 s ( 8.93 km/h ) à 5 h 01 m 23 s ( 8.40 km/h )
    11.00 km/h - 4 h 30 m 46 s ( 9.35 km/h ) à 4 h 47 m 41 s ( 8.80 km/h )
    11.50 km/h - 4 h 18 m 59 s ( 9.78 km/h ) à 4 h 35 m 11 s ( 9.20 km/h )
    12.00 km/h - 4 h 08 m 12 s ( 10.20 km/h ) à 4 h 23 m 43 s ( 9.60 km/h )
    12.50 km/h - 3 h 58 m 16 s ( 10.63 km/h ) à 4 h 13 m 10 s ( 10.00 km/h )
    13.00 km/h - 3 h 49 m 06 s ( 11.05 km/h ) à 4 h 03 m 25 s ( 10.40 km/h )
    13.50 km/h - 3 h 40 m 37 s ( 11.48 km/h ) à 3 h 54 m 24 s ( 10.80 km/h )
    14.00 km/h - 3 h 32 m 44 s ( 11.90 km/h ) à 3 h 46 m 02 s ( 11.20 km/h )
    14.50 km/h - 3 h 25 m 24 s ( 12.33 km/h ) à 3 h 38 m 14 s ( 11.60 km/h )
    15.00 km/h - 3 h 18 m 33 s ( 12.75 km/h ) à 3 h 30 m 58 s ( 12.00 km/h )
    15.50 km/h - 3 h 12 m 09 s ( 13.18 km/h ) à 3 h 24 m 10 s ( 12.40 km/h )
    16.00 km/h - 3 h 06 m 09 s ( 13.60 km/h ) à 3 h 17 m 47 s ( 12.80 km/h )
    16.50 km/h - 3 h 00 m 30 s ( 14.03 km/h ) à 3 h 11 m 47 s ( 13.20 km/h )
    17.00 km/h - 2 h 55 m 12 s ( 14.45 km/h ) à 3 h 06 m 09 s ( 13.60 km/h )
    17.50 km/h - 2 h 50 m 11 s ( 14.88 km/h ) à 3 h 00 m 50 s ( 14.00 km/h )
    18.00 km/h - 2 h 45 m 28 s ( 15.30 km/h ) à 2 h 55 m 48 s ( 14.40 km/h )
    18.50 km/h - 2 h 40 m 59 s ( 15.73 km/h ) à 2 h 51 m 03 s ( 14.80 km/h )
    19.00 km/h - 2 h 36 m 45 s ( 16.15 km/h ) à 2 h 46 m 33 s ( 15.20 km/h )
    19.50 km/h - 2 h 32 m 44 s ( 16.58 km/h ) à 2 h 42 m 17 s ( 15.60 km/h )

Il n'y a plus qu'à s'entrainer (durement) après...

D'autres outils suivront prochainement...
-----------------------------------------
