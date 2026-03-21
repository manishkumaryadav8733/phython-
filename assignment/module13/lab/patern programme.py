# This program prints a star pattern

for i in range(1, 6):       # Outer loop
    for j in range(i):      # Inner loop
        print("*", end="")  # Print without new line
    print()                 # Move to next line