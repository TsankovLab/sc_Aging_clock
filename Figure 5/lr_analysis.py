""" -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

* File Name : lr_analysis.py

* Description : Plot cell-cell communication results for Tcell-Myeloid interactions and WNT genes interactions

* Creation Date : 04-29-2025

* Last Modified : Thu 01 May 2025 01:34:26 PM EDT

* Created By : Atharva Bhagwat

_._._._._._._._._._._._._._._._._._._._._. """

from __imports__ import *
from __config__ import *
from __paths__ import *
from scipy.stats import fisher_exact, mannwhitneyu
import matplotlib.lines as mlines
from matplotlib.colors import TwoSlopeNorm

os.makedirs(FIG_DIR, exist_ok=True)

# dotplots
files = {'icam1_itgal': 'icam1_itgal.pkl', 'cd40lg_cd40_anxa1_fpr3': 'cd40lg_cd40_anxa1_fpr3.pkl', 'wnt': 'wnt.pkl'}
for tag, f in tqdm(files.items()):
    pkl = pickle.load(open(os.path.join(OBJ_DIR, f), 'rb'))
    score_df, pval_df = pkl['score_df'], pkl['pval_df']

    log_pval_df = -np.log10(pval_df)
    fig_width, fig_height = 2, 2
    
    fig, ax = plt.subplots(figsize=(fig_width, fig_height))
    norm = TwoSlopeNorm(vmin=-0.5, vcenter=0, vmax=0.5)

    for i, row in enumerate(score_df.index):
        for j, col in enumerate(score_df.columns):
            size = log_pval_df.loc[row, col]
            color = score_df.loc[row, col]
            if 0.05 <= pval_df.loc[row, col] <= 0.1:
                edgecolor = 'gray'
            elif pval_df.loc[row, col] <= 0.05:
                edgecolor = 'black'
            else:
                edgecolor = None
            ax.scatter(j, i, s=size * 50, c=color, cmap='Spectral_r', norm=norm, edgecolors=edgecolor, linewidth=1.1)
    ax.set_xticks(range(len(score_df.columns)))
    ax.set_xticklabels(score_df.columns, rotation=0, ha='center', fontsize=4)
    ax.set_yticks(range(len(score_df.index)))
    ax.set_yticklabels(score_df.index, fontsize=4)
    ax.set_xlabel('celltypes')
    ax.set_ylabel('genes')
    # add colorbar
    sm = plt.cm.ScalarMappable(cmap='Spectral_r', norm=norm)
    sm.set_array([])
    plt.colorbar(sm, label='Difference', ax=ax, fraction=0.02, pad=0.15, ticks=[-0.5, 0, 0.5])
    # add size legend
    sizes = [0, 1, 2, 3] ## -log10(p) values
    size_legend_text = [plt.scatter([], [], s=s * 50, color='gray', alpha=0.6, label=f'{s}') for s in sizes]
    size_legend = ax.legend(handles=size_legend_text, title='-log10(p)', loc='upper right', fontsize=2, bbox_to_anchor=(1.15, 1))
    ax.add_artist(size_legend)
    # add edgecolor legend
    gray_patch = mlines.Line2D([], [], color='gray', marker='o', markerfacecolor='none', linestyle='None', markersize=8, label='0.1')
    black_patch = mlines.Line2D([], [], color='black', marker='o', markerfacecolor='none', linestyle='None', markersize=8, label='0.05')
    edgecolor_legend = ax.legend(handles=[gray_patch, black_patch], title='Significance', loc='upper left', fontsize=4, bbox_to_anchor=(1.01, 0.5))
    ax.add_artist(edgecolor_legend)
    plt.savefig(os.path.join(FIG_DIR, f'lr_{tag}.pdf'), bbox_inches='tight')
    plt.close()

# proximity score boxplots
prox_files = {'icam1_dc_itgal_cd4t': ('ICAM1+ DC', 'ITGAL+ CD4T'), 'icam1_dc_itgal_cd8t': ('ICAM1+ DC', 'ITGAL+ CD8T'), 'cd40lg_cd4t_cd40_dc': ('CD40LG+ CD4T', 'CD40+ DC'), 'anxa1_cd4t_fpr3_dc': ('ANXA1+ CD4T', 'FPR3+ DC')}
x_axis = 'age_category'
x_ticks = ['<40', '≥50']

for f, (center, target) in tqdm(prox_files.items()):
    pkl = pickle.load(open(os.path.join(OBJ_DIR, f'{f}_neigh_prox.pkl'), 'rb'))
    for key, df in pkl.items():
        young = df.loc[df[x_axis] == '<40', target].values
        young = young[~np.isnan(young)]
        
        old = df.loc[df[x_axis] == '≥50', target].values
        old = old[~np.isnan(old)]
        
        _, pval = mannwhitneyu(young, old)
        label = ("****" if pval <= 0.0001 else
                "***" if pval <= 0.001 else
                "**" if pval <= 0.01 else
                "*" if pval <= 0.05 else
                "")
        
        max_val = np.nanmax(df[target].values)
        fig, ax = plt.subplots(1, 1, figsize=(1, 1))
        sns.boxplot(df, x=x_axis, y=target, hue=x_axis, order=x_ticks, showcaps=False, palette=AGE_PALETTE, flierprops={"marker": ""}, linewidth=1.1, fill=False, width=0.8)
        sns.stripplot(df, x=x_axis, y=target, hue=x_axis, order=x_ticks, palette=AGE_PALETTE, size=1)
        plt.title(f'{target} {key} for {center} as center', fontsize=1)
        xcoor_l = 0
        xcoor_r = 1
        xcoor = (xcoor_l + xcoor_r) / 2
        ul = max_val + max_val/50
        plt.xticks(fontsize=1)
        plt.yticks(fontsize=1)
        plt.xlabel(None)
        plt.ylabel(None)
        ax.text(xcoor, ul, label, horizontalalignment='center', verticalalignment='bottom', **{'fontsize':8})
        ax.plot([xcoor_l, xcoor_r], [ul, ul], '-|', color='black', linewidth=0.8)
        plt.savefig(os.path.join(FIG_DIR, f'{f}_{key}.pdf'), bbox_inches='tight')
        plt.close()