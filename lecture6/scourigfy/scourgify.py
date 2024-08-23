import sys, csv

student = []

def main():
    if len(sys.argv) < 3:
        sys.exit("missing command-line argument")
    elif len(sys.argv) > 3:
        sys.exit("Too many argumnts")
    read_file_name = sys.argv[1]
    write_file_name = sys.argv[2]

    read_file(read_file_name)
    write_file(write_file_name)

def read_file(file_name):
    counter = 0
    try:
        with open(file_name, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                counter += 1
                if counter == 1:
                    student.append({"first": "first", "last": "last", "house": "house"})
                    continue
                full_name = row[0].strip("'")  
                house = row[1].strip("'")      
                last, first = full_name.split(", ")
                student.append({"first": first, "last": last, "house": house})
    except FileNotFoundError:
        sys.exit("The file was not found. Please check the file path and try again.")

def write_file(file_name):
    try:
        with open(file_name, "a") as file:
            writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
            for row in student:
                writer.writerow(row)
    except:
        print("error happening") 

if __name__ == "__main__":
    main()