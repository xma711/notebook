from sklearn.datasets import make_classification
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# create dataset
n_samples = 1000
X, y = make_classification(	n_samples=n_samples,
				n_features=7,
				n_informative=4,
				n_redundant=2,
				n_repeated=0,
				n_classes=2,
				n_clusters_per_class=1,
				weights=[0.6, 0.4],
				flip_y=0.05,
				class_sep=0.8,
				random_state=2)

print ("X.shape = {}".format(X.shape))

pca = PCA(n_components=2)

pca.fit(X)

Xt = pca.transform(X)

print ("Xt.shape = {}".format(Xt.shape))


def plot_2d_points(Xt, y, ax, title):
	colors = ['red', 'blue']
	ax.scatter(Xt[:,0], Xt[:,1], c=y, cmap=ListedColormap(colors), edgecolor='k')
	ax.set_title(title)

fig, ((ax1, ax2)) = plt.subplots(1, 2, figsize=(15, 12))

plot_2d_points(X, y, ax1, 'Original first 2 dimensions')
plot_2d_points(Xt, y, ax2, 'First 2 principal dimensions')

plt.show()
