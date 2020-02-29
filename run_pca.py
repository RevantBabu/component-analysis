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


df1 = pd.read_csv('data_processed/' + sys.argv[1] + '_n.csv', index_col=0)
df1 = StandardScaler().fit_transform(df1)

#custom compute: covariance -> eigen_values
cov_mat = np.cov(df1)
eig_vals, eig_vecs = np.linalg.eig(cov_mat)

var_exp = [(i / sum(eig_vals)) for i in sorted(eig_vals, reverse=True)]

#use sklearn lib
pca = sklearnPCA().fit(df1)


#plot variance explined by each component & cumulative
fig = plt.figure(figsize=(8,8))
ax = plt.subplot(111)
ax.plot(pca.explained_variance_ratio_, 'o-', label="component\_lib", markersize=0.4)
ax.plot(np.cumsum(pca.explained_variance_ratio_), 'o-', label="cumulative\_lib", markersize=0.4)
ax.plot(var_exp, 'o-', label="component", markersize=0.4)
ax.plot(np.cumsum(var_exp), 'o-', label="cumulative", markersize=0.4)
plt.title('PCA')
plt.xlabel('components')
plt.ylabel('explained variance')
ax.yaxis.set_label_coords(-0.08,0.5)
ax.legend(loc='upper left', bbox_to_anchor=(0.55, 0.55), shadow=True, ncol=1)
plt.savefig("./results/" + sys.argv[1] + ".png")
