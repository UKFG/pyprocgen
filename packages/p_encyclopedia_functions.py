# =============================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITE DE SON CONTENU :
# Créer le dictionnaire v_dic_biomes
# et le dicionnaire v_dic_arbres,
# connaitre la hauteur max d'un arbre
# -----------------------------
# CONTENU :
# - f_add_in_dic(v_dic, v_classe)
# - f_dic_biomes_creation()
# -----------------------------
# PROGRAMMES UTILISATEURS :
# - procedural_generation_2D.py
# - p_image_creation.py
# - p_trees_generation.py
# =============================

from .p_classes import cl_biome, cl_tree, cl_encyclopedia

###############################################################
####################### F_ADD_IN_DIC ##########################
###############################################################
def f_add_in_dic(v_dic, v_classe):
    # =============================
    # INFORMATIONS :
    # -----------------------------
    # UTILITE :
    # Ajoute v_classe dans le dicionnaire v_dic avec
    # v_classe.nom_biome comme référence
    # -----------------------------
    # PRECONDITIONS :
    # - v_dic est un dictionnaire
    # - v_classe est un objet qui possède une caractéristique nom_biome
    # -----------------------------
    # DEPEND DE :
    # - p_classes.cl_biome
    # - p_classes.cl_tree
    # -----------------------------
    # UTILISE PAR :
    # - p_biomes_dic_creation.f_dic_biomes_creation()
    # - p_biomes_dic_creation.f_dic_trees_creation()
    # =============================

    v_dic[v_classe.nom_biome] = v_classe



###############################################################
################### F_DIC_BIOMES_CREATION #####################
###############################################################
def f_encyclopedia_creation():
    # =============================
    # INFORMATIONS :
    # -----------------------------
    # UTILITE :
    # Remplis le dictionnaire de l'encyclopédie puis la crée
    # -----------------------------
    # PRECONDITIONS :
    # - NONE
    # -----------------------------
    # DEPEND DE :
    # - p_creation_biomes_dic.f_add_in_dic()
    # - p_classes.cl_encyclopedia
    # - p_classes.cl_biome
    # - p_classes.cl_tree
    # -----------------------------
    # UTILISE PAR :
    # - procedural_generation_2D.py
    # =============================

    v_dic_biomes = {}

    v_empty_tree = cl_tree(
        v_nom_arbre = "arbre_vide",
        v_prob_arbre = 0,
        v_body = [
            []
        ]
    )

    ###############################################################
    ########################## DESERT #############################
    ###############################################################

    ########################### ARBRES ############################

    v_arbre_desert_1 = cl_tree(
        v_nom_arbre = "arbre_desert_1",
        v_prob_arbre = 0.005,
        v_body = [
            [None,          "106 82 18",   None,          None,          "106 82 18"  ],

            ["106 82 18",   "142 93 60",   None,          "127 85 63",   None         ],

            [None,          None,          "142 93 60",   "142 93 60",   "106 82 18"  ],

            [None,          "106 82 18",   "142 93 60",   None,          None         ],

            [None,          None,          "142 93 60",   None,          None         ]
        ]
    )


    ########################### BIOMES ############################

    f_add_in_dic(
        v_dic_biomes,
        cl_biome(
            v_nom_biome = "Desert_Cool",

            v_temp_min =  0,
            v_temp_max =  1,
            v_pluv_min = -4,
            v_pluv_max = -3,

            v_coul = "193 165 133",

            v_vect_arbres = [
                v_arbre_desert_1
            ]
        )
    )

    f_add_in_dic(
        v_dic_biomes,
        cl_biome(
            v_nom_biome = "Desert_Tropical",

            v_temp_min =  2,
            v_temp_max =  3,
            v_pluv_min = -4,
            v_pluv_max = -3,

            v_coul = "247 210 165",

            v_vect_arbres = [
                v_arbre_desert_1
            ]
        )
    )

    f_add_in_dic(
        v_dic_biomes,
        cl_biome(
            v_nom_biome = "Desert_Warm",

            v_temp_min =  1,
            v_temp_max =  2,
            v_pluv_min = -4,
            v_pluv_max = -3,

            v_coul = "207 151 100",

            v_vect_arbres = [
                v_arbre_desert_1
            ]
        )
    )



    ###############################################################
    ######################## DESERT_SCUB ##########################
    ###############################################################

    ########################### ARBRES ############################

    v_arbre_desert_scub_1 = cl_tree(
        v_nom_arbre = "arbre_desert_scub_1",
        v_prob_arbre = 0.007,
        v_body = [
            ["156 152 107", "156 152 107", None         ],

            ["156 152 107", "118 115 98",  "156 152 107"],

            [None,          "118 115 98",  None         ]
        ]
    )

    v_arbre_desert_scub_2 = cl_tree(
        v_nom_arbre = "arbre_desert_scub_2",
        v_prob_arbre = 0.015,
        v_body = [
            [None,          "156 152 107", None         ],

            ["156 152 107", "118 115 98",  "156 152 107"],

            [None,          "118 115 98",  None         ]
        ]
    )

    v_buisson_desert_scub_1 = cl_tree(
        v_nom_arbre = "buisson_desert_scub_1",
        v_prob_arbre = 0.005,
        v_body = [
            ["118 115 98"]
        ]
    )


    ########################### BIOMES ############################

    f_add_in_dic(
        v_dic_biomes,
        cl_biome(
            v_nom_biome = "Desert_Scub_Cool",

            v_temp_min =  0,
            v_temp_max =  1,
            v_pluv_min = -3,
            v_pluv_max = -2,

            v_coul = "187 158 126",

            v_vect_arbres = [
                v_arbre_desert_scub_1,
                v_arbre_desert_scub_2,
                v_buisson_desert_scub_1
            ]
        )
    )

    f_add_in_dic(
        v_dic_biomes,
        cl_biome(
            v_nom_biome = "Desert_Scub_Tropical",

            v_temp_min =  2,
            v_temp_max =  3,
            v_pluv_min = -3,
            v_pluv_max = -2,

            v_coul = "251 224 181",

            v_vect_arbres = [
                v_arbre_desert_scub_1,
                v_arbre_desert_scub_2,
                v_buisson_desert_scub_1
            ]
        )
    )

    f_add_in_dic(
        v_dic_biomes,
        cl_biome(
            v_nom_biome = "Desert_Scub_Warm",

            v_temp_min =  1,
            v_temp_max =  2,
            v_pluv_min = -3,
            v_pluv_max = -2,

            v_coul = "193 161 122",

            v_vect_arbres = [
                v_arbre_desert_scub_1,
                v_arbre_desert_scub_2,
                v_buisson_desert_scub_1
            ]
        )
    )



    ###############################################################
    ######################### DRY_FOREST ##########################
    ###############################################################

    v_arbre_dry_forest_1 = cl_tree(
        v_nom_arbre = "arbre_dry_forest_1",
        v_prob_arbre = 0.015,
        v_body = [
            [None,          None,          "121 105 56",  None,          None,          None,          None         ],

            [None,          None,          None,          "133 103 69",  None,          "133 103 69",  "121 105 56" ],

            ["121 105 56",  "133 103 69",  "133 103 69",  "133 103 69",  "133 103 69",  None,          None         ],

            [None,          "121 105 56",  None,          "133 103 69",  None,          None,          None         ],

            [None,          None,          None,          "133 103 69",  None,          None,          None         ],

            [None,          None,          None,          "133 103 69",  None,          None,          None         ]
        ]
    )

    v_arbre_dry_forest_2 = cl_tree(
        v_nom_arbre = "arbre_dry_forest_2",
        v_prob_arbre = 0.01,
        v_body = [
            [None,          "121 105 56",  None,          "133 103 69",  "121 105 56" ],

            ["121 105 56",  "133 103 69",  None,          "133 103 69",  None         ],

            [None,          None,          "133 103 69",  None,          None         ],

            [None,          None,          "133 103 69",  None,          None         ]
        ]
    )

    v_arbre_dry_forest_3 = cl_tree(
        v_nom_arbre = "arbre_dry_forest_3",
        v_prob_arbre = 0.005,
        v_body = [
            [None,          None,          None,          "121 105 56",  None         ],

            ["121 105 56",  None,          None,          "133 103 69",  "121 105 56" ],

            [None,          "133 103 69",  "133 103 69",  "133 103 69",  None         ],

            [None,          None,          "133 103 69",  None,          None         ],

            [None,          None,          "133 103 69",  None,          None         ],

            [None,          None,          "133 103 69",  None,          None         ]
        ]
    )

    v_buisson_dry_forest_1 = cl_tree(
        v_nom_arbre = "v_buisson_dry_forest_1",
        v_prob_arbre = 0.0005,
        v_body = [
            ["121 105 56"]
        ]
    )


    f_add_in_dic(
        v_dic_biomes,
        cl_biome(
            v_nom_biome = "Dry_Forest_Tropical",

            v_temp_min =  2,
            v_temp_max =  3,
            v_pluv_min =  0, v_pluv_max =  1,

            v_coul = "177 148 108",

            v_vect_arbres = [
                v_arbre_dry_forest_1,
                v_arbre_dry_forest_2,
                v_arbre_dry_forest_3,
                v_buisson_dry_forest_1
            ]
        )
    )

    f_add_in_dic(
        v_dic_biomes,
        cl_biome(
            v_nom_biome = "Dry_Forest_Warm",

            v_temp_min =  1,
            v_temp_max =  2, v_pluv_min = -1,
            v_pluv_max =  0,
            v_coul = "167 138 104",

            v_vect_arbres = [
                v_arbre_dry_forest_1,
                v_arbre_dry_forest_2,
                v_arbre_dry_forest_3,
                v_buisson_dry_forest_1
            ]

        )
    )



    ###############################################################
    ######################## MOIST_FOREST #########################
    ###############################################################

    v_arbre_moist_forest_1 = cl_tree(
        v_nom_arbre = "arbre_moist_forest_1",
        v_prob_arbre = 0.1,
        v_body = [
            [None,          "54 62 15",    "34 46 10",    "34 46 10",    None         ],

            ["65 71 23",    "34 46 10",    "34 46 10",    "34 46 10",    None         ],

            ["34 46 10",    "34 46 10",    "34 46 10",    "34 46 10",    "34 46 10"   ],

            [None,          None,          "58 45 26",    None,          None         ],

            [None,          None,          "58 45 26",    None,          None         ]
        ]
    )

    v_arbre_moist_forest_2 = cl_tree(
        v_nom_arbre = "arbre_moist_forest_2",
        v_prob_arbre = 0.05,
        v_body = [
            [None,          "34 46 10",    "34 46 10",    "34 46 10",    None         ],

            ["65 71 23",    "34 46 10",    "34 46 10",    "34 46 10",    "34 46 10"   ],

            [None,          "34 46 10",    "34 46 10",    "34 46 10",    None         ],

            [None,          "34 46 10",    "58 45 26",    "34 46 10",    None         ],

            [None,          None,          "58 45 26",    None,          None         ],

            [None,          None,          "58 45 26",    None,          None         ],

            [None,          None,          "58 45 26",    None,          None         ]
        ]
    )

    v_arbre_moist_forest_3 = cl_tree(
        v_nom_arbre = "arbre_moist_forest_3",
        v_prob_arbre = 0.07,
        v_body = [
            [None,          "54 62 15",    None         ],

            ["34 46 10",    "34 46 10",    "34 46 10"   ],

            ["34 46 10",    "34 46 10",    "34 46 10"   ],

            [None,          "58 45 26",    None         ],

            [None,          "58 45 26",    None         ]
        ]
    )

    v_arbre_moist_forest_4 = cl_tree(
        v_nom_arbre = "arbre_moist_forest_4",
        v_prob_arbre = 0.01,
        v_body = [
            [None,          None,          "36 49 11",    "34 46 10",    None,          None         ],

            ["65 71 23",    "34 46 10",    "34 46 10",    "54 62 15",    "34 46 10",    None         ],

            ["34 46 10",    "59 58 12",    "34 46 10",    "34 46 10",    "34 46 10",    "34 46 10"   ],

            [None,          "48 57 13",    "58 45 26",    "58 45 26",    "34 46 10",    "54 62 15"   ],

            [None,          None,          None,          "58 45 26",    None,          None         ],

            [None,          None,          None,          "58 45 26",    None,          None         ]
        ]
    )

    v_arbre_moist_forest_5 = cl_tree(
        v_nom_arbre = "arbre_moist_forest_5",
        v_prob_arbre = 0.015,
        v_body = [
            [None,          "59 72 30",    None         ],

            ["44 57 18",    "34 46 10",    "51 65 23"   ],

            ["46 59 19",    "58 45 26",    "42 54 16"   ],

            [None,          "58 45 26",    None         ]
        ]
    )

    v_arbre_moist_forest_6 = cl_tree(
        v_nom_arbre = "arbre_moist_forest_6",
        v_prob_arbre = 0.005,
        v_body = [
            [None,          "65 71 23",    None,          None,          None         ],

            ["54 62 15",    "34 46 10",    "34 46 10",    "34 46 10",    "54 62 15"   ],

            ["34 46 10",    "34 46 10",    "34 46 10",    "34 46 10",    "34 46 10"   ],

            ["34 46 10",    "34 46 10",    "58 45 26",    "34 46 10",    "34 46 10"   ],

            ["34 46 10",    "34 46 10",    "58 45 26",    "34 46 10",    "34 46 10"   ],

            [None,          None,          "58 45 26",    None,          None         ],

            [None,          None,          "58 45 26",    None,          None         ]
        ]
    )


    v_buisson_moist_forest_1 = cl_tree(
        v_nom_arbre = "buisson_moist_forest_1",
        v_prob_arbre = 0.0005,
        v_body = [
            ["109 153 97" ]
        ]
    )

    f_add_in_dic(
        v_dic_biomes,
        cl_biome(
            v_nom_biome = "Moist_Forest_Cool",

            v_temp_min =  0,
            v_temp_max =  1,
            v_pluv_min = -1,
            v_pluv_max =  0,

            v_coul = "78 105 36",

            v_vect_arbres = [
                v_arbre_moist_forest_1,
                v_arbre_moist_forest_2,
                v_arbre_moist_forest_3,
                v_arbre_moist_forest_4,
                v_arbre_moist_forest_5,
                v_arbre_moist_forest_6,
                v_buisson_moist_forest_1
            ]

        )
    )

    f_add_in_dic(
        v_dic_biomes,
        cl_biome(
            v_nom_biome = "Moist_Forest_Tropical",

            v_temp_min =  2,
            v_temp_max =  3,
            v_pluv_min =  1,
            v_pluv_max =  2,

            v_coul = "93 84 51",

            v_vect_arbres = [
                v_arbre_moist_forest_1,
                v_arbre_moist_forest_2,
                v_arbre_moist_forest_3,
                v_arbre_moist_forest_4,
                v_arbre_moist_forest_5,
                v_arbre_moist_forest_6,
                v_buisson_moist_forest_1
            ]
        )
    )

    f_add_in_dic(
        v_dic_biomes,
        cl_biome(
            v_nom_biome = "Moist_Forest_Warm",

            v_temp_min =  1,
            v_temp_max =  2,
            v_pluv_min =  0,
            v_pluv_max =  1,

            v_coul = "86 104 56",

            v_vect_arbres = [
                v_arbre_moist_forest_1,
                v_arbre_moist_forest_2,
                v_arbre_moist_forest_3,
                v_arbre_moist_forest_4,
                v_arbre_moist_forest_5,
                v_arbre_moist_forest_6,
                v_buisson_moist_forest_1
            ]
        )
    )



    ###############################################################
    ######################## RAIN_FOREST ##########################
    ###############################################################

    v_arbre_rain_forest_1 = cl_tree(
        v_nom_arbre = "arbre_rain_forest_1",
        v_prob_arbre = 0.15,
        v_body = [
            [None,          "68 88 39",    "68 88 39",    "68 88 39",    None         ],

            ["68 88 39",    "68 88 39",    "68 88 39",    "68 88 39",    "68 88 39"   ],

            [None,          "68 88 39",    "88 107 55",   "68 88 39",    "68 88 39"   ],

            [None,          None,          "111 129 74",  "68 88 39",    None         ],

            [None,          None,          "116 133 78",  None,          None         ],

            [None,          None,          "116 133 78",  None,          None         ],

            [None,          None,          "116 133 78",  None,          None         ],

            [None,          None,          "116 133 78",  None,          None         ],

            [None,          None,          "114 131 77",  None,          None         ]
        ]
    )

    v_arbre_rain_forest_2 = cl_tree(
        v_nom_arbre = "arbre_rain_forest_2",
        v_prob_arbre = 0.03,
        v_body = [
            [None,          "68 88 39",    "68 88 39",    "68 88 39",    None         ],

            ["68 88 39",    "68 88 39",    "68 88 39",    "68 88 39",    "68 88 39"   ],

            [None,          "68 88 39",    "88 107 55",   "68 88 39",    "68 88 39"   ],

            [None,          None,          "111 129 74",  None,          None         ],

            [None,          None,          "116 133 78",  None,          None         ],

            [None,          None,          "116 133 78",  None,          None         ],

            [None,          None,          "116 133 78",  None,          None         ],

            [None,          "114 131 77",  "116 133 78",  None,          None         ],

            [None,          "114 131 77",  None,          None,          None         ]
        ]
    )

    v_arbre_rain_forest_3 = cl_tree(
        v_nom_arbre = "arbre_rain_forest_3",
        v_prob_arbre = 0.05,
        v_body = [
            ["68 88 39",    "68 88 39",    None         ],

            ["68 88 39",    "68 88 39",    "68 88 39"   ],

            ["68 88 39",    "88 107 55",   "68 88 39"   ],

            [None,          "111 129 74",  None         ],

            [None,          "116 133 78",  None         ]
        ]
    )


    f_add_in_dic(
        v_dic_biomes,
        cl_biome(
            v_nom_biome = "Rain_Forest",

            v_temp_min =  0,
            v_temp_max =  1,
            v_pluv_min =  1,
            v_pluv_max =  2,

            v_coul = "89 93 66",

            v_vect_arbres = [
                v_arbre_rain_forest_1,
                v_arbre_rain_forest_2,
                v_arbre_rain_forest_3
            ]
        )
    )



    ###############################################################
    ####################### ROCKS_AND_ICE #########################
    ###############################################################

    f_add_in_dic(
        v_dic_biomes,
        cl_biome(
            v_nom_biome = "Rocks_and_ice",

            v_temp_min = -3,
            v_temp_max = -2,
            v_pluv_min = -4,
            v_pluv_max = -1,

            v_coul = "190 220 255",

            v_vect_arbres = [
                v_empty_tree
            ]
        )
    )



    ###############################################################
    ########################### STEPPE ############################
    ###############################################################
    f_add_in_dic(
        v_dic_biomes,
        cl_biome(
            v_nom_biome = "Steppe",

            v_temp_min =  0,
            v_temp_max =  1,
            v_pluv_min = -2,
            v_pluv_max = -1,

            v_coul = "160 173 120",

            v_vect_arbres = [
                v_empty_tree
            ]
        )
    )



    ###############################################################
    #################### STEPPE_WOODLAND_THORN ####################
    ###############################################################
    v_arbre_steppe_woodland_thorn_1 = cl_tree(
        v_nom_arbre = "steppe_woodland_thorn_1",
        v_prob_arbre = 0.05,
        v_body = [
            [None,          "34 58 26",    None         ],

            ["34 58 26",    "34 58 26",    "34 58 26"   ],

            ["34 58 26",    "34 58 26",    "34 58 26"   ],

            [None,          "88 73 50",    None         ]
        ]
    )

    v_arbre_steppe_woodland_thorn_2 = cl_tree(
        v_nom_arbre = "steppe_woodland_thorn_2",
        v_prob_arbre = 0.05,
        v_body = [
            [None,          "34 58 26",    None         ],

            ["34 58 26",    "34 58 26",    "34 58 26"   ],

            [None,          "88 73 50",    None         ]
        ]
    )

    v_arbre_steppe_woodland_thorn_3 = cl_tree(
        v_nom_arbre = "steppe_woodland_thorn_3",
        v_prob_arbre = 0.005,
        v_body = [
            ["34 58 26",    "34 58 26",    None         ],

            ["34 58 26",    "34 58 26",    "34 58 26"   ],

            [None,          "88 73 50",    None         ]
        ]
    )

    v_arbre_steppe_woodland_thorn_4 = cl_tree(
        v_nom_arbre = "steppe_woodland_thorn_4",
        v_prob_arbre = 0.005,
        v_body = [
            [None,          "34 58 26",    "34 58 26"   ],

            ["34 58 26",    "34 58 26",    "34 58 26"   ],

            [None,          "88 73 50",    None         ]
        ]
    )

    f_add_in_dic(
        v_dic_biomes,
        cl_biome(
            v_nom_biome = "Steppe_Woodland_Thorn",
            v_temp_min =  1,
            v_temp_max =  2,
            v_pluv_min = -2,
            v_pluv_max = -1,
            v_coul = "160 173 120",

            v_vect_arbres = [
                v_arbre_steppe_woodland_thorn_1,
                v_arbre_steppe_woodland_thorn_2,
                v_arbre_steppe_woodland_thorn_3,
                v_arbre_steppe_woodland_thorn_4
            ]
        )
    )

    ###############################################################
    ########################### TAIGA #############################
    ###############################################################
    v_arbre_taiga_1 = cl_tree(
        v_nom_arbre = "v_arbre_taiga_1",
        v_prob_arbre = 0.03,
        v_body = [
            [None,          None,          "34 58 26",    None,          None         ],

            [None,          None,          "34 58 26",    None,          None         ],

            [None,          "34 58 26",    "34 58 26",    "34 58 26",    None         ],

            ["34 58 26",    "34 58 26",    "88 73 50",    "34 58 26",    "34 58 26"   ],

            [None,          None,          "88 73 50",    None,          None         ]
        ]
    )

    v_arbre_taiga_2 = cl_tree(
        v_nom_arbre = "v_arbre_taiga_2",
        v_prob_arbre = 0.01,
        v_body = [
            [None,          None,          "34 58 26",    None,          None         ],

            [None,          None,          "34 58 26",    None,          None         ],

            [None,          "34 58 26",    "34 58 26",    "34 58 26",    None         ],

            ["34 58 26",    "34 58 26",    "88 73 50",    "34 58 26",    None         ],

            [None,          None,          "88 73 50",    None,          None         ]
        ]
    )

    v_arbre_taiga_3 = cl_tree(
        v_nom_arbre = "v_arbre_taiga_3",
        v_prob_arbre = 0.03,
        v_body = [
            [None,          "34 58 26",    None         ],

            [None,          "34 58 26",    None         ],

            ["34 58 26",    "34 58 26",    "34 58 26"   ],

            [None,          "88 73 50",    None         ]
        ]
    )


    f_add_in_dic(
        v_dic_biomes,
        cl_biome(
            v_nom_biome = "Taiga_Desert",

            v_temp_min = -1,
            v_temp_max =  0,
            v_pluv_min = -4,
            v_pluv_max = -3,
            v_coul = "146 126 101",

            v_vect_arbres = [
                v_arbre_taiga_1,
                v_arbre_taiga_2,
                v_arbre_taiga_3
            ]
        )
    )



    f_add_in_dic(
        v_dic_biomes,
        cl_biome(
            v_nom_biome = "Taiga_Dry",
            v_temp_min = -1,
            v_temp_max =  0,
            v_pluv_min = -3,
            v_pluv_max = -2,
            v_coul = "167 175 120",

            v_vect_arbres = [
                v_arbre_taiga_1,
                v_arbre_taiga_2,
                v_arbre_taiga_3
            ]
        )
    )

    f_add_in_dic(
        v_dic_biomes,
        cl_biome(
            v_nom_biome = "Taiga_Moist",

            v_temp_min = -1,
            v_temp_max =  0,
            v_pluv_min = -2,
            v_pluv_max = -1,

            v_coul = "86 104 56",

            v_vect_arbres = [
                v_arbre_taiga_1,
                v_arbre_taiga_2,
                v_arbre_taiga_3
            ]
        )
    )



    f_add_in_dic(
        v_dic_biomes,
        cl_biome(
            v_nom_biome = "Taiga_Rain",

            v_temp_min = -1,
            v_temp_max =  0,
            v_pluv_min =  0,
            v_pluv_max =  1,

            v_coul = "57 102 21",

            v_vect_arbres = [
                v_arbre_taiga_1,
                v_arbre_taiga_2,
                v_arbre_taiga_3
            ]
        )
    )



    f_add_in_dic(
        v_dic_biomes,
        cl_biome(
            v_nom_biome = "Taiga_Wet",

            v_temp_min = -1,
            v_temp_max =  0,
            v_pluv_min = -1,
            v_pluv_max =  0,

            v_coul = "75 102 44",

            v_vect_arbres = [
                v_arbre_taiga_1,
                v_arbre_taiga_2,
                v_arbre_taiga_3
            ]
        )
    )


    ###############################################################
    ########################## TOUDRA #############################
    ###############################################################
    v_buisson_toundra_1 = cl_tree(
        v_nom_arbre = "buisson_toundra_1",
        v_prob_arbre = 0.005,
        v_body = [
            ["34 58 26",    "34 58 26"   ]
        ]
    )

    v_buisson_toundra_2 = cl_tree(
        v_nom_arbre = "buisson_toundra_2",
        v_prob_arbre = 0.002,
        v_body = [
            ["34 58 26",    "34 58 26",    "34 58 26"   ]
        ]
    )

    v_buisson_toundra_3 = cl_tree(
        v_nom_arbre = "buisson_toundra_3",
        v_prob_arbre = 0.001,
        v_body = [
            [None,          "34 58 26",    None,          None         ],

            ["34 58 26",    "34 58 26",    "34 58 26",    "34 58 26"   ]
        ]
    )

    v_buisson_toundra_4 = cl_tree(
        v_nom_arbre = "buisson_toundra_4",
        v_prob_arbre = 0.001,
        v_body = [
            [None,          None,          "34 58 26",    None         ],

            ["34 58 26",    "34 58 26",    "34 58 26",    "34 58 26"   ]
        ]
    )

    f_add_in_dic(
        v_dic_biomes,
        cl_biome(
            v_nom_biome = "Toundra_Dry",

            v_temp_min = -2,
            v_temp_max = -1,
            v_pluv_min = -4,
            v_pluv_max = -3,

            v_coul = "167 175 120",

            v_vect_arbres = [
                v_buisson_toundra_1,
                v_buisson_toundra_2,
                v_buisson_toundra_3,
                v_buisson_toundra_4
            ]
        )
    )



    f_add_in_dic(
        v_dic_biomes,
        cl_biome(
            v_nom_biome = "Toundra_Moist",

            v_temp_min = -2,
            v_temp_max = -1,
            v_pluv_min = -3,
            v_pluv_max = -2,

            v_coul = "86 104 56",

            v_vect_arbres = [
                v_buisson_toundra_1,
                v_buisson_toundra_2,
                v_buisson_toundra_3,
                v_buisson_toundra_4
            ]
        )
    )



    f_add_in_dic(
        v_dic_biomes,
        cl_biome(
            v_nom_biome = "Toundra_Rain",

            v_temp_min = -2,
            v_temp_max = -1,
            v_pluv_min = -1,
            v_pluv_max =  0,

            v_coul = "57 102 21",

            v_vect_arbres = [
                v_buisson_toundra_1,
                v_buisson_toundra_2,
                v_buisson_toundra_3,
                v_buisson_toundra_4
            ]
        )
    )



    f_add_in_dic(
        v_dic_biomes,
        cl_biome(
            v_nom_biome = "Toundra_Wet",

            v_temp_min = -2,
            v_temp_max = -1,
            v_pluv_min = -2,
            v_pluv_max = -1,

            v_coul = "75 102 44",

            v_vect_arbres = [
                v_buisson_toundra_1,
                v_buisson_toundra_2,
                v_buisson_toundra_3,
                v_buisson_toundra_4
            ]
        )
    )


    ###############################################################
    ###################### TROPICAL_FOREST ########################
    ###############################################################
    v_arbre_tropical_forest_1 = cl_tree(
        v_nom_arbre = "arbre_tropical_forest_1",
        v_prob_arbre = 0.15,
        v_body = [
            [None,          "0 69 41",     "0 69 41",     "0 69 41",     "0 69 41",     "0 69 41",     None         ],

            ["0 69 41",     "0 69 41",     "0 69 41",     "0 69 41",     "0 69 41",     "0 69 41",     "0 69 41"    ],

            [None,          None,          None,          "88 73 50",    None,          None,          None         ],

            [None,          None,          None,          "88 73 50",    None,          None,          None         ],

            [None,          None,          None,          "88 73 50",    None,          None,          None         ],

            [None,          None,          None,          "88 73 50",    None,          None,          None         ],

            [None,          None,          None,          "88 73 50",    "88 73 50",    None,          None         ],

            [None,          None,          None,          None,          "88 73 50",    None,          None         ],

            [None,          None,          None,          None,          "88 73 50",    None,          None         ]
        ]
    )

    v_arbre_tropical_forest_2 = cl_tree(
        v_nom_arbre = "arbre_tropical_forest_2",
        v_prob_arbre = 0.1,
        v_body = [
            [None,          "124 168 21",  "124 168 21",  "124 168 21",  "124 168 21",  None         ],

            ["124 168 21",  "124 168 21",  "124 168 21",  "124 168 21",  "124 168 21",  "124 168 21" ],

            [None,          None,          "225 219 185", None,          None,          None         ],

            [None,          None,          "225 219 185", None,          None,          None         ],

            [None,          None,          "225 219 185", None,          None,          None         ],

            [None,          None,          "225 219 185", None,          None,          None         ],

            [None,          None,          "225 219 185", None,          None,          None         ],

            [None,          None,          "225 219 185", None,          None,          None         ]
        ]
    )

    v_arbre_tropical_forest_3 = cl_tree(
        v_nom_arbre = "arbre_tropical_forest_3",
        v_prob_arbre = 0.05,
        v_body = [
            [None,          "19 84 20",    "19 84 20",    "19 84 20",    None         ],

            ["19 84 20",    "19 84 20",    "19 84 20",    "19 84 20",    "19 84 20"   ],

            [None,          None,          "46 27 23",    None,          None         ],

            [None,          None,          "46 27 23",    None,          None         ],

            [None,          None,          "46 27 23",    None,          None         ],

            [None,          None,          "46 27 23",    None,          None         ],

            [None,          None,          "46 27 23",    None,          None         ]
        ]
    )

    f_add_in_dic(
        v_dic_biomes,
        cl_biome(
            v_nom_biome = "Tropical_Forest_Tropical",

            v_temp_min =  2,
            v_temp_max =  3,
            v_pluv_min =  3,
            v_pluv_max =  4,

            v_coul = "71 94 12",

            v_vect_arbres = [
                v_arbre_tropical_forest_1,
                v_arbre_tropical_forest_2,
                v_arbre_tropical_forest_3
            ]
        )
    )


    f_add_in_dic(
        v_dic_biomes,
        cl_biome(
            v_nom_biome = "Tropical_Forest_Warm",

            v_temp_min =  1,
            v_temp_max =  2,
            v_pluv_min =  2,
            v_pluv_max =  3,

            v_coul = "94 124 16",

            v_vect_arbres = [
                v_arbre_tropical_forest_1,
                v_arbre_tropical_forest_2,
                v_arbre_tropical_forest_3
            ]
        )
    )


    ###############################################################
    ###################### VERY_DRY_FOREST ########################
    ###############################################################
    v_arbre_very_dry_forest_1 = cl_tree(
        v_nom_arbre = "arbre_very_dry_forest_1",
        v_prob_arbre = 0.055,
        v_body = [
            [None,          None,          "121 105 56",  None,          None,          None,          None         ],

            [None,          None,          None,          "133 103 69",  None,          "133 103 69",  "121 105 56" ],

            ["121 105 56",  "133 103 69",  "133 103 69",  "133 103 69",  "133 103 69",  None,          None         ],

            [None,          "121 105 56",  None,          "133 103 69",  None,          None,          None         ],

            [None,          None,          None,          "133 103 69",  None,          None,          None         ],

            [None,          None,          None,          "133 103 69",  None,          None,          None         ]
        ]
    )

    v_arbre_very_dry_forest_2 = cl_tree(
        v_nom_arbre = "arbre_very_dry_forest_2",
        v_prob_arbre = 0.05,
        v_body = [
            [None,          "121 105 56",  None,          "133 103 69",  "121 105 56" ],

            ["121 105 56",  "133 103 69",  "133 103 69",  "133 103 69",  None         ],

            [None,          None,          "133 103 69",  None,          None         ],

            [None,          None,          "133 103 69",  None,          None         ]
        ]
    )

    v_arbre_very_dry_forest_3 = cl_tree(
        v_nom_arbre = "arbre_very_dry_forest_3",
        v_prob_arbre = 0.05,
        v_body = [
            [None,          None,          None,          "121 105 56",  None         ],

            ["121 105 56",  None,          None,          "133 103 69",  "121 105 56" ],

            [None,          "133 103 69",  "133 103 69",  "133 103 69",  None         ],

            [None,          None,          "133 103 69",  None,          None         ],

            [None,          None,          "133 103 69",  None,          None         ],

            [None,          None,          "133 103 69",  None,          None         ]
        ]
    )

    v_buisson_very_dry_forest_1 = cl_tree(
        v_nom_arbre = "buisson_very_dry_forest_1",
        v_prob_arbre = 0.005,
        v_body = [
            ["121 105 56" ]
        ]
    )

    f_add_in_dic(
        v_dic_biomes,
        cl_biome(
            v_nom_biome = "Very_Dry_Forest",

            v_temp_min =  2,
            v_temp_max =  3,
            v_pluv_min = -1,
            v_pluv_max =  0,

            v_coul = "191 168 124",

            v_vect_arbres = [
                v_arbre_very_dry_forest_1,
                v_arbre_very_dry_forest_2,
                v_arbre_very_dry_forest_3,
                v_buisson_very_dry_forest_1
            ]
        )
    )


    ###############################################################
    ######################### WET_FOREST ##########################
    ###############################################################
    v_arbre_wet_forest_1 = cl_tree(
        v_nom_arbre = "arbre_wet_forest_1",
        v_prob_arbre = 0.07,
        v_body = [
            [None,          "38 127 0",    "38 127 0",    "38 127 0",    None         ],

            ["38 127 0",    "38 127 0",    "38 127 0",    "38 127 0",    "38 127 0"   ],

            [None,          None,          "95 80 51",    None,          None         ],

            [None,          None,          "95 80 51",    None,          None         ],

            [None,          None,          "95 80 51",    None,          None         ],

            [None,          None,          "95 80 51",    None,          None         ],

            [None,          None,          "95 80 51",    None,          None         ],

            [None,          None,          "95 80 51",    None,          None         ]
        ]
    )

    v_arbre_wet_forest_1_variante_1 = cl_tree(
        v_nom_arbre = "arbre_wet_forest_1_variante_1",
        v_prob_arbre = 0.1,
        v_body = [
            [None,          "96 142 8",    "96 142 8",    "96 142 8",    None         ],

            ["96 142 8",    "96 142 8",    "96 142 8",    "96 142 8",    "96 142 8"   ],

            [None,          None,          "103 103 17",   None,          None         ],

            [None,          None,          "103 103 17",   None,          None         ],

            [None,          None,          "103 103 17",   None,          None         ],

            [None,          None,          "103 103 17",   None,          None         ],

            [None,          None,          "103 103 17",   None,          None         ],

            [None,          None,          "103 103 17",   None,          None         ]
        ]
    )

    v_arbre_wet_forest_1_variante_2 = cl_tree(
        v_nom_arbre = "arbre_wet_forest_1_variante_2",
        v_prob_arbre = 0.08,
        v_body = [
            [None,          "38 127 0",    "38 127 0",    "38 127 0",    None         ],

            ["38 127 0",    "38 127 0",    "38 127 0",    "38 127 0",    "38 127 0"   ],

            [None,          None,          "132 115 95",  None,          None         ],

            [None,          None,          "132 115 95",  None,          None         ],

            [None,          None,          "132 115 95",  None,          None         ],

            [None,          None,          "132 115 95",  None,          None         ],

            [None,          None,          "132 115 95",  None,          None         ],

            [None,          None,          "132 115 95",  None,          None         ]
        ]
    )

    v_arbre_wet_forest_2 = cl_tree(
        v_nom_arbre = "arbre_wet_forest_2",
        v_prob_arbre = 0.03,
        v_body = [
            [None,          "38 127 0",    None         ],

            ["38 127 0",    "38 127 0",    "38 127 0"   ],

            [None,          "95 80 51",    None         ],

            [None,          "95 80 51",    None         ],

            [None,          "95 80 51",    None         ],

            [None,          "95 80 51",    None         ]
        ]
    )

    v_arbre_wet_forest_2_variante_1 = cl_tree(
        v_nom_arbre = "arbre_wet_forest_2_variante_1",
        v_prob_arbre = 0.07,
        v_body = [
            [None,          "96 142 8",    None         ],

            ["96 142 8",    "96 142 8",    "96 142 8"   ],

            [None,          "103 103 17",    None         ],

            [None,          "103 103 17",    None         ],

            [None,          "103 103 17",    None         ],

            [None,          "103 103 17",    None         ]
        ]
    )

    v_arbre_wet_forest_2_variante_2 = cl_tree(
        v_nom_arbre = "arbre_wet_forest_2_variante_2",
        v_prob_arbre = 0.07,
        v_body = [
            [None,          "38 127 0",    None         ],

            ["38 127 0",    "38 127 0",    "38 127 0"   ],

            [None,          "132 115 95",  None         ],

            [None,          "132 115 95",  None         ],

            [None,          "132 115 95",  None         ],

            [None,          "132 115 95",  None         ]
        ]
    )

    f_add_in_dic(
        v_dic_biomes,
        cl_biome(
            v_nom_biome = "Wet_Forest_Cool",

            v_temp_min =  0,
            v_temp_max =  1,
            v_pluv_min =  0,
            v_pluv_max =  1,

            v_coul = "128 168 104",

            v_vect_arbres = [
                v_arbre_wet_forest_1,
                v_arbre_wet_forest_2
            ]
        )
    )



    f_add_in_dic(
        v_dic_biomes,
        cl_biome(
            v_nom_biome = "Wet_Forest_Tropical",

            v_temp_min =  2,
            v_temp_max =  3,
            v_pluv_min =  2,
            v_pluv_max =  3,

            v_coul = "128 168 104",

            v_vect_arbres = [
                v_arbre_wet_forest_1_variante_1,
                v_arbre_wet_forest_2_variante_1,
            ]
        )
    )



    f_add_in_dic(
        v_dic_biomes,
        cl_biome(
            v_nom_biome = "Wet_Forest_Warm",

            v_temp_min =  1,
            v_temp_max =  2,
            v_pluv_min =  1,
            v_pluv_max =  2,

            v_coul = "128 168 104",

            v_vect_arbres = [
                v_arbre_wet_forest_1_variante_2,
                v_arbre_wet_forest_2_variante_2,
            ]
        )
    )


    ###############################################################
    ####################### WOODLAND_THORN ########################
    ###############################################################
    v_arbre_woodland_thorn_1 = cl_tree(
        v_nom_arbre = "arbre_woodland_thorn_1",
        v_prob_arbre = 0.06,
        v_body = [
            [None,          "39 67 0",     "39 67 0",     "39 67 0",     "39 67 0",     "39 67 0",     None         ],

            ["39 67 0",     "39 67 0",     "39 67 0",     "39 67 0",     "39 67 0",     "39 67 0",     "39 67 0"    ],

            [None,          "138 127 99",  None,          "118 98 65",   None,          "138 127 99",  None         ],

            [None,          None,          None,          "118 98 65",   None,          "138 127 99",  None         ],

            [None,          None,          None,          None,          "118 98 65",   None,          None         ],

            [None,          None,          None,          None,          "118 98 65",   None,          None         ]
        ]
    )

    v_arbre_woodland_thorn_2 = cl_tree(
        v_nom_arbre = "arbre_woodland_thorn_2",
        v_prob_arbre = 0.03,
        v_body = [
            [None,          "39 67 0",     "39 67 0",     None         ],

            ["39 67 0",     "39 67 0",     "39 67 0",     "39 67 0"    ],

            ["138 127 99",  None,          "118 98 65",   None         ],

            [None,          None,          "118 98 65",   None         ],

            [None,          None,          "118 98 65",   None         ]
        ]
    )

    v_arbre_woodland_thorn_3 = cl_tree(
        v_nom_arbre = "arbre_woodland_thorn_3",
        v_prob_arbre = 0.01,
        v_body = [
            [None,          "39 67 0",     "39 67 0",     "39 67 0",     "39 67 0",     None         ],

            ["39 67 0",     "39 67 0",     "39 67 0",     "39 67 0",     "39 67 0",     "39 67 0"    ],

            ["138 127 99",  None,          "118 98 65",   None,          "138 127 99",  None         ],

            ["138 127 99",  None,          "118 98 65",   None,          "138 127 99",  None         ],

            [None,          None,          "118 98 65",   None,          None,          None         ],

            [None,          None,          "118 98 65",   None,          None,          None         ],

            [None,          "118 98 65",   None,          None,          None,          None         ]
        ]
    )

    f_add_in_dic(
        v_dic_biomes,
        cl_biome(
            v_nom_biome = "Woodland_Thorn",

            v_temp_min =  2,
            v_temp_max =  3,
            v_pluv_min = -2,
            v_pluv_max = -1,

            v_coul = "149 163 140",

            v_vect_arbres = [
                v_arbre_woodland_thorn_1,
                v_arbre_woodland_thorn_2,
                v_arbre_woodland_thorn_3
            ]
        )
    )


    ###############################################################
    ############################ WATER ############################
    ###############################################################
    f_add_in_dic(
        v_dic_biomes,
        cl_biome(
            v_nom_biome = "Water",

            v_temp_min =  0,
            v_temp_max =  0,
            v_pluv_min =  0,
            v_pluv_max =  0,

            v_coul = "30 144 235",

            v_vect_arbres = [
                v_empty_tree
            ]
        )
    )






    f_add_in_dic(
        v_dic_biomes,
        cl_biome(
            v_nom_biome = "Cyan_Water1",

            v_temp_min =  1.85,
            v_temp_max =  2,
            v_pluv_min =  3,
            v_pluv_max =  4,

            v_coul = "64 164 223",

            v_vect_arbres = [
                v_empty_tree
            ]
        )
    )

    f_add_in_dic(
        v_dic_biomes,
        cl_biome(
            v_nom_biome = "Cyan_Water2",

            v_temp_min =  0.85,
            v_temp_max =  1,
            v_pluv_min =  2,
            v_pluv_max =  3,

            v_coul = "64 164 223",

            v_vect_arbres = [
                v_empty_tree
            ]
        )
    )

    f_add_in_dic(
        v_dic_biomes,
        cl_biome(
            v_nom_biome = "Cyan_Water3",

            v_temp_min = -0.25,
            v_temp_max =  0,
            v_pluv_min =  1,
            v_pluv_max =  2,

            v_coul = "64 164 223",

            v_vect_arbres = [
                v_empty_tree
            ]
        )
    )

    f_add_in_dic(
        v_dic_biomes,
        cl_biome(
            v_nom_biome = "Cyan_Water4",

            v_temp_min = -1.25,
            v_temp_max = -1,
            v_pluv_min =  0,
            v_pluv_max =  1,

            v_coul = "64 164 223",

            v_vect_arbres = [
                v_empty_tree
            ]
        )
    )

    f_add_in_dic(
        v_dic_biomes,
        cl_biome(
            v_nom_biome = "Cyan_Water5",

            v_temp_min = -2.25,
            v_temp_max = -2,
            v_pluv_min = -1,
            v_pluv_max =  0,

            v_coul = "64 164 223",

            v_vect_arbres = [
                v_empty_tree
            ]
        )
    )

    f_add_in_dic(
        v_dic_biomes,
        cl_biome(
            v_nom_biome = "Cyan_Water6",

            v_temp_min =  1,
            v_temp_max =  2,
            v_pluv_min =  3,
            v_pluv_max =  3.15,

            v_coul = "64 164 223",

            v_vect_arbres = [
                v_empty_tree
            ]
        )
    )

    f_add_in_dic(
        v_dic_biomes,
        cl_biome(
            v_nom_biome = "Cyan_Water7",

            v_temp_min =  0,
            v_temp_max =  1,
            v_pluv_min =  2,
            v_pluv_max =  2.15,

            v_coul = "64 164 223",

            v_vect_arbres = [
                v_empty_tree
            ]
        )
    )

    f_add_in_dic(
        v_dic_biomes,
        cl_biome(
            v_nom_biome = "Cyan_Water8",

            v_temp_min = -1,
            v_temp_max =  0,
            v_pluv_min =  1,
            v_pluv_max =  1.15,

            v_coul = "64 164 223",

            v_vect_arbres = [
                v_empty_tree
            ]
        )
    )

    f_add_in_dic(
        v_dic_biomes,
        cl_biome(
            v_nom_biome = "Cyan_Water9",

            v_temp_min = -2,
            v_temp_max = -1,
            v_pluv_min =  0,
            v_pluv_max =  0.15,

            v_coul = "64 164 223",

            v_vect_arbres = [
                v_empty_tree
            ]
        )
    )

    f_add_in_dic(
        v_dic_biomes,
        cl_biome(
            v_nom_biome = "Cyan_Water10",

            v_temp_min = -3,
            v_temp_max = -2,
            v_pluv_min = -1,
            v_pluv_max = -0.85,

            v_coul = "64 164 223",

            v_vect_arbres = [
                v_empty_tree
            ]
        )
    )


    return cl_encyclopedia("Classique", v_dic_biomes)
