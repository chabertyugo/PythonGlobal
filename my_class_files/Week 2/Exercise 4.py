age = input("What is your age?").strip()
sex = input("What is your sex?").strip().upper()
age = int(age)
if age <=22 and sex == "M":
    print("You have been selected for this trial!")
elif age>22:
    print("Unfortunately, you are too old for this trial!")
elif sex != "M":
    print("Unfortunately, you must be male to participate in this trial!")
elif age>22 and sex!="M":
    print("Unfortunately, you must be a male under 22 years of age to participate")