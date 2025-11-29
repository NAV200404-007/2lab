from Lab2 import calc_average, calc_median_temperature, display_main_menu, find_min_max, get_user_input, sort_temperature


def main():
    while True:
        display_main_menu()
        print("1. Enter temperatures")
        print("2. Calculate average")
        print("3. Find min & max")
        print("4. Sort temperatures")
        print("5. Calculate median")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            temps = get_user_input()

        elif choice == "2":
            print("Average =", calc_average(temps))

        elif choice == "3":
            minimum, maximum = find_min_max(temps)
            print("Min =", minimum, "Max =", maximum)

        elif choice == "4":
            print("Sorted =", sort_temperature(temps))

        elif choice == "5":
            print("Median =", calc_median_temperature(temps))

        elif choice == "0":
            print("Exiting…")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()

