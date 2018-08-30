#-*- coding: utf-8 -*-
#K-Means聚类算法

import pandas as pd
from sklearn.cluster import KMeans #导入K均值聚类算法
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':

  inputfile = '../result/zscoreddata.xls' #待聚类的数据文件
  k = 5                       #需要进行的聚类类别数

#读取数据并进行聚类分析
  data = pd.read_excel(inputfile) #读取数据

#调用k-means算法，进行聚类分析
  kmodel = KMeans(n_clusters = k, n_jobs = 4) #n_jobs是并行数，一般等于CPU数较好
  kmodel.fit(data) #训练模型

  kmodel.cluster_centers_ #查看聚类中心
  kmodel.labels_ #查看各样本对应的类别

  labels = data.columns  # 标签
  k = 5  # 数据个数
  plot_data = kmodel.cluster_centers_
  color = ['b', 'g', 'r', 'c', 'y']  # 指定颜色

  for i in range(len(plot_data)):
    print(plot_data[i])

  angles = np.linspace(0, 2 * np.pi, k, endpoint=False)
  plot_data = np.concatenate((plot_data, plot_data[:, [0]]), axis=1)  # 闭合
  angles = np.concatenate((angles, [angles[0]]))  # 闭合

  fig = plt.figure()
  ax = fig.add_subplot(111, polar=True)  # polar参数！！
  for i in range(len(plot_data)):
      ax.plot(angles, plot_data[i], 'o-', color=color[i], label=u'CG' + str(i), linewidth=2)  # 画线

  ax.set_rgrids(np.arange(0.01, 3.5, 0.5), np.arange(-1, 2.5, 0.5), fontproperties="SimHei")
  ax.set_thetagrids(angles * 180 / np.pi, labels, fontproperties="SimHei")
  plt.legend(loc=4)
  plt.show()





