print("Do you want to compute your average score (Yes or No)")
respone = input()
while respone == "Yes":
    print("Enter students last name")
    lastname = input()
    print("Enter exam score 1")
    score1 = float(input())
    print("Enter score 2")
    score2 = float(input())
    avg = (score1 + score2) / 2
    print(lastname + ", Your average score is " + str(avg))
    print("Do you want to compute your average score (Yes or No)")
    respone = input()
