def check_if_positive(a,b,c):
    num_list = []
    num_list.extend([a,b,c])
    count = 0

    for num in num_list:
        count = count + 1 if num > 0 and num % 2 == 0 else count
               
    # Checks if exactly two numbers are divisible by 2    
    if count == 2:
        print("True")
    else:
        print("False")

# Takes three number inputs and passes them to the function    
check_if_positive(int(input("Num1: ")), int(input("Num2: ")), int(input("Num3: ")))