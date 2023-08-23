def time_converter(hour, min, period):
   
    if period == "am" and min < 60:
        if hour == 12:
            hour = 0
            print(f"{hour :02d}{min :02d} hrs")
        elif 1 <= hour <= 11:
            print(f"{hour :02d}{min :02d} hrs")
    
    elif period == "pm" and min < 60:
        if hour == 12:
            print(f"{hour}{min :02d} hrs")
        elif 1 <= hour <= 11:
            print(f"{hour + 12}{min :02d} hrs")
            
    else:
        print("Invalid Time format")
# Takes in inputs as arguments and passes them to the time converter function        
time_converter(int(input("Hour: ")), int(input("Min: ")), input("am/pm: "))
