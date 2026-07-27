#!/usr/bin/env python3

# https://annuaire-entreprises.data.gouv.fr/export-sirene
# Code NAP/APE 96.02A – Coiffure

import csv

MOTS_CLES = ["HAIR", "MECHE", "TIF", "DECOIF"]
OCCURENCES_MIN = 5

occurences_par_nom = {}
with open("annuaire.csv", newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        for colonne in ["denominationUsuelleEtablissement", "denominationUniteLegale"]:
            nom = row[colonne]
            nom = nom.replace("'", " ")
            nom = nom.replace("SARL", "")
            nom = nom.strip()
            if not nom or nom == "[ND]":
                continue
            if nom in occurences_par_nom:
                occurences_par_nom[nom] += 1
            else:
                occurences_par_nom[nom] = 1

occurences_sorted = sorted(occurences_par_nom.items(), key=lambda x: x[1], reverse=True)
occurences_sorted = [(x, y) for x, y in occurences_sorted if y >= OCCURENCES_MIN]

with open("occurences.txt", "w") as f:
    for nom, occurences in occurences_sorted:
        f.write(nom + "\t" + str(occurences) + "\n")

with open("occurences_motscles.txt", "w") as f:
    for nom, occurences in occurences_sorted:
        for mot_cle in MOTS_CLES:
            if mot_cle in nom:
                f.write(nom + "\t" + str(occurences) + "\n")
                break
