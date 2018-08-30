#-*- coding: utf-8 -*- 
#对数据进行基本的探索
#返回缺失值个数以及最大最小值

import pandas as pd

datafile= '../data/air_data.csv'  #raw data from airline compnany
resultfile = '../result/explore.xls'  #dataset after explore

data = pd.read_csv(datafile, encoding = 'utf-8') #read the raw data

explore = data.describe(percentiles = [], include = 'all').T
# summury for data    T is transport matrix, which is convinient for viewing data
#‘all’ : All columns of the input will be included in the output.
explore['null'] = len(data)-explore['count'] # count() only count the record which is not null

explore = explore[['null', 'max', 'min']]
explore.columns = [u'null value', u'max ', u'min '] #rename the head of table

'''这里只选取部分探索结果。
describe()函数自动计算的字段有count（非空值数）、unique（唯一值数）、top（频数最高者）、freq（最高频数）、mean（平均值）、std（方差）、min（最小值）、50%（中位数）、max（最大值）'''

explore.to_excel(resultfile) # output the result