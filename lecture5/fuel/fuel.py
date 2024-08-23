def main():
    user_input = input("Fraction: ")
    percentage_result = convert(user_input)
    final_result = gauge(percentage_result)
    print(final_result)

def convert(fraction):
    try:
        numerator, denominator = fraction.split('/')
        value_x = int(numerator)
        value_y = int(denominator)
        
        if value_y == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")
        if value_x > value_y:
            raise ValueError("Numerator is greater than denominator.")
        
        result = value_x / value_y
        return result * 100
    
    except ValueError as ve:
        print(f"Value Error: {ve}")
        raise
    except ZeroDivisionError as zde:
        print(f"Zero Division Error: {zde}")
        raise


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
