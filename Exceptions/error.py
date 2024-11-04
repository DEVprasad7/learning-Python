def get_fuel_percentage():
    while True:
        fraction = input("Fraction: ")

        try:
            x_str, y_str = fraction.split("/")
            x = int(x_str)
            y = int(y_str)

            if y == 0 or x > y:
                pass

            percentage = (x / y) * 100

            rounded_percentage = round(percentage)

            if rounded_percentage <= 1:
                return "E"
            elif rounded_percentage > 100:
                pass
            elif rounded_percentage >= 99:
                return "F"
            else:
                return f"{rounded_percentage}%"

        except (ValueError, ZeroDivisionError):
            pass

if __name__ == "__main__":
    print(get_fuel_percentage())