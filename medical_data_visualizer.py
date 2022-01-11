import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
with open('medical_examination.csv', 'r') as f:
  df = pd.read_csv(f, header=0) 

# Add 'overweight' column
df['overweight'] = ((df['weight'] / (df['height']/100)**2) > 25) * 1
# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = (df['cholesterol'] > 1) * 1
df['gluc'] = (df['gluc'] > 1) * 1




# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = df.melt(id_vars=['cardio'], value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.


    # Draw the catplot with 'sns.catplot()'
    sns.set_theme(style='whitegrid')
    fig = sns.catplot(x='variable', hue='value', col='cardio', data=df_cat, kind='count', aspect=1.2).fig
    for ax in fig.axes:
      ax.set_ylabel('total')

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df.loc[ (df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975)) ]

    # Calculate the correlation matrix
    corr =  np.corrcoef(df_heat, rowvar=False).round(1)

    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True
    # Set up the matplotlib figure
    fig, ax = plt.subplots()
    

    # Draw the heatmap with 'sns.heatmap()'
    ax = sns.heatmap(corr, mask=mask, vmax=0.3, vmin=-0.1, center=0.0, xticklabels=df_heat.columns, yticklabels=df_heat.columns, annot=True, fmt=".1f")


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
