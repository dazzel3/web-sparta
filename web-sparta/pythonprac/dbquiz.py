from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# 영화제목 '매트릭스'의 평점 가져오기
movie = db.movies.find_one({'title':'매트릭스'}, {'_id': False})
print(movie['point'])

# '매트릭스'의 평점과 같은 평점의 영화 제목들을 가져오기
movie_point = movie['point']
same_point = list(db.movies.find({'point': movie_point}, {'_id': False}))
for sp in same_point:
    print(sp['title'])

# 매트릭스 영화의 평점을 0으로 만들기
db.movies.update_one({'title':'매트릭스'},{'$set':{'point':0}})