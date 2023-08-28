import mysql.connector

'''# 执行查询
query = "SELECT * FROM goods"
cursor.execute(query)

# 获取查询结果
result = cursor.fetchall()
for row in result:
    print(row)'''

def add_sql(text):
    # 连接到MySQL数据库
    cnx = mysql.connector.connect(
        host="192.168.1.9",
        user="root",
        password="1017",
        database="python"
    )
    # 创建游标对象
    cursor = cnx.cursor()
    # 插入数据
    insert_query = "INSERT INTO gonggao (name) VALUES (%s)"
    data = (text,)
    cursor.execute(insert_query, data)
    cnx.commit()
    # 关闭游标对象和数据库连接
    cursor.close()
    cnx.close()

def read_gonggao():  #暂时有问题
    # 连接到MySQL数据库
    cnx = mysql.connector.connect(
        host="192.168.1.9",
        user="root",
        password="1017",
        database="python"
    )
    # 创建游标对象
    cursor = cnx.cursor()
    # 执行查询
    query = "SELECT * FROM gonggao"
    cursor.execute(query)
    # 获取查询结果
    result = cursor.fetchall()
    for row in result:
        print(row)
    pass