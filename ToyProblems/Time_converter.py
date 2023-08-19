def time_converter(hour, min, period):
   
    if period == "am" and min <= 60:
        if hour == 12:
            hour = 0
            print(f"{hour :02d}{min} hrs")
        elif 1 <= hour <= 11:
            print(f"{hour :02d}{min} hrs")
    
    elif period == "pm" and min <= 60:
        if hour == 12:
            print(f"{hour}{min} hrs")
        elif 1 <= hour <= 11:
            print(f"{hour + 12}{min} hrs")
            
    else:
        print("Invalid format")
         
time_converter(int(input("Hour: ")), int(input("Min: ")), input("am/pm: "))
