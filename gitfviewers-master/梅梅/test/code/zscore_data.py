#-*- coding: utf-8 -*-
#标准差标准化

import pandas as pd

datafile = '../data/zscoredata.xls' #data need to be standard score
zscoredfile = '../tmp/zscoreddata.xls' #data after standard score
#标准化处理
data = pd.read_excel(datafile)
data = (data - data.mean(axis = 0))/(data.std(axis = 0)) # z=(x-μ)/σ
data.columns=['Z'+i for i in data.columns] # rename the head of table

data.to_excel(zscoredfile, index = False)