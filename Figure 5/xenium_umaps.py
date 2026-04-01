""" -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

* File Name : xenium_umaps.py

* Description : Plot UMAPs for all merged data colored by celltype annotation and donor id

* Creation Date : 05-01-2025

* Last Modified : Wed 01 Apr 2026 09:26:05 AM EDT

* Created By : Atharva Bhagwat

_._._._._._._._._._._._._._._._._._._._._. """

from __imports__ import *
from __config__ import *
from __paths__ import *

ScanpyConfig.figdir = Path(FIG_DIR)

# all cells
mdata = ad.read_h5ad(os.path.join(OBJ_DIR, 'xenium.h5ad'))
sc.pl.umap(mdata, color='celltype_final', palette=CELLTYPE_PALETTE, show=False, save='_celltype_fig5c.png')
sc.pl.umap(mdata, color='donor_id', show=False, save='_donor_fig5c.png')

# epithelial cells
mdata = ad.read_h5ad(os.path.join(OBJ_DIR, 'epithelial_xenium.h5ad'))
sc.pl.umap(mdata, color='celltype_final', palette=CELLTYPE_PALETTE, show=False, save='_epithelial_fig5d.png')

# stromal cells
mdata = ad.read_h5ad(os.path.join(OBJ_DIR, 'stromal_xenium.h5ad'))
sc.pl.umap(mdata, color='celltype_final', palette=CELLTYPE_PALETTE, show=False, save='_stromal_fig5d.png')

# myeloid cells
mdata = ad.read_h5ad(os.path.join(OBJ_DIR, 'myeloid_xenium.h5ad'))
sc.pl.umap(mdata, color='celltype_final', palette=CELLTYPE_PALETTE, show=False, save='_myeloid_fig5d.png')

# lymphoid cells
mdata = ad.read_h5ad(os.path.join(OBJ_DIR, 'lymphoid_xenium.h5ad'))
sc.pl.umap(mdata, color='celltype_final', palette=CELLTYPE_PALETTE, show=False, save='_lymphoid_fig5d.png')
