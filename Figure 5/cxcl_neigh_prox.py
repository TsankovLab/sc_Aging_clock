""" -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

* File Name : cxcl_neigh_prox.py

* Description : Plot neighborhood scores and proximity scores for CXCL9 and CXCL10 analysis

* Creation Date : 04-28-2025

* Last Modified : Mon 28 Apr 2025 01:49:44 PM EDT

* Created By : Atharva Bhagwat

_._._._._._._._._._._._._._._._._._._._._. """

from __imports__ import *
from __config__ import *
from __paths__ import *
from scipy.stats import wilcoxon

os.makedirs(FIG_DIR, exist_ok=True)

files = {'cxcl9': 'cxcl9_neigh_prox.pkl', 'cxcl10': 'cxcl10_neigh_prox.pkl', 'cxcl9_merged_t': 'cxcl9_merged_t_neigh_prox.pkl', 'cxcl10_merged_t': 'cxcl10_merged_t_neigh_prox.pkl'}

for tag, f in files.items():
    pkl = pickle.load(open(os.path.join(OBJ_DIR, f), 'rb'))
    for score_type in pkl.keys():
        for celltype in pkl[score_type].keys():
            df = pkl[score_type][celltype]
            pos_key, neg_key = df.columns

            _, pval = wilcoxon(df[pos_key], df[neg_key])
            label = (
                "****" if pval <= 0.0001 else
                "***" if pval <= 0.001 else
                "**" if pval <= 0.01 else
                "*" if pval <= 0.05 else
                "")
            max_val = np.nanmax(df)
    
            fig, ax = plt.subplots(1, 1, figsize=(1, 1))
            sns.boxplot(df, showcaps=False, flierprops={"marker": ""}, linewidth=1.1, fill=False, width=0.8, palette=CXCL_PALETTE)
            sns.stripplot(df, palette=CXCL_PALETTE, size=1)
            plt.title(f'{celltype} {score_type} {pos_key} vs {neg_key}', fontsize=1)
            xcoor_l = 0
            xcoor_r = 1
            xcoor = (xcoor_l + xcoor_r) / 2
            ul = max_val + max_val/50
            plt.xticks(fontsize=1)
            plt.yticks(fontsize=1)
            ax.text(xcoor, ul, label, horizontalalignment='center', verticalalignment='bottom', **{'fontsize':8})
            ax.plot([xcoor_l, xcoor_r], [ul, ul], '-|', color='black', linewidth=0.8)
            plt.savefig(os.path.join(FIG_DIR, f'{tag}_{celltype}_{score_type}.pdf'), bbox_inches='tight')
            plt.close()