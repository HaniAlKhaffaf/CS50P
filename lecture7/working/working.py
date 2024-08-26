import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    matches = re.search(r"^(0?[1-9]|1[0-2]):?\.?([0-5][0-9])? (AM|PM) to (0?[1-9]|1[0-2]):?\.?([0-5][0-9])? (AM|PM)$", s)
    if matches:
        first_time = time_to_24hr_format(matches.group(1), matches.group(2), matches.group(3))
        second_time = time_to_24hr_format(matches.group(4), matches.group(5), matches.group(6))
        return f"{first_time} to {second_time}"
    else:
        raise ValueError

def time_to_24hr_format(hr, min, period):
    if min is None or min == "":
        min_24 = "00"
    else:
        min_24 = f"{int(min):02}"
    
    if hr == "12" and period == "AM":
        hr_24 = "00"
    elif hr == "12" and period == "PM":
        hr_24 = "12"
    else:
        hr_24 = f"{int(hr) + 12}" if period == "PM" else f"{int(hr):02}"
    
    return f"{hr_24}:{min_24}"


if __name__ == "__main__":
    main()