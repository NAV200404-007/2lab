def calculate_bmi(height,weight):
    print("Height=" + str(height))
    print("Weight=" + str(weight))

    bmi = weight/(height*height)
    print(bmi)

    if(bmi < 18.5):
        print("Under weight")
        return -1
    elif(bmi <= 25):
        print("Normal Weight")
        return 0
    else:
        print("Over Weight")
        return 1

calculate_bmi(weight=79,height=1.80)

