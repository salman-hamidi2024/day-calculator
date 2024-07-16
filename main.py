def day_calculator(x):
    global year_days
    global mounth_days
    global days
    all_days = []
    person1 = '14-01-1999'
    day1 = int(person1[0:2])
    mounth1 = int(person1[3:5])
    year1 = int(person1[6:10])
    # person2 = '16-03-2024'
    day2 = int(x[0:2])
    mounth2 = int(x[3:5])
    year2 = int(x[6:10])
    year_days = year2 - year1 
    mounth_days = mounth2 - mounth1 
    days = day2 - day1
    all_days.append(days)
    all_days.append(mounth_days * 30)
    all_days.append(year_days * 365)
    return sum(all_days)
try:
    user_input = input("wich date do you want: ")
    if user_input > '14-01-1999':
        print(f"salman is {day_calculator(user_input)} from your date")
        print(f"salman is {year_days} years and {mounth_days} and {days} old")
    else:
        print("Not yet born")
except ValueError:
    print("you date should have 10 characters")