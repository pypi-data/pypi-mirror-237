import numpy as np
import pandas as pd
import seaborn as sns
from scipy.stats import uniform, randint
import matplotlib.pyplot as plt

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample dataframe
data = {
    'Phenotype': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'B', 'B', 'C', 'A'],
}
df = pd.DataFrame(data)

# Create a countplot (bar plot of value counts)
plt.figure(figsize=(10, 6))
sns.countplot(x='Phenotype', data=df, order=df['Phenotype'].value_counts().index)
plt.title('Phenotype Distribution')
plt.ylabel('Count')
plt.xlabel('Phenotype')
plt.show()


def sns_plot():
    # Simulate DataFrame
    # df = pd.DataFrame({
    # 'rsid'  : ['rs{}'.format(i) for i in np.arange(10000)],
    # 'chrom' : [i for i in randint.rvs(1,23+1,size=10000)],
    # 'pos'   : [i for i in randint.rvs(0,10**5,size=10000)],
    # 'pval'  : uniform.rvs(size=10000)})
    # df['-logp'] = -np.log10(df.pval)
    # df = df.sort_values(['chrom','pos'])

    df = pd.read_csv("single_snp.csv", delimiter='\t')
    df['-logp'] = -np.log10(df['PValue'])
    df = df.sort_values(['Chr','ChrPos'])

    df.reset_index(inplace=True, drop=True)
    df['i'] = df.index

    # Generate Manhattan plot: (#optional tweaks for relplot: linewidth=0, s=9)
    plot = sns.relplot(data=df, x='i', y='-logp', aspect=3.7,
                       hue='Chr', palette = 'bright', legend=None)
    chrom_df=df.groupby('Chr')['i'].median()
    plot.ax.set_xlabel('Chr')
    plot.ax.set_xticks(chrom_df)
    plot.ax.set_xticklabels(chrom_df.index)
    plot.fig.suptitle('Manhattan plot')
    plt.show()

# import matplotlib.pyplot as plt
# import geneview as gv
#
# df = pd.read_csv("gwas_results.csv", delimiter=' ')
# df.columns = ['SNP', 'PValue']
# df[['Chr', 'ChrPos']] = df['SNP'].str.split(':', expand=True)
#
#
# #df = df.sort_values(by=['Chr', 'ChrPos'])
# df['Chr'] = df['Chr'].astype(int)
# # chr_names = df['Chr'].unique()
# df['ChrPos'] = df['ChrPos'].astype(int)
# ax = gv.manhattanplot(data=df, chrom='Chr', pos="ChrPos", pv="PValue", snp="SNP", logp=False, title="GWAS Manhatten Plot",
#                       xlabel="Chromosome", ylabel=r"Feature Importance")
# plt.show()
# # df = df.head(limit)
#
# # common parameters for plotting
# plt_params = {
#     "font.sans-serif": "Arial",
#     "legend.fontsize": 14,
#     "axes.titlesize": 18,
#     "axes.labelsize": 16,
#     "xtick.labelsize": 14,
#     "ytick.labelsize": 14
# }
# plt.rcParams.update(plt_params)
#
# # Create a manhattan plot
# f, ax = plt.subplots(figsize=(12, 5), facecolor="w", edgecolor="k")
# # xtick = set(["chr" + i for i in list(map(str, chr_names))])
# _ = gv.manhattanplot(data=df, chrom='Chr', pos="ChrPos", pv="PValue", snp="SNP", marker="."
#                      , logp=False,
#                      sign_marker_color="r", title="GWAS Manhatten Plot " + '\n',
#                      # xtick_label_set=xtick,
#                      xlabel="Chromosome", ylabel=r"Feature Importance", sign_line_cols=["#D62728", "#2CA02C"],
#                      #hline_kws={"linestyle": "--", "lw": 1.3},
#                      text_kws={"fontsize": 12, "arrowprops": dict(arrowstyle="-", color="k", alpha=0.6)},
#                      ax=ax)
# plt.tight_layout(pad=1)
# plt.savefig('test.png', dpi=100)
#
# df = df.sort_values(by=['PValue'])
# print (df)
#
#



# set parameter show=True, if you want view the image instead of saving

#sns_plot()
#
# # import libraries
# from pandas import DataFrame
# from scipy.stats import uniform
# from scipy.stats import randint
# import numpy as np
# import matplotlib.pyplot as plt
# #import seaborn as sns
# #sns.set_theme()
# # sample data
# # df = DataFrame({'gene' : ['gene-%i' % i for i in np.arange(1000000)],
# # 'pvalue' : uniform.rvs(size=1000000),
# # 'Chr' : ['ch-%i' % i for i in randint.rvs(0,12,size=1000000)]})
# # # -log_10(pvalue)
# # df['-logp'] = -np.log10(df.pvalue)
# # print (df)
# df = pd.read_csv("single_snp.csv", delimiter='\t')
# df['-logp'] = -np.log10(df['PValue'])
# df['Chr'] = df['Chr'].apply(lambda x: f"chr{int(x)}")
# print (df)
# #df = df.sort_values(['Chr', 'ChrPos'])
#
#
# df['Chr'] = df['Chr'].astype('category')
#
# #df['Chr']= df['Chr'].cat.set_categories(['ch-%i' % i for i in range(12)], ordered=True)
# df['Chr']= df['Chr'].cat.set_categories(['chr%i' % i for i in range(12)], ordered=True)
#
# #print (df)
# df = df.sort_values('Chr')
#
#
# # How to plot gene vs. -log10(pvalue) and colour it by chromosome?
# df['ind'] = range(len(df))
# df_grouped = df.groupby(('Chr'))
# print (df_grouped)
# # manhattan plot
# fig = plt.figure(figsize=(14, 8)) # Set the figure size
# ax = fig.add_subplot(111)
# colors = ['#FFD1DC','#A2CFFE','#B0E57C', '#FFF79A']
# x_labels = []
# x_labels_pos = []
# #print (df)
# #df = df.reset_index()
# for num, (name, group) in enumerate(df_grouped):
#     group.plot(kind='scatter', x='ind', y='-logp',color=colors[num % len(colors)], ax=ax)
#     x_labels.append(name)
#     #print (group['ind'])
#     #print (group['ind'].iloc[-1])
#     #x_labels_pos.append((group['ind'].iloc[-1] - (group['ind'].iloc[-1] - group['ind'].iloc[0])/2))
# #ax.set_xticks(x_labels_pos)
# ax.set_xticklabels(x_labels)
#
# # set axis limits
# ax.set_xlim([0, len(df)])
# ax.set_ylim([0, 20])
#
# # x axis label
# ax.set_xlabel('Chromosome')
#
# # show the graph
# plt.show()


