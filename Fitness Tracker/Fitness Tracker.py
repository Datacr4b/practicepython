#
# Fitness tracker.py - Program to calculate your total time and store data. WIP
#

class Workout:

    total = 0

    def __init__(self, name, time_spent, date):
        self.name = name
        self.time_spent = time_spent
        self.date = date

        Workout.total += 1

    def showdata(self):
        return f'Time spent on {self.name} is {self.time_spent} min on {self.date}'


# Variable Statements
total_time = 0 # statement for the program
current_data = 'a'
class_list = [] # list for the workout instances

# TODO: ASK TO REMOVE DATA OR SPECIFIC DATA
# TODO: PANDAS

# Question loop - ask for info input
while True:
    name = input("Type the exercise that you've done today (type q to quit): ")
    if name.lower() == 'q':
        break
    time_spent = input("Type the time spent on the exercise in minutes (type q to quit): ")
    if time_spent.lower() == 'q':
        break
    date = input("Type the date of the exercise (type q to quit): ")
    if date.lower() == 'q':
        break

    # NOTE DOWN DATA IN FILE
    with open("Fitness.txt", 'a') as file:
        file.write(f'{name},{time_spent},{date},\n')

# OPEN FILE IN READ AND PUT DATA IN OBJECT INSTANCE
with open("Fitness.txt", 'r') as file:
    for line in file.readlines():
        object_inst=line.split(',')

        # INITIATE INSTANCE
        workout = Workout(object_inst[0], int(object_inst[1]), object_inst[2])
        class_list.append(workout) # PUT ALL OBJECTS IN LIST

# CALCULATE THE TOTAL TIME SPENT
for i in range(0,len(class_list)):
    total_time += class_list[i].time_spent

# SHOW TIME AND DATE FOR EVERY WORKOUT
for i in range(0,len(class_list)):
    print(class_list[i].showdata())

print(f'Here is the total time spent on all exercises : {total_time} min')
print(f'Total Workouts {Workout.total}')

