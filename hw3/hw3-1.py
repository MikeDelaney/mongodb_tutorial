import pymongo

connection = pymongo.Connection("mongodb://localhost", safe=True)

db = connection.school
students = db.students

cursor = students.find()

for doc in cursor:
    scores = doc['scores']
    lowest = float('inf')
    target_index = 0
    for item in scores:
        if item['type'] == 'homework':
            if item['score'] < lowest:
                target_index = scores.index(item)
    del scores[target_index]
    students.save(doc)
