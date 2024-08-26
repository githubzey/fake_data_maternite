format_122_header = """Groupage_version_classification,Groupage_num_CMD,Num_GHM,Filler,Num_version_format_RSS,Groupage_code_retour,Num_FINESS_inscription_ePMSI,Version_format_RUM,Num_RSS,Num_Admin_local_sejour,Num_RUM,Date_naissance,Sexe,Num_unite_medicale,Type_autorisation_lit_dedie,Date_entree_unite_medicale,Mode_entree_unite_medicale,Provenance_mode_entree,Date_sortie_unite_medicale,Mode_sortie_unite_medicale,Destination_mode_sortie,Code_postal_residence,Poids_nouveau_ne_entree_unite_medicale,Age_gestationnel,Date_dernières_regles,Nombre_seances,Nombre_diagnostics_associes,Nombre_donnees_documentaires,Nombre_zones_actes,Diagnostic_principal,Diagnostic_relier,IGS_2,Confirmation_codage_RSS,Type_machine_radiotherapie,Type_dosimetrie,Num_innovation,Conversion_hospitalisation_complete,Prise_en_charge_RAAC,Contexte_patient_surveillance_particuliere,Administration_produit_RH,Rescrit_tarifaire,Categorie_nombre_interventions_totales,Non_Programme_NP,Passage_structure_urgences,Filler_2,Zone_reservee"""
format_122 = [
(1,2),
(3,4),
(5,8),
(9,9),
(10,12),
(13,15),
(16,24),
(25,27),
(28,47),
(48,67),
(68,77),
(78,85),
(86,86),
(87,90),
(91,92),
(93,100),
(101,101),
(102,102),
(103,110),
(111,111),
(112,112),
(113,117),
(118,121),
(122,123),
(124,131),
(132,133),
(134,135),
(136,137),
(138,140),
(141,148),
(149,156),
(157,159),
(160,160),
(161,161),
(162,162),
(163,177),
(178,178),
(179,179),
(180,180),
(181,181),
(182,182),
(183,183),
(184,184),
(185,185),
(186,189),
(190,192)]

# Writing to CSV file
with open("output.csv", "w") as csv_file:
    # Write the header
    csv_file.write(format_122_header + "\n")

    with open("RSS_anonymise_extrait.txt") as f:
        for line in f.readlines():
            csv_line = ""
            for i, j in format_122:
                csv_line += line[i-1:j] + ","
            csv_file.write(csv_line[:-1] + "\n")
