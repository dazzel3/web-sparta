from pymongo import MongoClient           # pymongo를 쓰겠다.
client = MongoClient('localhost', 27017)  # 내 컴퓨터에서 지금 돌아가고 있는데 mongoDB에 접속하겠다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만든다.

# MongoDB에 insert 하기
db.users.insert_one({'name':'bobby','age':21}) # db 안에 'users'라는 collection에 {'name':'bobby','age':21}를 insert한다.
db.users.insert_one({'name':'kay','age':27})
db.users.insert_one({'name':'john','age':30})
db.users.insert_one({'name':'jane','age':21})

# find 데이터 여러개 가져올 때
same_ages = list(db.users.find({'age':21},{'_id':False})) # age가 21인 데이터를 찾고, 임의의 값으로 주어지는 _id값은 나타내지 말기. 그리고 그 데이터들은 딕셔너리 형태로 리스트에 들어감
all = list(db.users.find({}, {'_id': False})) # db의 users라는 컬렉션의 모든 데이터를 _id값 빼고 리스트에 넣어라
for i in all:
    print(i)

# find 데이터 하나 가져올 때
user = db.users.find_one({'name':'bobby'}, {'_id': False}) # 이름이 bobby인 데이터 하나만 가져와라. 만약 여러개 있다면 제일 위에 있는 값을 가져옴
print(user)

# update
db.users.update_one({'name':'bobby'},{'$set':{'age':19}}) # 이름이 bobby인 데이터를 찾아서 age를 19로 바꿔라.

# delete
db.users.delete_one({'name':'bobby'}) # 이름이 bobby인 데이터를 찾아서 삭제해라.