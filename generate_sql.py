# Author: Yoanndp
import sys

def main():
    # Check if the correct number of arguments were passed
    if len(sys.argv) != 3:
        print(f"Usage: python3 {sys.argv[0]} <input_file> <output_file>")
        sys.exit(1)

    # Get the input and output file names
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Read the input file
    with open(input_file, "r") as f:
        lines = f.readlines()

    # Write the output file
    with open(output_file, "w") as f:
        for line in lines:
            try:
                # Split the line into the name and value
                name, value = line.strip().split("|")
                # Build the query
                query = f"UPDATE Flags SET boolVal = {value} WHERE name = \"{name}\";"
                # Write the query to the output file (note: the "\n" isn't mandatory)
                f.write(f"{query}\n")
            except ValueError:
                # If the line doesn't have the correct format, print an error and exit
                print(f"Invalid line: {line}")
                sys.exit(1)
            except Exception as e:
                # If there was an error, print it and exit
                print(f"Error: {e}")
                sys.exit(1)

if __name__ == "__main__":
    main()