import mysql.connector

#连接数据库
conn = mysql.connector.connect(user='root', password='root', database='test')
cursor = conn.cursor()
sql_select = "select * from cnkiinfotest"

try:
    cursor.execute(sql_select)
    result = cursor.fetchall()

    for row in result:
        id = row[0]
        print(id)
        
        # 清除title、abstract、keywords任意为null的项
        if row[1] == None or row[5] == None or row[6] == None:
            cursor.execute("delete from cnkiinfotest where id = %d" % (row[0]))
            conn.commit()
        
        # 将title内无用空格去除
        print(row[1].strip())
        cursor.execute("UPDATE cnkiinfotest SET title = \'%s\' WHERE id = %d" %(row[1].strip(),row[0]))
        conn.commit()
        """
        if row[1] != '':
            title = row[1]
            print("title:" + title.strip())
        if row[5] != '':
            abstracts = row[5]
            print("abstract" + abstracts)
        if row[6] != '':
            keywords = row[6]
            print("keyword:" + keywords)
        # 打印结果
        """

except:
    print("Error: unable to fecth data")

#清理后，id删除重做
cursor.execute("ALTER  TABLE  cnkiinfotest DROP id")
conn.commit()
cursor.execute("ALTER  TABLE  cnkiinfotest ADD id mediumint(6) PRIMARY KEY NOT NULL AUTO_INCREMENT FIRST")
conn.commit()

conn.close()
