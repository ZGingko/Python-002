import pymysql
import pandas as pd

dbInfo = {
    'host': '192.168.1.103',
    'port': 3306,
    'user': 'root',
    'password': 'root123',
    'db': 'learn_python'
}

conn = pymysql.connect(
            host=dbInfo['host'],
            port=dbInfo['port'],
            user=dbInfo['user'],
            password=dbInfo['password'],
            db=dbInfo['db']
        )

data = pd.read_sql("select * from t_pandas_test", conn)

# 1. SELECT * FROM data;
print(data)

# 2. SELECT * FROM data LIMIT 10;
print(data[:10])

# 3. SELECT id FROM data; //id 是 data 表的特定一列
print(data["id"])

# 4. SELECT COUNT(id) FROM data;
print(data["id"].count())

# 5. SELECT * FROM data WHERE id<1000 AND age>30;
print(data[(data["id"] < 1000) & (data["age"] > 30)])

# 6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
# unique()是以 数组形式（numpy.ndarray）返回列的所有唯一值（特征的所有唯一值）
# nunique() Return number of unique elements in the object.即返回的是唯一值的个数
print(data.groupby("id").agg({"order_id": "nunique"}))

# 7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
data1 = pd.read_sql("select * from table1", db)
data2 = pd.read_sql("select * from table2", db)
pd.merge(data1, data2, on="id")

# 8. SELECT * FROM table1 UNION SELECT * FROM table2;
# how的取值‘left’, ‘right’, ‘outer’, ‘inner’
pd.merge(data1, data2, how="outer")

# 9. DELETE FROM table1 WHERE id=10;
# drop内是索引，drop([row_num])删某行，drop(["column_name"],axis=1)删某列
data1 = data1.drop(data1[data1["id" == 10]].index)

# 10. ALTER TABLE table1 DROP COLUMN column_name;
data1 = data1.drop(["column_name"], axis=1)

db.close()
