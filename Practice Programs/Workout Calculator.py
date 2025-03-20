import pprint

exercise_list=[]
exercise_dict={}
total_time=0
exercise=''

while exercise != 'c':
    print('What Exercise have you done today? Type c to continue')
    exercise=input()
    if exercise != 'c':
        exercise_list.append(exercise)

for exercise in exercise_list:
    print('How much time did ' + exercise + ' take? (in minutes)')
    time=int(input())
    exercise_dict[exercise] = time
    total_time=total_time+time

print('Total time spent on the exercises : ' + str(total_time) + ' minutes')
pprint.pprint(exercise_dict)


