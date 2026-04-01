""" -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

* File Name : qc_compare.py

* Description : Plot n_genes_by_counts for this study and Vannan et. al.

* Creation Date : 05-01-2025

* Last Modified : Wed 01 Apr 2026 09:25:04 AM EDT

* Created By : Atharva Bhagwat

_._._._._._._._._._._._._._._._._._._._._. """

from __imports__ import *
from __config__ import *
from __paths__ import *

os.makedirs(FIG_DIR, exist_ok=True)

df = pd.read_csv(os.path.join(OBJ_DIR, 'qc_compare.csv'))

fig, ax = plt.subplots(1, 1, figsize=(2, 2))
sns.boxplot(df, x='study', y='n_genes_by_counts', hue='study', palette=QC_PALETTE, showcaps=False, showfliers=False, flierprops={'marker': ''}, linewidth=1.1, fill=False, width=0.5)
plt.xticks(rotation=90)
plt.savefig(os.path.join(FIG_DIR, 'exfig6b_n_genes_by_counts_compare.pdf'), bbox_inches='tight')
plt.close()
