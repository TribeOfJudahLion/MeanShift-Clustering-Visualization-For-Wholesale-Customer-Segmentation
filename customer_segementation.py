import pandas as pd
import numpy as np
from sklearn.cluster import MeanShift, estimate_bandwidth
import matplotlib.pyplot as plt

def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def perform_clustering(X):
    bandwidth = estimate_bandwidth(X, quantile=0.8, n_samples=len(X))
    meanshift = MeanShift(bandwidth=bandwidth, bin_seeding=True)
    meanshift.fit(X)
    return meanshift.labels_, meanshift.cluster_centers_

def plot_clusters(centroids, names):
    plt.figure(figsize=(10, 6))
    plt.scatter(centroids[:, 1], centroids[:, 2], s=100, edgecolors='k', facecolors='none')

    for i, centroid in enumerate(centroids):
        plt.annotate(f'Cluster {i}', (centroid[1], centroid[2]), textcoords="offset points", xytext=(0,10), ha='center')

    plt.xlabel(names[1])
    plt.ylabel(names[2])
    plt.title('Centroids of Clusters for Milk and Groceries')
    plt.grid(True)
    plt.show()

def main():
    input_file = 'wholesale.csv'
    data = load_data(input_file)

    if data is not None:
        X = data.values[:, 2:]
        labels, centroids = perform_clustering(X)
        num_clusters = len(np.unique(labels))

        print("Number of clusters in input data =", num_clusters)
        print("Centroids of clusters:")
        print('\t'.join([name[:3] for name in data.columns[2:]]))
        for centroid in centroids:
            print('\t'.join([str(int(x)) for x in centroid]))

        plot_clusters(centroids, data.columns)

if __name__ == "__main__":
    main()
