# Conversion functions
def metric_to_imperial_length(metric_value):
    # Conversion factor: 1 meter = 3.28084 feets.
    imperial_value = metric_value * 3.28084
    return imperial_value

def metric_to_imperial_weight(metric_value):
    # Conversion factor: 1 kilogram = 2.20462 pounds.
    imperial_value = metric_value * 2.20462
    return imperial_value

# User-friendly interface
print("Metric to Imperial Converter")

while True:
    print("\nChoose a conversion option:")
    print("1. Convert length (meters to feet)")
    print("2. Convert weight (kilograms to pounds)")
    print("3. Quit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        metric_value = float(input("Enter a length in meters: "))
        imperial_value = metric_to_imperial_length(metric_value)
        print(f"{metric_value} meters is approximately {imperial_value} feet.")
    elif choice == '2':
        metric_value = float(input("Enter a weight in kilograms: "))
        imperial_value = metric_to_imperial_weight(metric_value)
        print(f"{metric_value} kilograms is approximately {imperial_value} pounds.")
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
