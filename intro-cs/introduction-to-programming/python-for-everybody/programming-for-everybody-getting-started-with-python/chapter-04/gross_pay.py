def computepay(h, r):
    if h > 40:
        extra_hour = h - 40
        return extra_hour * r * 1.5 + 40 * r
    return h * r

hrs = int(input("Enter Hours: "))
rate = float(input("Enter Rate: "))
pay = computepay(hrs, rate)
print("Pay", pay)