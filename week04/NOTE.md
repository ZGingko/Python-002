### 学习笔记

#### pandas
类似于Python + Excel的组合工具。用来进行数据的清洗，切片以及重组合聚。  
pandas 中文文档：https://www.pypandas.cn/   
Numpy 学习文档：https://numpy.org/doc/  
matplotlib 学习文档：https://matplotlib.org/contents.html  
pandas最擅长的就是数据的预处理和清洗  

pandas基本数据类型  
Series: 相当于excel中的一列 (但是Series会自动加上可更改索引)  
DataFrame: 相当于excel的多行和多列的一种结构 (类似于excel的表格)  

pandas数据导入  
pandas支持大量格式的导入，使用的是read_*()的形式， 比如pd.read_excel(r'test.xlsx')  
pandas数据预处理  

缺失值处理:  
爬虫反复爬取数据填补  
用数学函数来补充 df.ffill()  
非技术手段补全  

重复值处理:  
爬取数据重复，比如时间不同但是内容相同  
多个用户提交的内容是一致的  

pandas数据调整  
行列调整
df.iloc[:, [0, 2]] # 所有行， 获得第一列和第三列  
df.loc[0:2] # 第一行到第三行   
比较  
df[ (df['A'] < 5) & ( df['C'] < 4) ]  
替换  
df['C'].replace(4, 40)  
排序  
df.sort_values( by = ['A'], ascending = False)  
删除  
df.drop('A', axis = 1)  
df.drop(3, axis = 0)  
行列互换  
df.T  
df.T.T  
小收获
用os.path.dirname(os.path.realpath(file)) 以及 os.path.join(pwd, 'file.csv') 来从绝对路径来读取文件。 但是这个方法对于交互模式的运行是不太好用的.