runningstuff
============

marathonstuff.py
----------------
Script Python pour calculer des **ordres de grandeur** d’objectif sur marathon en fonction de ses performances sur des distances plus courtes. Le script permet d’extrapoler des performances sur 10 km au semi et au marathon ainsi que d’extrapoler des performances au semi directement vers le marathon. Le script permet également de faire une estimation VMA sur la base de temps sur 5 km, 10 km, semi (et marathon). Ensuite des estimations de temps sont données pour toutes ces distances en fonction de la VMA. Le script est customisable facilement (chercher CUSTOM) pour être adapté à un profil de coureur.

Mon retour d’expérience sur les formules utilisées (et dérivées de celles que l'on trouve dans les magazines de running) est assez bon. Grosso modo, l'année dernière, je suis parti de ~41'45 sur 10 km (VMA autour de 15.5/16 km/h) pour finir par courir un marathon pas plat (~400 m D+) en 3 h 18 **après un entrainement adéquat** (14 semaines, ciblé 3 h 15/3 h 30). Donc les valeurs ci-dessous me semblent plutôt cohérentes. Cette année, en partant de 40'25 sur 10 km, j'espère faire un peu mieux dans quelques mois :-)

Exemple de sortie :

    Extrapolation semi vers marathon :
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
    Extrapolation 10 km vers semi vers marathon :
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
    Estimations VMA :
    19 m 44 s /  5 km ( 15.20 km/h ) => 16.52 km/h à 16.89 km/h
    40 m 25 s / 10 km ( 14.85 km/h ) => 16.14 km/h à 16.49 km/h
    1 h 30 m 24 s /SM ( 13.94 km/h ) => 15.49 km/h à 16.40 km/h
    3 h 18 m 31 s / M ( 12.75 km/h ) => 15.00 km/h à 15.94 km/h
    VMA vers 10 km :
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
    VMA vers semi :
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
    VMA vers marathon :
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

    15.62 km/h - 3 h 10 m 40 s ( 13.28 km/h ) à 3 h 22 m 36 s ( 12.50 km/h )
    15.97 km/h - 3 h 06 m 30 s ( 13.57 km/h ) à 3 h 18 m 09 s ( 12.78 km/h )
    16.14 km/h - 3 h 04 m 32 s ( 13.72 km/h ) à 3 h 16 m 04 s ( 12.91 km/h )
    16.49 km/h - 3 h 00 m 37 s ( 14.02 km/h ) à 3 h 11 m 54 s ( 13.19 km/h )
    16.52 km/h - 3 h 00 m 17 s ( 14.04 km/h ) à 3 h 11 m 33 s ( 13.22 km/h )
    16.60 km/h - 2 h 59 m 25 s ( 14.11 km/h ) à 3 h 10 m 38 s ( 13.28 km/h )
    16.80 km/h - 2 h 57 m 17 s ( 14.28 km/h ) à 3 h 08 m 22 s ( 13.44 km/h )
    16.89 km/h - 2 h 56 m 20 s ( 14.36 km/h ) à 3 h 07 m 22 s ( 13.51 km/h )
    Vitesses marathon :
    3 h 00 m 00 s - 14.06 km/h
    3 h 01 m 00 s - 13.99 km/h
    3 h 02 m 00 s - 13.91 km/h
    3 h 03 m 00 s - 13.83 km/h
    3 h 04 m 00 s - 13.76 km/h
    3 h 05 m 00 s - 13.68 km/h
    3 h 06 m 00 s - 13.61 km/h
    3 h 07 m 00 s - 13.54 km/h
    3 h 08 m 00 s - 13.47 km/h
    3 h 09 m 00 s - 13.40 km/h
    3 h 10 m 00 s - 13.32 km/h
    3 h 11 m 00 s - 13.25 km/h
    3 h 12 m 00 s - 13.19 km/h
    3 h 13 m 00 s - 13.12 km/h
    3 h 14 m 00 s - 13.05 km/h
    3 h 15 m 00 s - 12.98 km/h
    3 h 16 m 00 s - 12.92 km/h
    3 h 17 m 00 s - 12.85 km/h
    3 h 18 m 00 s - 12.79 km/h
    3 h 19 m 00 s - 12.72 km/h

Il n'y a plus qu'à s'entrainer (durement) après...

D'autres outils suivront prochainement...
-----------------------------------------