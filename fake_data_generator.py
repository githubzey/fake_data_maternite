import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta

# Initialize Faker with French localization
fake = Faker("fr_FR")

# Define the column information with Cadrage/Remplissage rules
# (column_name, length, data_type, fill_type)
columns_info = [
    ("Groupage_version_classification", 2, "A", "NA/NA"),
    ("Groupage_num_CMD", 2, "A", "NA/NA"),
    ("Num_GHM", 4, "A", "NA/NA"),
    ("Filler", 1, "A*", "Gauche/Espace"),
    ("Num_version_format_RSS", 3, "A", "NA/NA"),
    ("Groupage_code_retour", 3, "A", "NA/NA"),
    ("Num_FINESS_inscription_ePMSI", 9, "A", "NA/NA"),
    ("Version_format_RUM", 3, "A", "NA/NA"),
    ("Num_RSS", 20, "N", "Droite/Zéro"),
    # ("Num_RSS", 20, "A*", "Gauche/Espace"),
    ("Num_Admin_local_sejour", 20, "N", "Gauche/Espace"),
    # ("Num_Admin_local_sejour",20,'A*','Gauche/Espace'),
    ("Num_RUM", 10, "N", "Droite/Zéro"),
    # ("Num_RUM",10,'A*','Gauche/Espace'),
    ("Date_naissance", 8, "Date", "NA/NA"),
    ("Sexe", 1, "A", "NA/NA"),
    ("Num_unite_medicale", 4, "A*", "Gauche/Espace"),
    ("Type_autorisation_lit_dedie", 2, "A*", "Gauche/Espace"),
    ("Date_entree_unite_medicale", 8, "Date", "NA/NA"),
    ("Mode_entree_unite_medicale", 1, "A", "NA/NA"),
    ("Provenance_mode_entree", 1, "A*", "Gauche/Espace"),
    ("Date_sortie_unite_medicale", 8, "Date", "NA/NA"),
    ("Mode_sortie_unite_medicale", 1, "A", "NA/NA"),
    ("Destination_mode_sortie", 1, "A*", "Gauche/Espace"),
    ("Code_postal_residence", 5, "A", "NA/NA"),
    ("Poids_nouveau_ne_entree_unite_medicale", 4, "N", "Droite/Zéro"),
    ("Age_gestationnel", 2, "N", "Droite/Zéro"),
    ("Date_dernières_regles", 8, "Date", "Gauche/Espace"),
    ("Nombre_seances", 2, "N", "Droite/Zéro"),
    ("Nombre_diagnostics_associes", 2, "N", "Droite/Zéro"),
    ("Nombre_donnees_documentaires", 2, "N", "Droite/Zéro"),
    ("Nombre_zones_actes", 3, "N", "Droite/Zéro"),
    ("Diagnostic_principal", 8, "A*", "Gauche/Espace"),
    ("Diagnostic_relier", 8, "A*", "Gauche/Espace"),
    ("IGS_2", 3, "N", "Droite/Zéro"),
    ("Confirmation_codage_RSS", 1, "A*", "Gauche/Espace"),
    ("Type_machine_radiotherapie", 1, "A*", "Gauche/Espace"),
    ("Type_dosimetrie", 1, "A*", "Gauche/Espace"),
    ("Num_innovation", 15, "A*", "Gauche/Espace"),
    ("Conversion_hospitalisation_complete", 1, "A*", "Gauche/Espace"),
    ("Prise_en_charge_RAAC", 1, "A*", "Gauche/Espace"),
    ("Contexte_patient_surveillance_particuliere", 1, "A*", "Gauche/Espace"),
    ("Administration_produit_RH", 1, "A*", "Gauche/Espace"),
    ("Rescrit_tarifaire", 1, "A*", "Gauche/Espace"),
    ("Categorie_nombre_interventions_totales", 1, "A*", "Gauche/Espace"),
    ("Non_Programme_NP", 1, "A*", "Gauche/Espace"),
    ("Passage_structure_urgences", 1, "A*", "Gauche/Espace"),
    ("Filler_2", 4, "A*", "Gauche/Espace"),
    ("Zone_reservee", 3, "A*", "NA/Espace"),
]

# Function to format data according to Cadrage/Remplissage rules


def format_data(value, length, fill_type):
    if fill_type == "Gauche/Espace":
        return value.ljust(length, " ")
    elif fill_type == "Droite/Zéro":
        return str(value).rjust(length, "0")
    elif fill_type == "NA/NA":
        return value  # No formatting needed if the field is always filled
    elif fill_type == "NA/Espace":
        return value or " " * length  # Fill with spaces if value is missing
    return value


# Function to generate data based on type and length


def generate_fake_data(
    data_type, length, min_age=18, max_age=60, fill_type="Gauche/Espace"
):
    if data_type == "A":
        # Generate Alphanumeric (A-Z, 0-9) values
        return format_data(
            fake.password(length=length + 4, special_chars=False, lower_case=False),
            length,
            fill_type,
        )[:length]
    elif data_type == "A*" or data_type == "A**":
        # Generate Alphanumeric values with spaces for short lengths
        return format_data(
            fake.password(length=length + 4, special_chars=False, lower_case=False),
            length,
            fill_type,
        )[:length]
    elif data_type == "N":
                # Generate numeric values
        return format_data(fake.numerify("#" * length), length, fill_type)
    elif data_type == "Date":
                # Generate a date of birth based on a specified age range
        birth_date = fake.date_of_birth(minimum_age=min_age, maximum_age=max_age)
        # Date formatted as ddmmyyyy
        return format_data(birth_date.strftime("%d%m%Y"), length, fill_type)


# Specific data generation functions for the special columns


def generate_sexe(length, fill_type):
    return format_data(random.choice(["1", "2", "3"]), length, fill_type)


def generate_mode_entree(length, fill_type):
    return format_data(random.choice(["6", "7", "0", "8", "N", "O"]), length, fill_type)

    # Generate Provenance based on mode of entry
def generate_provenance(mode_entree, length, fill_type):
    if mode_entree in ["6", "7", "0"]:
        return format_data(
            random.choice(["1", "R", "2", "3", "4", "6", "7"]), length, fill_type
        )
    return format_data(
        random.choice(["", "1", "R", "2", "3", "4", "6", "7"]), length, fill_type
    )


def generate_mode_sortie(length, fill_type):
    return format_data(random.choice(["6", "7", "0", "8", "9"]), length, fill_type)

    # Generate Destination based on mode of exit
def generate_destination(mode_sortie, length, fill_type):
    if mode_sortie in ["6", "7", "0"]:
        return format_data(
            random.choice(["1", "2", "3", "4", "6", "7"]), length, fill_type
        )
    return format_data(
        random.choice(["", "1", "2", "3", "4", "6", "7"]), length, fill_type
    )


def generate_code_postal(length, fill_type):
    # Generate a number between 00 and 99, format it as a 5-character string
    code_postal = fake.random_number(digits=2, fix_len=True)
    # Convert to string and format
    return format_data(str(code_postal), length, fill_type)


def generate_poids_nouveau_ne(length, fill_type, min_value=1000, max_value=6000):
    return format_data(fake.random_int(min=min_value, max=max_value), length, fill_type)


def generate_age_gestationnel(length, fill_type, min_value=0, max_value=6):
    return format_data(fake.random_int(min=min_value, max=max_value), length, fill_type)


def generate_diagnostic_principal(length, fill_type):
    return format_data(random.choice(["AAA", "BBB", "CCC", "DDD", "EEE"]), length, fill_type)



#######################################################

# Function to generate fake data for a given year
def generate_yearly_fake_data(year, num_records):

    # Define min and max values for columns
    value_ranges = {
        "Date_entree_unite_medicale": {
            "start_date": datetime(year, 1, 1),
            "end_date": datetime(year, 12, 31),
        },
        "Date_sortie_unite_medicale": {"min_days_diff": 1, "max_days_diff": 30},
        "Date_naissance": {"min_age": 18, "max_age": 60},
        "Poids_nouveau_ne_entree_unite_medicale": {"min_value": 1000, "max_value": 6000},
        "Age_gestationnel": {"min_value": 0, "max_value": 6},
        # Add more ranges as needed
    }

    # Initialize the data dictionary
    data = {}

    # Generate data for each column based on information and rules provided
    for column_name, length, data_type, fill_type in columns_info:
        if column_name == "Date_entree_unite_medicale":
            start_date = value_ranges[column_name]["start_date"]
            end_date = value_ranges[column_name]["end_date"]
            date_range = (end_date - start_date).days
            data[column_name] = [
                format_data(
                    (start_date + timedelta(days=random.randint(0, date_range))).strftime(
                        "%d%m%Y"
                    ),
                    length,
                    fill_type,
                )
                for _ in range(num_records)
            ]
        elif column_name == "Num_Admin_local_sejour":
            data[column_name] = [
                generate_fake_data(data_type, length, fill_type=fill_type)
                for _ in range(num_records)
            ]
            data[column_name] = [
                "X" * 7 + data[column_name][_][7:9] + " " * 11 for _ in range(num_records)
            ]

        elif column_name == "Num_RSS":
            data[column_name] = [
                generate_fake_data(data_type, length, fill_type=fill_type)
                for _ in range(num_records)
            ]
            data[column_name] = [
                "0" * 13 + data[column_name][_][13:21] for _ in range(num_records)
            ]

        elif column_name == "Num_RUM":
            data[column_name] = [
                generate_fake_data(data_type, length, fill_type=fill_type)
                for _ in range(num_records)
            ]
            data[column_name] = [
                "0" * 3 + data[column_name][_][3:11] for _ in range(num_records)
            ]
        
        elif column_name == "Date_sortie_unite_medicale":
            min_days_diff = value_ranges[column_name]["min_days_diff"]
            max_days_diff = value_ranges[column_name]["max_days_diff"]
            data[column_name] = [
                format_data(
                    (
                        datetime.strptime(data["Date_entree_unite_medicale"][i], "%d%m%Y")
                        + timedelta(days=random.randint(min_days_diff, max_days_diff))
                    ).strftime("%d%m%Y"),
                    length,
                    fill_type,
                )
                for i in range(num_records)
            ]
        elif column_name == "Date_naissance":
            min_age = value_ranges[column_name]["min_age"]
            max_age = value_ranges[column_name]["max_age"]
            data[column_name] = [
                generate_fake_data(
                    "Date", length, min_age=min_age, max_age=max_age, fill_type=fill_type
                )
                for _ in range(num_records)
            ]
            data[column_name] = [
                "X" * 4 + data[column_name][_][4:9] for _ in range(num_records)
            ]
        elif column_name == "Sexe":
            data[column_name] = [
                generate_sexe(length, fill_type) for _ in range(num_records)
            ]
        elif column_name == "Mode_entree_unite_medicale":
            data[column_name] = [
                generate_mode_entree(length, fill_type) for _ in range(num_records)
            ]
        elif column_name == "Provenance_mode_entree":
            data[column_name] = [
                generate_provenance(
                    data["Mode_entree_unite_medicale"][i], length, fill_type
                )
                for i in range(num_records)
            ]
        elif column_name == "Mode_sortie_unite_medicale":
            data[column_name] = [
                generate_mode_sortie(length, fill_type) for _ in range(num_records)
            ]
        elif column_name == "Destination_mode_sortie":
            data[column_name] = [
                generate_destination(
                    data["Mode_sortie_unite_medicale"][i], length, fill_type
                )
                for i in range(num_records)
            ]
        elif column_name == "Code_postal_residence":
            data[column_name] = [
                generate_code_postal(length, fill_type) for _ in range(num_records)
            ]

        elif column_name == "Diagnostic_principal":
            data[column_name] = [
                generate_diagnostic_principal(length, fill_type) for _ in range(num_records)
            ]

        elif column_name == "Poids_nouveau_ne_entree_unite_medicale":
            min_value = value_ranges[column_name]["min_value"]
            max_value = value_ranges[column_name]["max_value"]
            data[column_name] = [
                generate_poids_nouveau_ne(
                    length, fill_type, min_value=min_value, max_value=max_value
                )
                for _ in range(num_records)
            ]
        elif column_name == "Age_gestationnel":
            min_value = value_ranges[column_name]["min_value"]
            max_value = value_ranges[column_name]["max_value"]
            data[column_name] = [
                generate_age_gestationnel(
                    length, fill_type, min_value=min_value, max_value=max_value
                )
                for _ in range(num_records)
            ]
        else:
            data[column_name] = [
                generate_fake_data(data_type, length, fill_type=fill_type)
                for _ in range(num_records)
            ]


    # Convert to a DataFrame
    df = pd.DataFrame(data)

    # Constant columns
    df["Groupage_version_classification"] = "11"
    df["Filler"] = " "
    df["Filler_2"] = "    "
    df["Num_version_format_RSS"] = "122"
    df["Groupage_code_retour"] = " 00"
    df["Num_FINESS_inscription_ePMSI"] = "350000022"
    df["Version_format_RUM"] = "022"
    df["Sexe"] = "2"
    df["Code_postal_residence"] = "XXXXX"
    df["Date_dernières_regles"] = "        "
    df["Type_autorisation_lit_dedie"] = "  "
    df["Num_innovation"] = "               "
    return df

# An example data for 20 years 
number_of_years = 20
yearly_record_number = 200
deviation = 30

main_df = pd.DataFrame()

for year in range(2024 - number_of_years, 2024):
    df2 = generate_yearly_fake_data(year, random.randrange(yearly_record_number - deviation, yearly_record_number + deviation))
    main_df = pd.concat([main_df, df2])
# Convert the dataframe to csv file
main_df.to_csv("csv_fake_data_twenty_years.csv", index=False, sep=",", encoding="utf-8")
# Convert the dataframe to txt file
test_df = main_df.astype(str).agg(''.join, axis=1)
test_df.to_csv("txt_fake_data_twenty_years.txt", header=False, index=False, sep=",", encoding="utf-8")

print("fake data generated for twenty years")