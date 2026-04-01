""" -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

* File Name : gene_exp_dotplot.py

* Description : Plot showing expression of representative markers across each annotated cell type

* Creation Date : 04-01-2026

* Last Modified : Wed Apr  1 09:57:36 2026

* Created By : Atharva Bhagwat

_._._._._._._._._._._._._._._._._._._._._. """

from __imports__ import *
from __config__ import *
from __paths__ import *

os.makedirs(FIG_DIR, exist_ok=True)

gene_map = {
    'AT1': ['AGER', 'SCEL'],
    'AT2': ['SFTPD', 'PLA2G4F'],
    'BPlasma': ['CD79A', 'MS4A1', 'MZB1', 'TNFRSF17'],
    'Basal': ['KRT5', 'TP63'],
    'T': ['CD3D', 'CD40LG', 'CD28', 'CD8B'],
    'DC': ['CLEC10A', 'CD1C'],
    'Endothelial': ['VWF', 'CLDN5', 'PROX1', 'MMRN1'],
    'Fibroblasts': ['PDGFRA', 'SFRP2'],
    'Macrophages': ['MARCO', 'APOE'],
    'Mast': ['MS4A2', 'KIT'],
    'Monocytes': ['S100A12', 'FCN1'],
    'Multiciliated': ['CCDC78', 'FOXJ1'],
    'NK': ['NKG7', 'GZMB'],
    'Pericytes': ['KCNK3', 'LAMC3'],
    'Secretory': ['BPIFB1', 'MUC5B'],
    'SmoothMuscle': ['PLN', 'DES']
}

ctorder = ['AT1', 'AT2', 'Basal', 'Multiciliated', 'Secretory', 'Endothelial', 'LymphaticEC', 'Fibroblasts', 'Pericytes', 'SmoothMuscle', 'B', 'Plasma', 'CD4T', 'CD8T', 'NK', 'DC', 'Mast', 'Macrophages', 'Monocytes']
def get_ordered(gene_map):
    grouporder = ['AT1', 'AT2', 'Basal', 'Multiciliated', 'Secretory', 'Endothelial', 'Fibroblasts', 'Pericytes', 'SmoothMuscle', 'BPlasma', 'T', 'NK', 'DC', 'Mast', 'Macrophages', 'Monocytes']
    return {k: gene_map[k] for k in grouporder}

mdata = ad.read_h5ad(os.path.join(OBJ_DIR, 'xenium.h5ad'))

plt.rcParams.update({'font.size': 6})
dp = sc.pl.dotplot(
    mdata,
    var_names=get_ordered(gene_map),
    groupby='celltype_final',
    use_raw=False,
    categories_order=ctorder,
    swap_axes=True,
    figsize=(6, 6),
    dot_min=0.0,
    dot_max=1.0,
    show=False,
    return_fig=True,
)

dp = dp.style(
    smallest_dot=0.2,
    largest_dot=80,
    cmap='Reds'
)

dp.savefig(os.path.join(FIG_DIR, 'exfig6a_dotplot_celltype_markers.pdf'))