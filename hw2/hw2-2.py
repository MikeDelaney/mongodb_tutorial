import pymongo

connection = pymongo.Connection("mongodb://localhost", safe=True)

db = connection.students
grades = db.grades

query = {'type': 'homework'}

cursor = grades.find(query).sort([('student_id', pymongo.ASCENDING),
                                  ('score', pymongo.ASCENDING)])
target_id = -1

for doc in cursor:
    if doc['student_id'] != target_id:
        target_id = doc['student_id']
        grades.remove({'_id': doc['_id']})
