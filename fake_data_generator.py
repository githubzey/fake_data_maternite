import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta
import yaml
path_config = "config.yaml"
with open(path_config, 'r') as file:
    configs = yaml.safe_load(file)



# Initialize Faker with French localization
fake = Faker("fr_FR")
configs["liste_num_CMD"]
# liste_columns_info
liste_num_CMD = configs["liste_num_CMD"]
liste_num_GHM = configs["liste_num_GHM"]
liste_grp_code_retour = configs["liste_grp_code_retour"]
liste_Num_FINESS_inscription_ePMSI = configs["liste_Num_FINESS_inscription_ePMSI"]
liste_sexe = configs["liste_sexe"]
liste_Type_autorisation_lit_dedie = configs["liste_Type_autorisation_lit_dedie"]
liste_Mode_entree_unite_medicale = configs["liste_Mode_entree_unite_medicale"]
liste_Provenance_mode_entree = configs["liste_Provenance_mode_entree"]
liste_Mode_sortie_unite_medicale = configs["liste_Mode_sortie_unite_medicale"]
liste_Destination_mode_sortie = configs["liste_Destination_mode_sortie"]
liste_Code_postal_residence = configs["liste_Code_postal_residence"]
liste_Diagnostic_principal = configs["liste_Diagnostic_principal"]
liste_Diagnostic_relier = configs["liste_Diagnostic_relier"]
liste_Confirmation_codage_RSS = configs["liste_Confirmation_codage_RSS"]
liste_Type_machine_radiotherapie = configs["liste_Type_machine_radiotherapie"]
liste_Conversion_hospitalisation_complete = configs["liste_Conversion_hospitalisation_complete"]
liste_Prise_en_charge_RAAC = configs["liste_Prise_en_charge_RAAC"]
liste_Contexte_patient_surveillance_particuliere = configs["liste_Contexte_patient_surveillance_particuliere"]
liste_Administration_produit_RH = configs["liste_Administration_produit_RH"]
liste_Rescrit_tarifaire = configs["liste_Rescrit_tarifaire"]
liste_Categorie_nombre_interventions_totales = configs["liste_Categorie_nombre_interventions_totales"]
liste_Non_Programme_NP = configs["liste_Non_Programme_NP"]
liste_Passage_structure_urgences = configs["liste_Passage_structure_urgences"]

# da
liste_da = configs["liste_da"]
# dad 
liste_dad = configs["liste_dad"]

# za_columns_info
liste_Code_CCAM = configs["liste_Code_CCAM"]
liste_Extension_PMSI = configs["liste_Extension_PMSI"]
liste_Phase = configs["liste_Phase"]
liste_Activite = configs["liste_Activite"]
liste_Extension_documentaire = configs["liste_Extension_documentaire"]
liste_Modificateurs = configs["liste_Modificateurs"]
liste_Remboursement_exceptionnel = configs["liste_Remboursement_exceptionnel"]
liste_Association_non_prevue = configs["liste_Association_non_prevue"]

# if not a liste
not_liste = configs["not_liste"]

# Define the column information with Cadrage/Remplissage rules
# (column_name, length, data_type, fill_type)
columns_info = [
    ("Groupage_version_classification", 2, "A", "NA/NA", not_liste),
    ("Groupage_num_CMD", 2, "A", "NA/NA", liste_num_CMD),
    ("Num_GHM", 4, "A", "NA/NA", liste_num_GHM),
    ("Filler", 1, "A*", "Gauche/Espace", not_liste),
    ("Num_version_format_RSS", 3, "A", "NA/NA", not_liste),
    ("Groupage_code_retour", 3, "A", "NA/NA", liste_grp_code_retour),
    ("Num_FINESS_inscription_ePMSI", 9, "A", "NA/NA", liste_Num_FINESS_inscription_ePMSI),
    ("Version_format_RUM", 3, "A", "NA/NA", not_liste),
    ("Num_RSS", 20, "N", "Droite/Zéro", not_liste),
    # ("Num_RSS", 20, "A*", "Gauche/Espace"),
    ("Num_Admin_local_sejour", 20, "N", "Gauche/Espace", not_liste),
    # ("Num_Admin_local_sejour",20,'A*','Gauche/Espace', not_liste),
    ("Num_RUM", 10, "N", "Droite/Zéro", not_liste),
    # ("Num_RUM",10,'A*','Gauche/Espace', not_liste),
    ("Date_naissance", 8, "Date", "NA/NA", not_liste),
    ("Sexe", 1, "A", "NA/NA", liste_sexe),
    ("Num_unite_medicale", 4, "A*", "Gauche/Espace", not_liste),
    ("Type_autorisation_lit_dedie", 2, "A*", "Gauche/Espace", liste_Type_autorisation_lit_dedie),
    ("Date_entree_unite_medicale", 8, "Date", "NA/NA", not_liste),
    ("Mode_entree_unite_medicale", 1, "A", "NA/NA", liste_Mode_entree_unite_medicale),
    ("Provenance_mode_entree", 1, "A*", "Gauche/Espace", liste_Provenance_mode_entree),
    ("Date_sortie_unite_medicale", 8, "Date", "NA/NA", not_liste),
    ("Mode_sortie_unite_medicale", 1, "A", "NA/NA", liste_Mode_sortie_unite_medicale),
    ("Destination_mode_sortie", 1, "A*", "Gauche/Espace", liste_Destination_mode_sortie),
    ("Code_postal_residence", 5, "A", "NA/NA", liste_Code_postal_residence),
    ("Poids_nouveau_ne_entree_unite_medicale", 4, "N", "Droite/Zéro", not_liste),
    ("Age_gestationnel", 2, "N", "Droite/Zéro", not_liste),
    ("Date_dernières_regles", 8, "Date", "Gauche/Espace", not_liste),
    ("Nombre_seances", 2, "N", "Droite/Zéro", not_liste),
    ("Nombre_diagnostics_associes", 2, "N", "Droite/Zéro", not_liste),
    ("Nombre_donnees_documentaires", 2, "N", "Droite/Zéro", not_liste),
    ("Nombre_zones_actes", 3, "N", "Droite/Zéro", not_liste),
    ("Diagnostic_principal", 8, "A*", "Gauche/Espace", liste_Diagnostic_principal),
    ("Diagnostic_relier", 8, "A*", "Gauche/Espace", liste_Diagnostic_relier),
    ("IGS_2", 3, "N", "Droite/Zéro", not_liste),
    ("Confirmation_codage_RSS", 1, "A*", "Gauche/Espace", liste_Confirmation_codage_RSS),
    ("Type_machine_radiotherapie", 1, "A*", "Gauche/Espace", liste_Type_machine_radiotherapie),
    ("Type_dosimetrie", 1, "A*", "Gauche/Espace", not_liste),
    ("Num_innovation", 15, "A*", "Gauche/Espace", not_liste),
    ("Conversion_hospitalisation_complete", 1, "A*", "Gauche/Espace", liste_Conversion_hospitalisation_complete),
    ("Prise_en_charge_RAAC", 1, "A*", "Gauche/Espace", liste_Prise_en_charge_RAAC),
    ("Contexte_patient_surveillance_particuliere", 1, "A*", "Gauche/Espace", liste_Contexte_patient_surveillance_particuliere),
    ("Administration_produit_RH", 1, "A*", "Gauche/Espace", liste_Administration_produit_RH),
    ("Rescrit_tarifaire", 1, "A*", "Gauche/Espace", liste_Rescrit_tarifaire),
    ("Categorie_nombre_interventions_totales", 1, "A*", "Gauche/Espace", liste_Categorie_nombre_interventions_totales),
    ("Non_Programme_NP", 1, "A*", "Gauche/Espace", liste_Non_Programme_NP),
    ("Passage_structure_urgences", 1, "A*", "Gauche/Espace", liste_Passage_structure_urgences),
    ("Filler_2", 4, "A*", "Gauche/Espace", not_liste),
    ("Zone_reservee", 3, "A*", "NA/Espace", not_liste),
]

za_columns_info = [
    ("Date_realisation", 8, "Date", "NA/NA", not_liste),
    ("Code_CCAM", 7, "A", "NA/NA", liste_Code_CCAM),
    ("Extension_PMSI", 3,	"A**", "NA/Espace", liste_Extension_PMSI),
    ("Phase", 1, "A*", "NA/NA", liste_Phase),
    ("Activite", 1, "A*", "NA/NA", liste_Activite),
    ("Extension_documentaire", 1, "A*", "Gauche/Espace", liste_Extension_documentaire),
    ("Modificateurs", 4, "A*" ,	"Gauche/Espace", liste_Modificateurs),
    ("Remboursement_exceptionnel", 1, "A*",	"Gauche/Espace", liste_Remboursement_exceptionnel),
    ("Association_non_prevue", 1, "A*",	"Gauche/Espace", not_liste),
    ("Nombre_realisations_acte_nZA", 2,	"N"	,"Droite/Zéro", not_liste),
]


listed_columns_info = ["Groupage_num_CMD", "Num_GHM", "Groupage_code_retour", "Num_FINESS_inscription_ePMSI", "Sexe",
                       "Type_autorisation_lit_dedie", "Mode_entree_unite_medicale", "Provenance_mode_entree", "Mode_sortie_unite_medicale", 
                       "Destination_mode_sortie",  "Code_postal_residence", "Diagnostic_principal", "Diagnostic_relier", 
                       "Confirmation_codage_RSS", "Type_machine_radiotherapie", "Conversion_hospitalisation_complete", "Prise_en_charge_RAAC",
                       "Contexte_patient_surveillance_particuliere", "Administration_produit_RH", "Rescrit_tarifaire", 
                       "Categorie_nombre_interventions_totales", "Non_Programme_NP", "Passage_structure_urgences"]
                        
listed_za_columns_info = ["Extension_PMSI", "Phase", "Activite", "Modificateurs", "Remboursement_exceptionnel" ]

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


def generate_fake_data(data_type, length, fill_type="Gauche/Espace"):
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
        # Date formatted as ddmmyyyy
        return format_data(fake.date("%d%m%Y"), length, fill_type)


# Specific data generation functions for the special columns

    # Generate Provenance based on mode of entry
def generate_provenance(mode_entree, length, fill_type):
    if mode_entree in ["6", "7", "0"]:
        return format_data(
            random.choice(liste_Provenance_mode_entree), length, fill_type
        )
    return format_data(
        random.choice(["", liste_Provenance_mode_entree]), length, fill_type
    )


    # Generate Destination based on mode of exit
def generate_destination(mode_sortie, length, fill_type):
    if mode_sortie in ["6", "7", "0"]:
        return format_data(
            random.choice(liste_Destination_mode_sortie), length, fill_type
        )
    return format_data(
        random.choice(["", liste_Destination_mode_sortie]), length, fill_type
    )


# def generate_code_postal(length, fill_type):
#     # Generate a number between 00 and 99, format it as a 5-character string
#     code_postal = fake.random_number(digits=2, fix_len=True)
#     # Convert to string and format
#     return format_data(str(code_postal), length, fill_type)

# as grammes
poids_nouveau_ne_min = int(configs["poids_nouveau_ne_min"])
poids_nouveau_ne_max = int(configs["poids_nouveau_ne_max"])
def generate_poids_nouveau_ne(length, fill_type, min_value=poids_nouveau_ne_min, max_value=poids_nouveau_ne_max):
    return format_data(fake.random_int(min=min_value, max=max_value), length, fill_type)


# as weeks
age_gestationnel_min = int(configs["age_gestationnel_min"])
age_gestationnel_max = int(configs["age_gestationnel_max"])


def generate_age_gestationnel(length, fill_type, min_value=age_gestationnel_min, max_value=age_gestationnel_max):
    # Decide if the generated age should be full-term or preterm based on probability
    is_full_term = random.random() < 0.98  # 98% chance for full-term
    
    if is_full_term:
        # Generate a full-term age between 37 and max_value
        age = fake.random_int(min=37, max=max_value)
    else:
        # Generate a preterm age between min_value and 36
        age = fake.random_int(min=min_value, max=36)

    return format_data(age, length, fill_type)


date_naissance_start = datetime.strptime(configs["date_naissance_start"], "%Y-%m-%d")
date_naissance_end = datetime.strptime(configs["date_naissance_end"], "%Y-%m-%d")



def generate_date_naissance(length, fill_type, date_naissance_start, date_naissance_end, baby_percentage=0.53):
    # Decide if the entry should be a baby or a mother based on the given percentage
    is_baby = random.random() < baby_percentage

    if is_baby:
        # Generate a birth date for the baby within the specified date range (e.g., within 2023)
        date_naissance = fake.date_between(start_date=date_naissance_start, end_date=date_naissance_end)
    else:
        # Define age groups and weights to prioritize 30-34, followed by 25-29
        age_groups = [(17, 19), (20, 24), (25, 29), (30, 34), (35, 39), (40, 44), (45, 50)]
        weights = [0.05, 0.1, 0.25, 0.4, 0.1, 0.07, 0.03]  # Adjusted to prioritize 30-34 and 25-29
        
        # Select an age group based on the weights
        selected_group = random.choices(age_groups, weights=weights, k=1)[0]
        
        # Generate a random age within the selected age group
        mother_age = random.randint(selected_group[0], selected_group[1])
        
        # Calculate mother's birth year based on the chosen age
        mother_birth_year = date_naissance_end.year - mother_age
        mother_birth_start = datetime(mother_birth_year, 1, 1)
        mother_birth_end = datetime(mother_birth_year, 12, 31)
        
        # Generate a birth date within the calculated range for the mother
        date_naissance = fake.date_between(start_date=mother_birth_start, end_date=mother_birth_end)

    # Format the date and return it
    return format_data(date_naissance.strftime("%d%m%Y"), length, fill_type)



date_ddr_start = datetime.strptime(configs["date_ddr_start"], "%Y-%m-%d")
date_ddr_end = datetime.strptime(configs["date_ddr_end"], "%Y-%m-%d")


def generate_date_derniere_regle(length, fill_type, date_ddr_start, date_ddr_end):
    return format_data(fake.date_between(start_date=date_ddr_start, end_date=date_ddr_end).strftime("%d%m%Y"), length, fill_type)

# def generate_diagnostic_principal(length, fill_type):
#     return format_data(random.choice(configs["liste_diagnostic_principal"]), length, fill_type)

# def generate_diagnostic_relier(length, fill_type):
#     return format_data(random.choice(["FFF", "GGG", "HHH"]), length, fill_type)

def generate_diagnostic_assosicie(length, fill_type):
    return format_data(random.choice(liste_da), length, fill_type)

def generate_donnees_documentaire(length, fill_type):
    return format_data(random.choice(liste_dad), length, fill_type)


def generate_random_choice_from_liste(length, fill_type, liste):
    return format_data(random.choice(liste), length, fill_type)



def generate_code_CCAM(length, fill_type, liste):
    # List of high-priority values with more weight
    high_priority_values = ['JQGD001', 'JQGD002', 'JQGD003', 'JQGD004', 'JQGD005', 
                            'JQGD007', 'JQGD008', 'JQGD010', 'JQGD012', 'JQGD013']
    
    # Set up weights for each element in the list
    weights = [8 if item in high_priority_values else 1 for item in liste]  # Give higher weight to high-priority items

    # Use random.choices with weights to select an item
    selected_item = random.choices(liste, weights=weights, k=1)[0]
    
    # Format the selected item
    return format_data(selected_item, length, fill_type)



def generate_zones_acte(row):
    za_str = ""

    for column_name, length, data_type, fill_type, liste in za_columns_info:
        if column_name == "Date_realisation":
            start_date = datetime.strptime(row["Date_entree_unite_medicale"], "%d%m%Y")
            end_date = datetime.strptime(row["Date_sortie_unite_medicale"], "%d%m%Y")
            za_str += format_data(fake.date_between(start_date=start_date, end_date=end_date).strftime("%d%m%Y"), length, fill_type)

        elif column_name == "Code_CCAM":
            za_str += generate_code_CCAM(length, fill_type, liste)   

        elif column_name in listed_za_columns_info:
            za_str += generate_random_choice_from_liste(length, fill_type, liste)
                
        else :
            za_str += generate_fake_data(data_type, length, fill_type=fill_type)
                 
    return za_str 


def add_dynamic_fields(row):

    dyn_col = ""
    das, dads, zas =["", "", ""]
    
    #generate DAs
    for i in range(int(row["Nombre_diagnostics_associes"])):
        das += generate_diagnostic_assosicie(8, "Gauche/Espace")

    dyn_col += das
    
    #generate DADs
    for i in range(int(row["Nombre_donnees_documentaires"])):
        dads += generate_donnees_documentaire(8, "Gauche/Espace")

    dyn_col += dads

    #generate ZAs
    for i in range(int(row["Nombre_zones_actes"])):
        zas += generate_zones_acte(row)

    dyn_col += zas

    return dyn_col

#######################################################


# Function to generate fake data for a given year
def generate_yearly_fake_data(year, num_records):


    min_days_diff = configs["min_days_diff"]  # min differrence days between Date_entree_unite_medicale and Date_sortie_unite_medicale
    max_days_diff = configs["max_days_diff"]  # max differrence days between Date_entree_unite_medicale and Date_sortie_unite_medicale
  
    
    # Define min and max values for columns
    value_ranges = {
        "Date_entree_unite_medicale": {
            "start_date": datetime(year, 1, 1),
            "end_date": datetime(year, 12, 31),
        },
        "Date_sortie_unite_medicale": {"min_days_diff": min_days_diff, "max_days_diff": max_days_diff},
        "Poids_nouveau_ne_entree_unite_medicale": {"min_value": poids_nouveau_ne_min, "max_value": poids_nouveau_ne_max},
        "Age_gestationnel": {"min_value": age_gestationnel_min, "max_value": age_gestationnel_max},
        # Add more ranges as needed
    }

    # Initialize the data dictionary
    data = {}

    # Generate data for each column based on information and rules provided
    for column_name, length, data_type, fill_type, liste in columns_info:
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

        elif column_name in listed_columns_info:
            data[column_name] = [generate_random_choice_from_liste(length, fill_type, liste)
                                for _ in range(num_records)]

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
            
            data[column_name] = [generate_date_naissance(length, fill_type, date_naissance_start, date_naissance_end) for _ in range(num_records)]
            ## Load start and end dates from config and parse as datetime objects
            #date_naissance_start = value_ranges[column_name]["date_naissance_start"]
            #date_naissance_end = value_ranges[column_name]["date_naissance_end"]
            #data[column_name] = [
            #    format_data(fake.date_between(start_date=date_naissance_start, end_date=date_naissance_end).strftime("%d%m%Y"), length, fill_type)
            #    for _ in range(num_records)
            #        ]
        
        elif column_name == "Provenance_mode_entree":
            data[column_name] = [
                generate_provenance(
                    data["Mode_entree_unite_medicale"][i], length, fill_type
                )
                for i in range(num_records)
            ]
       
        elif column_name == "Destination_mode_sortie":
            data[column_name] = [
                generate_destination(
                    data["Mode_sortie_unite_medicale"][i], length, fill_type
                )
                for i in range(num_records)
            ]
        
        elif column_name == "Nombre_diagnostics_associes":
            min_num_da = configs["min_num_da"] # min Nombre_diagnostics_associes
            max_num_da = configs["max_num_da"] # max Nombre_diagnostics_associes
            data[column_name] = [format_data(fake.random_int(min=min_num_da, max=max_num_da), length, fill_type) for _ in range(num_records)
            ]

        elif column_name == "Nombre_donnees_documentaires":
            min_num_dad = configs["min_num_dad"] # min Nombre_donnees_documentaires
            max_num_dad = configs["max_num_dad"] # max Nombre_donnees_documentaires
            data[column_name] = [format_data(fake.random_int(min=min_num_dad, max=max_num_dad), length, fill_type) for _ in range(num_records)
            ]

        elif column_name == "Nombre_zones_actes":
            min_num_za = configs["min_num_za"] # min Nombre_zones_actes
            max_num_za = configs["max_num_za"] # max Nombre_zones_actes
            data[column_name] = [format_data(fake.random_int(min=min_num_za, max=max_num_za), length, fill_type) for _ in range(num_records)
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

        elif column_name == "Date_dernières_regles":
             data[column_name] = [
                 generate_date_derniere_regle(length, fill_type, date_ddr_start, date_ddr_end) for _ in range(num_records)
             ]

        # elif column_name == "Sexe":
        #     data[column_name] = [
        #         generate_sexe(length, fill_type) for _ in range(num_records)
        #     ]
        # elif column_name == "Mode_entree_unite_medicale":
        #     data[column_name] = [
        #         generate_mode_entree(length, fill_type) for _ in range(num_records)
        #     ]
        #  elif column_name == "Mode_sortie_unite_medicale":
        #     data[column_name] = [
        #         generate_mode_sortie(length, fill_type) for _ in range(num_records)
        #     ]

        # elif column_name == "Code_postal_residence":
        #     data[column_name] = [
        #         generate_code_postal(length, fill_type) for _ in range(num_records)
        #     ]

        # elif column_name == "Diagnostic_principal":
        #     data[column_name] = [
        #         generate_diagnostic_principal(length, fill_type) for _ in range(num_records)
        #     ]

        # elif column_name == "Diagnostic_relier":
        #     data[column_name] = [
        #         generate_diagnostic_relier(length, fill_type) for _ in range(num_records)
        #     ]
        else:
            data[column_name] = [
                generate_fake_data(data_type, length, fill_type=fill_type)
                for _ in range(num_records)
            ]


    # Convert to a DataFrame
    df = pd.DataFrame(data)

    # Constant columns (to define some constant values for some columns)
    
    df["Age_gestationnel"] = df["Age_gestationnel"].astype(int)
        
    def modify_poids_nouveau_ne(gestational_age):
        if gestational_age < 31:
            # Extremely preterm weight range
            poids = fake.random_int(min=poids_nouveau_ne_min, max=1500)
        elif 31 <= gestational_age < 37:
            # Moderate to late preterm weight range
            poids = fake.random_int(min=1500, max=2500)
        elif 37 <= gestational_age <= age_gestationnel_max:
            # Full-term weight range
            poids = fake.random_int(min=2500, max=poids_nouveau_ne_max)
        else:
            # Fallback in case of any unexpected gestational age
            poids = fake.random_int(min=poids_nouveau_ne_min, max=poids_nouveau_ne_max)

        return poids
    
    




    df["Poids_nouveau_ne_entree_unite_medicale"] = df["Age_gestationnel"].apply(modify_poids_nouveau_ne)
    df["Groupage_version_classification"] = configs["Groupage_version_classification"]
    df["Filler"] = configs["Filler"]
    df["Filler_2"] = configs["Filler_2"]
    df["Num_version_format_RSS"] = configs["Num_version_format_RSS"]
    #df["Groupage_code_retour"] = " 00"
    #df["Num_FINESS_inscription_ePMSI"] = configs["Num_FINESS_inscription_ePMSI"]
    df["Version_format_RUM"] = configs["Version_format_RUM"]
    df["Sexe"] = configs["Sexe"]
    df["Code_postal_residence"] = configs["Code_postal_residence"]
    #df["Date_dernières_regles"] = configs["Date_dernières_regles"]
    #df["Type_autorisation_lit_dedie"] = configs["Type_autorisation_lit_dedie"]
    df["Num_innovation"] = configs["Num_innovation"]

    return df

# An example data for 2023 
number_of_years = configs["number_of_years"] # how many years you want to generate data for (if 3 years you will get tha data for 2021, 2022, 2023)
yearly_record_number = configs['yearly_record_number'] # how many records you want to generate data per year
deviation = configs['deviation'] # the deviation of number of records per year -+

main_df = pd.DataFrame()

for year in range(2024 - number_of_years, 2024):
    df2 = generate_yearly_fake_data(year, random.randrange(yearly_record_number - deviation, yearly_record_number + deviation))
    df2["dynamic_cols"] = df2.apply(add_dynamic_fields, axis=1)
    main_df = pd.concat([main_df, df2])
   

main_df.to_csv("csv_fake_data_for_2023.csv", index=False, sep=",", encoding="utf-8")

# Convert the dataframe to txt file
test_df = main_df.astype(str).agg(''.join, axis=1)
test_df.to_csv("txt_fake_data_for_2023.txt", header=False, index=False, sep=",", encoding="utf-8")

print("fake data generated for 2023")