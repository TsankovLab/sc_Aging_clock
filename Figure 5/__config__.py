""" -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

* File Name : __config__.py

* Description : Configs to generate plots

* Creation Date : 04-28-2025

* Last Modified : Mon 28 Apr 2025 10:39:16 AM EDT

* Created By : Atharva Bhagwat

_._._._._._._._._._._._._._._._._._._._._. """

AGE_PALETTE = {
    '<40': '#0091CA',
    '≥50': '#D8423D'
}

AGE_DIST_PALETTE = {
    #'<40'
    '15-29': '#0091CA',
    '30-39': '#0091CA',
    #'40-49'
    '40-49': '#D3D3D3',
    #'>=50'
    '50-59': '#D8423D',
    '60-69': '#D8423D',
    '70-85': '#D8423D',
}

SEX_PALETTE = {
    'Male': 'tab:green',
    'Female': 'tab:purple'
}

SMOKING_PALETTE = {
    'N/A': 'silver',
    'Yes': '#B2182B',
    'No': '#2166AC',
}

ETHNICITY_PALETTE = {
    'N/A': '#2c353b',
    'Other': '#98F5FF',
    'African American': '#9bb796',
    'White': '#f3827b'
}

QC_PALETTE = {
    'Xu et. al., this study\n(n=70)': 'black',
    'Vannan et. al., Nat. Gen.\n(n=10)': '#ACACAC',
    'Quanch etl. al., Nat. Comm.\n(n=2)': '#ACACAC'
}

CXCL_PALETTE = {
    'CXCL9+ Myeloid': '#CDC673',
    'CXCL9- Myeloid': '#6959CD',
    'CXCL10+ Myeloid': '#FF6347',
    'CXCL10- Myeloid': '#EEAEEE',
    'CD8T': '#60afda'
}

ICAM1_ITGAL_PALETTE = {
    'ICAM1+ DC': '#4c8145',
    'ICAM1- DC': '#86eb81',
    'ITGAL+ CD4T': '#894929',
    'ITGAL+ CD8T': '#4481A4',
    'CD8T': '#60afda'
}

ANXA1_FPR3 = {
    'ANXA1+ CD4T': '#9F5F3F',
    'FPR3+ DC': '#40623C'
}

CD40LG_CD40 = {
    'CD40LG+ CD4T': '#663D28',
    'CD40+ DC': '#659A5E'
}

NICHE_PROP = {
    'inside_niche': '#BE00FF',
    'outside_niche': '#FFC000'
}

CELLTYPE_PALETTE = {
    'AT1': '#555eaa',
    'AT2': '#cf3b30',
    'B': '#769a56',
    'Basal': '#f0e582',
    'CD4T': '#bb6235',
    'CD8T': '#60afda',
    'Multiciliated': '#ae1f63',
    'DC': '#78c268',
    'Fibroblasts': '#d593a5',
    'LymphaticEC': '#7c65a4',
    'Macrophages': '#e3ae67',
    'Mast': '#3c1b52',
    'Monocytes': '#622a79',
    'NK': '#e8c56c',
    'Pericytes': '#ca982b',
    'Plasma': '#99c93c',
    'Secretory': '#ca982b',
    'SmoothMuscle': '#99c93c',
    'Endothelial': '#486982',
}