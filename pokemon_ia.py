import pandas as pa
import numpy as np
import os

listeFichiers = os.listdir("C:/Users/benoi/OneDrive/Bureau/Cours/IA_Avec_Pokemon/IA_Avec_Pokemon/datas")

nosPokemons = pa.read_csv("C:/Users/benoi/OneDrive/Bureau/Cours/IA_Avec_Pokemon/IA_Avec_Pokemon/datas/pokedex.csv")



print(nosPokemons.columns.values)
nosPokemons['LEGENDAIRE'] = (nosPokemons['LEGENDAIRE'] == "VRAI").astype(int)
nosPokemons["NOM"][62] = "Colossinge"
print(nosPokemons["NOM"][62])