def main():
    user_date = input("Date: ") 
    if "/" in user_date:
        first_format(user_date)
    else:
        second_format(user_date)


def first_format(date):
    split_date = date.split("/")
    year = split_date[2]
    month = split_date[0]
    day = split_date[1]

    if int(day) < 1 or int(day) > 31:
        main()

    if int(month) < 1 or int(month) > 12:
        main()
    
    if len(month) == 1:
        month = "0" + month

    if len(day) == 1:
        day = "0" + day

    print(f"{year}-{month}-{day}")



def second_format(date):
    split_date = date.split(" ")
    year = split_date[2]
    month = split_date[0].title()
    day = split_date[1].rstrip(",")

    if int(day) < 1 or int(day) > 31:
        main()

    if len(month) == 1:
        month = "0" + month

    if len(day) == 1:
        day = "0" + day
    
    print(f"{year}-{months[month]}-{day}")

months = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12"
}

main()