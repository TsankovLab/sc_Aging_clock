""" -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

* File Name : spatial_plots.py

* Description : Plot spatial embedding for all figure panels.

* Creation Date : 05-29-2025

* Last Modified : Wed 01 Apr 2026 09:38:22 AM EDT

* Created By : Atharva Bhagwat

_._._._._._._._._._._._._._._._._._._._._. """

from __imports__ import *
from __config__ import *
from __paths__ import *

ScanpyConfig.figdir = Path(FIG_DIR)

fig_name_dict = {
    'celltype_final_D21.c3': 'fig5b',
    'celltype_final_D9.c1': 'fig5b',
    'celltype_final_D4.c2': 'fig5b',
    'celltype_final_D1.c2': 'exfig6c',
    'celltype_final_D20.c3': 'exfig6c',
    'cxcl9_myeloid_D21.c2': 'fig5g',
    'cxcl9_myeloid_D9.c1': 'exfig6e',
    'cxcl10_myeloid_D21.c2': 'exfig6f',
    'cxcl10_myeloid_D9.c1': 'exfig6f',
    'anxa1_cd4t_fpr3_dc_D10.c1': 'exfig6h',
    'anxa1_cd4t_fpr3_dc_D20.c3': 'exfig6h',
    'cd40lg_cd4t_cd40_dc_D10.c2': 'exfig6i',
    'cd40lg_cd4t_cd40_dc_D20.c3': 'exfig6i',
    'icam1_dc_itgal_cd4t_cd8t_D20.c1': 'exfig6g',
    'icam1_dc_itgal_cd4t_cd8t_D10.c2': 'exfig6g',
    'icam1_dc_itgal_cd8t_niche_D21.c2': 'fig5k',
}

core_mapping = {
    'celltype_final': (CELLTYPE_PALETTE, ['D21.c3', 'D9.c1', 'D4.c2', 'D1.c2', 'D20.c3']),
    'cxcl9_myeloid': (CXCL_PALETTE, ['D21.c2', 'D9.c1']),
    'cxcl10_myeloid': (CXCL_PALETTE, ['D21.c2', 'D9.c1']),
    'anxa1_cd4t_fpr3_dc': (ANXA1_FPR3, ['D10.c1', 'D20.c3']),
    'cd40lg_cd4t_cd40_dc': (CD40LG_CD40, ['D10.c2', 'D20.c3']),
    'icam1_dc_itgal_cd4t_cd8t': (ICAM1_ITGAL_PALETTE, ['D20.c1', 'D10.c2']),
    'icam1_dc_itgal_cd8t_niche': (ICAM1_ITGAL_PALETTE, ['D21.c2'])
}

for key, values in tqdm(core_mapping.items()):
    palette, cores = values
    for core_id in tqdm(cores):
        fig_name = fig_name_dict[f'{key}_{core_id}']
        adata = ad.read_h5ad(os.path.join(OBJ_DIR, f'{key}_{core_id}.h5ad'))
        age = adata.obs['age'].unique()[0]
        sc.pl.spatial(adata, color=key, palette=palette, spot_size=10, title=f'{key} {core_id} (age {age})', show=False, save=f'_{key}_{core_id}_{fig_name}.pdf')
