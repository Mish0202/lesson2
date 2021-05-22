school= [
    {'school_class': '4a', 'scores': [2, 2, 2]}, 
    {'school_class': '4b', 'scores': [4, 4, 4, 4, 4,]},
    {'school_class': '4c', 'scores': [5,5,5,5,5,5,5,]},
    ]
sum = 0
count = 0
for c in school:
    print(c['scores'])
    for score in c['scores']:
        sum += score
        count +=1
        average_score = sum/count
print(average_score)

sum = 0
count = 0
for score in school[0]['scores']:
        print(score)
        sum += score
        count +=1
        average_score_c0 = sum/count
print(average_score_c0)
