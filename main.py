
f = open("study_data.csv")

hours = []
scores = []
next(f)
for line in f:
    line = line.split(",")
    hours.append(int(line[0]))
    scores.append(int(line[1]))
# m = (scores[1]-scores[0]) / (hours[1]-hours[0])
n = len(scores)
sum_y= 0
sum_x = 0
sum_xy = 0
sum_x2= 0

for i in range(n):
    sum_x += (hours[i]) 
    sum_y += (scores[i]) 
    sum_xy += (hours[i] * scores[i])
    sum_x2 += (hours[i]) **2

m = (n* sum_xy - sum_x*sum_y) / (n* sum_x2-(sum_x**2))
b = (sum_y - m*sum_x)/n

user_x = float(input("Enter the number of hours you studied:\n"))
user_score = m*user_x + b

if user_x<0:
    print("Invalid Input")
else:
    print(f"If you study {user_x:.2f} hours, predicted score is {user_score:.2f}")
f.close()


