import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="PSH",
  password="conet2025",
  database='test'
)
print(mydb)
# mycursor = mydb.cursor()
# sql = "insert into app_user (name,age) values (%s,%s)"
# val = ('권율',35)
# mycursor.execute(sql,val)
# mydb.commit()
# print(mycursor.rowcount, " record inserted")

# mycursor = mydb.cursor(dictionary=True) # 원래 리턴은 튜플이지만 dictionary = true 를 주면 리턴이 키:밸류 딕셔너리 형태로 나옴
# sql = "select * from app_user"
# mycursor.execute(sql)
# myresult = mycursor.fetchall() # 여러명의 정보를 가져옴

# for x in myresult:
#     print(x)

# print(myresult[0]['name']) # 딕셔너리에서 값 추출하는 방식입니다. 이 방식은 여러 행이 있을 때, 특정 행을 선택해서 값을 꺼내는 데 유용합니다.

# mycursor = mydb.cursor(dictionary=True) # dictionary = true 를 주면 리턴이 키:밸류 딕셔너리 형태로 나옴
# sql = "select * from app_user where id =4"
# mycursor.execute(sql)
# myresult = mycursor.fetchone() # 한 행의 정보만을 가져옴


# print(myresult['name'],myresult['age']) #myresult가 딕셔너리일 때만 유효합니다. 즉, myresult가 단일 딕셔너리일 때

# mycursor = mydb.cursor(dictionary=True)
# sql = "select * from app_user where age =%s"
# val=(35,)
# mycursor.execute(sql, val)
# myresult = mycursor.fetchall()

# for x in myresult:
#     print(x)
# mydb.close() # 반드시 해줘야함 초보개발자의 흔산 실수
# 요즘은 db-pool을 사용해서 10개씩 db에 계속 연결해서 python에서 연결했다 끊었다하는게 효율이 훨씬 좋음
# sql injection 방지를위해 placeholder를 쓰는게 좋다

# mycursor = mydb.cursor(dictionary=True)
# sql = "select * from app_user order by NAME desc"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()

# for x in myresult:
#     print(x)

mycursor = mydb.cursor(dictionary=True)
sql = "delete from app_user where name=%s"
val = ('신사임당',)
mycursor.execute(sql,val)
mydb.commit()