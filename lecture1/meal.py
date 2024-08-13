def main():
    userTime = input("What time is it? ")
    time = convert(userTime)
    if 7 <= time <= 8:
        print("breakfast time")
    if 12 <= time <= 13:
        print("lunch time")
    if 18 <= time <= 19:
        print("dinner time")


def convert(time):
    if ":" in time:
        timeInFloat = time.replace(":", ".")
        hours, minutes = timeInFloat.split(".")
        finalResult = float(hours) + float(minutes) / 60
        return finalResult
    else:
        return float(time)

main() 