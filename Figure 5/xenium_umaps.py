""" -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

* File Name : xenium_umaps.py

* Description : Plot UMAPs for all merged data colored by celltype annotation and donor id

* Creation Date : 05-01-2025

* Last Modified : Fri 09 May 2025 02:59:54 PM EDT

* Created By : Atharva Bhagwat

_._._._._._._._._._._._._._._._._._._._._. """

from __imports__ import *
from __config__ import *
from __paths__ import *

ScanpyConfig.figdir = Path(FIG_DIR)

mdata = ad.read_h5ad(os.path.join(OBJ_DIR, 'xenium.h5ad'))
sc.pl.umap(mdata, color='celltype_final', palette=CELLTYPE_PALETTE, show=False, save='_celltype.png')
sc.pl.umap(mdata, color='donor_id', show=False, save='_donor.png')
