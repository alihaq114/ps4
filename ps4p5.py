print("do you want to start? ")
start = input()
while start == "yes":
    print("what is the quanitiy of item? ")
    qty = int(input())
    print("what is the price of item? ")
    price = float(input())
    extp = qty * price
    if extp >= 10000:
        dis = extp * 0.25
    else:
        dis = extp * 0.1
    total = extp - dis
    print("your extended price is = " + str(extp))
    print("your discount is = " + str(dis))
    print("your total is = " + str(total))
    print("do you have another order? (yes or no)")
    start = input()
td = dis
print("your total discount is = " + str(td))
