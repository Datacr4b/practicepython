#
# Fitness tracker.py - Program to calculate your total time and store data. WIP
#


# Variable Statements
total_time = 0 # statement for the program
data_dict = {} # dictionary for the fitness data

# TODO: ASK TO REMOVE DATA OR SPECIFIC DATA
# TODO: PANDAS

# Question loop - ask for info input
while True:
    exercise = input("Type the exercise that you've done today (type q to quit): ")
    if exercise.lower() == 'q':
        break
    time_spent = input("Type the time spent on the exercise in minutes (type q to quit): ")
    if time_spent.lower() == 'q':
        break
    date_exercise = input("Type the date of the exercise (type q to quit): ")
    if date_exercise.lower() == 'q':
        break
    # NOTE DOWN DATA IN FILE IN DICT FORMAT FOR EASY ACCESS
    file = open("Fitness.txt", 'a')
    file.write(f'{date_exercise},{exercise},{time_spent},\n')
    file.close()

# OPEN FILE IN READ AND PUT DATA IN DICT
file = open("Fitness.txt", 'r')
for line in file.readlines():
    line_list=line.split(',')
    if line_list[0].lower == current_data[0].lower:
        data_dict[current_data[0]].append(line_list[1])
        data_dict[current_data[0]].append(line_list[2])
        current_data = line_list
    else:
        current_data = line_list
        data_dict[line_list[0]] = [line_list[1],line_list[2]]

file.close()

# CALCULATE THE TOTAL TIME SPENT
for time in data_dict.values():
    for k in range(0,len(time),2):
        total_time += int(time[k+1])

# SHOW TIME FOR EVERY EXERCISE
for exercise, time_and_date in data_dict.items():
    print(f'Time spent on {exercise} is {time_and_date[0]} min on {time_and_date[1]}')

print(f'Here is the total time spent on all exercises : {total_time} min')

