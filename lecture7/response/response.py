from validator_collection import validators, errors

def main():
    print(email_validate(input("Email: ")))

def email_validate(email):

    try:
        valid_email = validators.email(email)
        print(f"'{valid_email}' is a valid email.")
        return "Valid" 

    except errors.InvalidEmailError:
        print(f"'{email}' is not a valid email.")
        return "Invalid" 


main()
