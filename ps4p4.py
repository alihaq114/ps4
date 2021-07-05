numEmp = 0
totGp = 0
print("Do you want to start? (yes or no)")
start = input()
while start == "yes":
    numEmp = numEmp + 1
    print("what is your last name")
    lastname = input()
    print("how many hours worked?")
    hw = int(input())
    print("what is the rate of pay")
    rop = int(input())
    if hw >= 40:
        gp = 40 * rop + (40 - hw) * rop
    else:
        gp = hw * rop
    totGp = totGp + gp
    print(lastname + ", gross pay: " + str(gp))
    print("Do you want to start again?")
    start = input()
print("Total Employee Gross Pay: " + str(totGp))
print("Total Employees: " + str(numEmp))
