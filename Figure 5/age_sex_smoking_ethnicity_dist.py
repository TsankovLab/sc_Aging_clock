""" -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

* File Name : age_sex_smoking_ethnicity_dist.py

* Description : Plot age and sex distribution

* Creation Date : 04-28-2025

* Last Modified : Thu 29 May 2025 02:51:39 PM EDT

* Created By : Atharva Bhagwat

_._._._._._._._._._._._._._._._._._._._._. """

from __imports__ import *
from __paths__ import *
from __config__ import *

os.makedirs(FIG_DIR, exist_ok=True)

# age distribution
age_map = json.load(open(os.path.join(OBJ_DIR, 'age_map.json'), 'r'))

age_df = pd.DataFrame(pd.json_normalize(age_map).T)
age_df.columns = ['age']
age_df['label'] = age_df['age'].map(lambda age: '15-29' if 15 <= age <= 29 else
                                                  '30-39' if 30 <= age <= 39 else
                                                  '40-49' if 40 <= age <= 49 else
                                                  '50-59' if 50 <= age <= 59 else
                                                  '60-69' if 60 <= age <= 69 else
                                                  '70-85' if 70 <= age <= 85 else None)
label_counts = age_df['label'].value_counts().reindex(AGE_DIST_PALETTE.keys(), fill_value=0)

plt.figure(figsize=(3, 3))
sns.barplot(
    x=label_counts.index,
    y=label_counts.values,
    palette=AGE_DIST_PALETTE,
    order=label_counts.index,
    width=0.9
)

plt.xlabel("Age")
plt.ylabel("Sample counts")
plt.title("Xenium cohort age distribution")
plt.savefig(os.path.join(FIG_DIR, 'xenium_age_distribution.pdf'), bbox_inches='tight')
plt.close()

# sex distribution
sex_map = json.load(open(os.path.join(OBJ_DIR, 'sex_map.json'), 'r'))

sex_df = pd.DataFrame(pd.DataFrame(sex_map.items(), columns=['sample_id', 'sex'])['sex'].value_counts())
sex_df['count'] = sex_df['count']/sex_df.sum().values[0]

ax = sex_df.T.plot(kind='bar', stacked=True, color=SEX_PALETTE.values())
plt.title('Sex distribution')
plt.ylabel('Fraction of samples')
plt.yticks([0, 0.5, 1], [0, 0.5, 1])

for idx, column in enumerate(sex_df.columns):
    cumulative_height = 0
    for row in sex_df.index:
        value = sex_df.loc[row, column]
        if value > 0.01:
            ax.text(
                idx,
                cumulative_height + value / 2,
                f'{value*100:.1f}%',
                ha='center',
                va='center',
                fontsize=10,
                color='black'
            )
        cumulative_height += value
plt.savefig(os.path.join(FIG_DIR, 'xenium_sex_distribution.pdf'), bbox_inches='tight')
plt.close()

# smoking + ethnicity distribution
colors = list(SMOKING_PALETTE.values()) + list(ETHNICITY_PALETTE.values())

df = pd.read_csv(os.path.join(OBJ_DIR, 'smoking_ethnicity_dist.csv'), index_col=0)

ax = df.plot(kind='bar', stacked=True, figsize=(4, 4), color=colors)

ax.set_title("Smoking and Ethnicity distribution")
ax.set_ylabel("Percentage of samples")
plt.xticks(rotation=0)
plt.yticks([0, 25, 50, 75, 100], ['0%', '25%', '50%', '75%', '100%'])

for idx, col in enumerate(df.index):
    cumulative_height = 0
    for category in df.columns:
        value = df.loc[col, category]
        if np.isnan(value):
            value = 0
        if value > 0.01:
            ax.text(
                idx,
                cumulative_height + value / 2,
                f'{value:.1f}%',
                ha='center',
                va='center',
                fontsize=10,
                color='black'
            )
        cumulative_height += value
plt.savefig(os.path.join(FIG_DIR, 'xenium_smoking_ethnicity_distribution.pdf'), bbox_inches='tight')
plt.show()
