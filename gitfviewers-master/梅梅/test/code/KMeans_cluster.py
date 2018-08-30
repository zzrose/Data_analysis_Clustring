#-*- coding: utf-8 -*-
#K-Means聚类算法

import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    inputfile = '../tmp/zscoreddata.xls'
    k = 5

    data = pd.read_excel(inputfile) #

 #use the k-means algorithm to do the cluster analysis
    kmodel = KMeans(n_clusters = k, n_jobs = 4)
  # n_jobs : int
  # The number of jobs to use for the computation.
  #  This works by computing each of the n_init runs in parallel.


    kmodel.fit(data) # fit(X[, y])	Compute k-means clustering.

    kmodel.cluster_centers_ # Coordinates of cluster centers
    kmodel.labels_ #Labels of each point

    # draw polar
    labels = data.columns  # label
    k = 5  # 数据个数
    plot_data = kmodel.cluster_centers_
    color = ['b', 'g', 'r', 'c', 'y']  # color

    angles = np.linspace(0, 2 * np.pi, k, endpoint=False)
    plot_data = np.concatenate((plot_data, plot_data[:, [0]]), axis=1)  # 闭合
    angles = np.concatenate((angles, [angles[0]]))  # 闭合

    fig = plt.figure()
    ax = fig.add_subplot(111, polar=True)  # polar参数！！
    for i in range(len(plot_data)):
        ax.plot(angles, plot_data[i], 'o-', color=color[i], label=u'客户群' + str(i), linewidth=2)  # 画线

    ax.set_rgrids(np.arange(0.01, 3.5, 0.5), np.arange(-1, 2.5, 0.5), fontproperties="SimHei")
    ax.set_thetagrids(angles * 180 / np.pi, labels, fontproperties="SimHei")
    plt.legend(loc=4)
    plt.show()


