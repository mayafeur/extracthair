Ce script classe les noms de salons de coiffure par fréquence.

Le fichier *annuaire.csv* doit provenir de la base [SIRENE](https://annuaire-entreprises.data.gouv.fr/export-sirene) de l'administration française ; j'ai choisi comme seuls critères le code NAP/APE **96.02A** et les entreprises en activité pour un premier export, puis j'ai fait un second export avec seulement les entreprises cessées et j'ai fusionné les deux fichiers.

Le script crée deux fichiers :
 - *occurences.txt* liste tous les noms de salons par fréquence d'occurence décroissante ;
 - *occurences_motscles.txt* filtre cette liste en fonction de mots clés prédéfinis par la liste `MOTS_CLES` ;
 - la variable `OCCURENCES_MIN` permet de filtrer uniquement les noms qui réapparaissent un certain nombre de fois.

Les noms sont extraits depuis le CSV :
 - à partir des colonnes *denominationUsuelleEtablissement* et *denominationUniteLegale* ;
 - les apostrophes sont retirées à cause de l'inconsistance de leur usage.

Limites :
 - la présence ou non des déterminants peut fausser un peu le comptage ;
 - il est probable que certains salons aient un nom de devanture différent de ce qui est déclaré légalement ;
 - le script ne gère pour le moment pas d'autres territoires francophones.