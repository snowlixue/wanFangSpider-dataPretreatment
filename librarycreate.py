import mysql.connector
import jieba

conn = mysql.connector.connect(user='root', password='root', database='test')
cursor = conn.cursor()

f = open("./abstract.txt", "w", encoding='UTF-8')

#将abstract写入txt，为训练词向量准备
try:
    cursor.execute("select * from cnkiinfotest")
    results = cursor.fetchall()
    for row in results:
        print("abstract"+row[5])
        wordlist = jieba.cut(row[5])
        for word in wordlist:
            f.write(word)
            f.write(" ")
        f.write("\n")

except:
    print("something wrong,can't featch all")

conn.close()