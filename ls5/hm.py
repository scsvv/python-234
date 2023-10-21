# ->
max_value, min_value = None, None
while True:
    data = input("Type number (from -inf to +inf): ")

    # case is a Number
    try:
        data = int(data)
    except ValueError:
        print("No Valid data")
        continue

    # case
    if data == 0:
        break

    if not (max_value):
        max_value = data
        min_value = data
        continue

    if data > max_value:
        max_value = data
    elif data < min_value:
        min_value = data

print("Exit with status 1")
print(f"Max: {max_value or 'N/A'}, min: {min_value or 'N/A'}")

# Aaron Aaron - 1 list - 1_000_000 -> break; -> 2_000_000_000 -> 5_000 -> ?) -> break;
