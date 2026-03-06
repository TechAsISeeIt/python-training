def sum(a: float, b: float) -> float | None:
    """
    sum is a function that takes two float arguments and returns their sum.

    Args:
        a (float): Operand for addition
        b (float): Operand for addition
    Raises:
        TypeError: Raised when input validation is failed
    Returns:
        float|None: Returns either sum of operands or None in case of exception
    """
    try:
        if a is None or b is None:
            raise TypeError(
                "Both arguments must be of type float"
            )  # Checking for None values and raising a TypeError if either argument is None
        return a + b
    except TypeError:
        print("Error: Both arguments must be of type float")


def read_binary_file(
    file_path: str,
) -> None:  # Strict type hinting for the file path and return type
    """
    read_binary_file is a function that takes a file path as input
    and reads the contents of the specified binary file.

    Args:
        file_path (str): File Path to read the binary file from
    """
    with open(
        file_path, "rb"
    ) as f:  # Using a context manager to ensure the file is properly closed after reading
        data = (
            f.read()
        )  # Reading the entire contents of the binary file into a bytes variable
    print(data)  # Returning the contents of the binary file as bytes


def append_to_file(
    file_path: str, data: str
) -> None:  # Strict type hinting for the file path, data, and return type
    """
    append_to_file is a function that takes a file path and data as input and appends the data to the specified file.

    'a' mode is used to append to the file.
    If the file already exists, the new data will be added to the end of the file.
    If the file does not exist, it will be created.

    Args:
        file_path (str): File Path to append the data to
        data (str): Content to append to the file
    """
    with open(
        file_path, "a"
    ) as f:  # Using a context manager to ensure the file is properly closed after writing
        f.write(
            data + "\n"
        )  # Appending the provided data followed by a newline character to the file


def write_to_file(
    file_path: str, data: str
) -> None:  # Strict type hinting for the file path, data, and return type
    """
    write_to_file is a function that takes a file path and data as input and writes the data to the specified file.

    'w' mode is used to write to the file.
    If the file already exists, it will be overwritten.
    If the file does not exist, it will be created.

    Args:
        file_path (str): File Path to write the data to
        data (str): Content to write to the file
    """
    with open(
        file_path, "w"
    ) as f:  # Using a context manager to ensure the file is properly closed after writing
        f.write(data)  # Writing the provided data to the file


def read_lines(
    file_path: str,
) -> None:  # Strict type hinting for the file path and return type
    """
    read_lines is a function that takes a file path as input
    and reads the contents of the specified file line by line.

    Args:
        file_path (str): file path to read the file from
    """
    try:
        with open(
            file_path, "r"
        ) as f:  # Using a context manager to ensure the file is properly closed after reading
            for line in f:  # Iterating through each line in the file
                print(
                    f"Line: {line.strip()}"
                )  # Printing each line after stripping leading and trailing whitespace
    # except FileNotFoundError:  # Handling the case where the specified file does not exist
    #     print(f"Error: The file '{file_path}' was not found.")
    except (
        Exception
    ) as e:  # Catching any other unexpected exceptions that may occur during file reading
        print(
            f"An unexpected error occurred while reading the file '{file_path}'.\n Exception: {e}"
        )
    finally:  # The finally block will execute regardless of whether an exception was raised or not
        print(
            f"Finished attempting to read the file '{file_path}'."
        )  # Indicating that the file reading attempt has completed


def read_file(
    file_path: str,
) -> str:  # Strict type hinting for the file path and return type
    """

    read_file is a function that takes a file path as input and reads the entire contents of the specified file.
    Args:
        file_path (str): File Path to read the file from
    Returns:
        str: Returns the contents of the file as a string
    """
    with open(
        file_path, "r"
    ) as file:  # Using a context manager to ensure the file is properly closed after reading
        data = (
            file.read()
        )  # Reading the entire contents of the file into a string variable
    return data  # Returning the contents of the file as a string


def main():
    print("===============Init===============")
    read_lines(
        "sampledata/data.txt"
    )  # Calling the function to read lines from the specified file

    print("===============After Writing===============")
    append_to_file("sampledata/newfile.txt", "This is additional content for the file")
    read_lines("sampledata/newfile.txt")

    # print("===============Reading Binary File===============")
    # read_binary_file(
    #     "sampledata/GitFlow.png"
    # )  # Calling the function to read a binary file

    print("===exception handling===")
    read_lines(
        "sampledata/nonexistentfile.txt"
    )  # Attempting to read a non-existent file to demonstrate exception handling

    print("===============Sum Function===============")
    result = sum(3.5, 2.5)  # Calling the sum
    print(f"Result: {result}")
    print("===============Sum Function with None===============")
    result = sum(
        None, 2.5
    )  # Calling the sum function with None to demonstrate error handling
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
