import pandas as pd

# Lire les CSVs en forçant toutes les colonnes en texte
df_2023 = pd.read_csv("csv_fake_data_for_2023.csv", dtype=str)
df_2024 = pd.read_csv("csv_fake_data_for_2024.csv", dtype=str)

# Concaténer les deux DataFrames
multi_center_year_df = pd.concat([df_2023, df_2024], ignore_index=True)

# Sauvegarder en CSV en gardant les chaînes
multi_center_year_df.to_csv("multi_center_year_df.csv", index=False, sep=",", encoding="utf-8")

# Convertir en fichier TXT (chaque ligne = concaténation des colonnes)
test_df = multi_center_year_df.astype(str).agg(''.join, axis=1)
test_df.to_csv("multi_center_year_df.txt", header=False, index=False, sep=",", encoding="utf-8")

print("fake multi center year data generated")
