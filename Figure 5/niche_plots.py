""" -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

* File Name : niche_plots.py

* Description : Plot proportion of cells colored by age categories in niche, proportion of DC and ICAM1+ DC in niche vs out of niche

* Creation Date : 05-27-2025

* Last Modified : Tue 27 May 2025 03:53:30 PM EDT

* Created By : Atharva Bhagwat

_._._._._._._._._._._._._._._._._._._._._. """

from __imports__ import *
from __config__ import *
from __paths__ import *
from scipy.stats import mannwhitneyu

import SOAPy_st as sp

os.makedirs(FIG_DIR, exist_ok=True)

# niche cellprop by age
df = pd.read_csv(os.path.join(OBJ_DIR, 'niche_cellprop_by_age.csv'), index_col=0)
plt.figure(figsize=(3, 3))
df.T.plot(kind='bar', stacked=True, color=['#d7433b', '#1091c8'])
plt.ylabel('Percentage')
plt.savefig(os.path.join(FIG_DIR, 'niche_young_old.pdf'), bbox_inches='tight')
plt.close()

niche_boxplots = pickle.load(open(os.path.join(OBJ_DIR, 'niche_boxplots.pkl'), 'rb'))
# ICAM1+ DC prop
icam1_dc = niche_boxplots['icam1_dc']
left_key, right_key = icam1_dc['prop_type'].unique()
cluster = icam1_dc.loc[icam1_dc['prop_type'] == left_key, 'score'].values
other = icam1_dc.loc[icam1_dc['prop_type'] == right_key, 'score'].values

cluster = cluster.astype(float)
cluster = cluster[~np.isnan(cluster)]

other = other.astype(float)
other = other[~np.isnan(other)]

_, pval = mannwhitneyu(cluster, other)
label = (
        "****" if pval <= 0.0001 else
        "***" if pval <= 0.001 else
        "**" if pval <= 0.01 else
        "*" if pval <= 0.05 else
        "")

# fig, ax = plt.subplots(1, 1, figsize=(8, 5))
fig, ax = plt.subplots(1, 1, figsize=(3, 3))
sns.boxplot(icam1_dc, x='prop_type', y='score', order=[left_key, right_key], palette=NICHE_PROP, showcaps=False, flierprops={'marker': ''}, linewidth=1.1, fill=False, width=0.5)
xcoor_l = 0
xcoor_r = 1
xcoor = (xcoor_l + xcoor_r)/2
max_val = np.nanmax(icam1_dc['score'].values)
ul = max_val + max_val/50
ax.text(xcoor, ul, label, horizontalalignment='center', verticalalignment='bottom', **{'fontsize':8})
ax.plot([xcoor_l, xcoor_r], [ul, ul], '-|', color='black', linewidth=0.8)
plt.title('ICAM1+ DC proportion')
plt.savefig(os.path.join(FIG_DIR, 'icam1_dc_niche.pdf'), bbox_inches='tight')
plt.close()

# DC prop
dc = niche_boxplots['dc']
left_key, right_key = icam1_dc['prop_type'].unique()
cluster = dc.loc[icam1_dc['prop_type'] == left_key, 'score'].values
other = dc.loc[icam1_dc['prop_type'] == right_key, 'score'].values

cluster = cluster.astype(float)
cluster = cluster[~np.isnan(cluster)]

other = other.astype(float)
other = other[~np.isnan(other)]

_, pval = mannwhitneyu(cluster, other)
label = (
        "****" if pval <= 0.0001 else
        "***" if pval <= 0.001 else
        "**" if pval <= 0.01 else
        "*" if pval <= 0.05 else
        "")

# fig, ax = plt.subplots(1, 1, figsize=(8, 5))
fig, ax = plt.subplots(1, 1, figsize=(3, 3))
sns.boxplot(dc, x='prop_type', y='score', order=[left_key, right_key], palette=NICHE_PROP, showcaps=False, flierprops={'marker': ''}, linewidth=1.1, fill=False, width=0.5)
xcoor_l = 0
xcoor_r = 1
xcoor = (xcoor_l + xcoor_r)/2
max_val = np.nanmax(dc['score'].values)
ul = max_val + max_val/50
ax.text(xcoor, ul, label, horizontalalignment='center', verticalalignment='bottom', **{'fontsize':8})
ax.plot([xcoor_l, xcoor_r], [ul, ul], '-|', color='black', linewidth=0.8)
plt.title('DC proportion')
plt.savefig(os.path.join(FIG_DIR, 'dc_niche.pdf'), bbox_inches='tight')
plt.close()

# niche heatmap
adata = ad.read_h5ad(os.path.join(OBJ_DIR, 'xenium.h5ad'))
adata.obs['C_niche'] = pd.read_csv(os.path.join(OBJ_DIR, 'soapy_obs.csv'), index_col=0)['C_niche'].astype(str)
adata.uns['SOAPy'] = pickle.load(open(os.path.join(OBJ_DIR, 'soapy_uns.pkl'), 'rb'))
_ = sp.pl.show_celltype_niche_heatmap(
    adata,
    norm_method='proportion',
    cmap='BuGn',
    title='r50 k30',
    figsize=(20, 16),
    save=os.path.join(FIG_DIR, 'niche_heatmap.pdf'),
    **{'vmin':0, 'vmax':0.75}
)