import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from matplotlib import*
import matplotlib.pyplot as plt
from matplotlib.cm import register_cmap
from scipy import stats
from sklearn.decomposition import PCA as sklearnPCA
import seaborn

from matplotlib import rc
rc('text', usetex=True)
rc('font', family='serif', size=18)


df1 = pd.read_csv('data_processed/mean_n.csv', index_col=0)


#custom compute: covariance -> eigen_values
# cov_mat = np.cov(df1)
# eig_vals, eig_vecs = np.linalg.eig(cov_mat)
# var_exp = [(i / sum(eig_vals)) for i in sorted(eig_vals, reverse=True)]

#use sklearn lib
#df1 = StandardScaler().fit_transform(df1)
pca = sklearnPCA().fit(df1)


#plot variance explined by each component & cumulative
fig = plt.figure(figsize=(8,8))
ax = plt.subplot(111)
ax.plot(pca.explained_variance_ratio_, 'o-', label="component", markersize=0.4)
ax.plot(np.cumsum(pca.explained_variance_ratio_), 'o-', label="cumulative", markersize=0.4)
plt.title('PCA variance explained')
plt.xlabel('components')
plt.ylabel('explained variance')
ax.yaxis.set_label_coords(-0.08,0.5)
ax.legend(loc='upper left', bbox_to_anchor=(0.55, 0.55), shadow=True, ncol=1)
plt.savefig("./results/variance.png")

fig = plt.figure(figsize=(9,5))
ax = plt.subplot(111)
ax.plot(pca.components_[0], 'o-', label="PCA-1", markersize=0.4)
ax.plot(pca.components_[1], 'o-', label="PCA-2", markersize=0.4)
plt.axvline(x=15, ymin=-0.1, ymax=1.2, color="black", linestyle=(0, (5, 10)))
plt.axvline(x=39, ymin=-0.1, ymax=1.2, color="black", linestyle=(0, (5, 10)))
plt.axvline(x=94, ymin=-0.1, ymax=1.2, color="black", linestyle=(0, (5, 10)))
plt.axvline(x=113, ymin=-0.1, ymax=1.2, color="black", linestyle=(0, (5, 10)))
plt.title('PCA wts')
plt.xlabel('questions')
plt.ylabel('wt')
ax.yaxis.set_label_coords(-0.08,0.5)
ax.legend(loc='upper left', bbox_to_anchor=(0.75, 1.05), shadow=True, ncol=1)
plt.savefig("./results/wts.png")


transform = pca.transform(df1)

fig = plt.figure(figsize=(8,8))
ax = plt.subplot(111)
ax.plot(transform[:, 0], transform[:, 1], 'o', label="Participant", markersize=5)
plt.title('score')
plt.xlabel('PCA1')
plt.ylabel('PCA2')
ax.yaxis.set_label_coords(-0.08,0.5)
ax.legend(loc='upper left', bbox_to_anchor=(0.75, 1.05), shadow=True, ncol=1)
plt.savefig("./results/score.png")

fig = plt.figure(figsize=(8,8))
ax = plt.subplot(111)
for i in range(0, pca.components_.shape[1]):
	ax.plot([pca.components_[0][i], 0], [pca.components_[1][i], 0], 'o-', markersize=5)
plt.title('feature contributions')
plt.xlabel('PCA1')
plt.ylabel('PCA2')
ax.yaxis.set_label_coords(-0.08,0.5)
plt.savefig("./results/wts_1.png")

df1 = pd.read_csv('data_processed/mean_n.csv', index_col=0)
corr = np.zeros(df1.shape[1])

fig = plt.figure(figsize=(8,8))
ax = plt.subplot(111)
for i in range(1, df1.shape[1]+1):
	corr[i-1] = np.correlate(df1["1"].tolist(), df1[str(i)].tolist())
ax.plot(corr, 'o-', markersize=5)
plt.axvline(x=15, ymin=-30, ymax=90, color="black", linestyle=(0, (5, 10)))
plt.axvline(x=39, ymin=-30, ymax=90, color="black", linestyle=(0, (5, 10)))
plt.axvline(x=94, ymin=-30, ymax=90, color="black", linestyle=(0, (5, 10)))
plt.axvline(x=113, ymin=-30, ymax=90, color="black", linestyle=(0, (5, 10)))
plt.title('Correlation of 1st feature with rest')
plt.xlabel('Feature')
plt.ylabel('correlation value')
ax.yaxis.set_label_coords(-0.08,0.5)
plt.savefig("./results/correlation.png")
