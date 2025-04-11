import sys

class Matrix:
    def __init__(self, rows):
        """Initialize the matrix with a list of lists."""
        self.rows = rows
        self.num_rows = len(rows)
        self.num_cols = len(rows[0]) if rows else 0

    def display(self):
        """Display the matrix in a readable format."""
        print("\nYour Matrix:")
        for row in self.rows:
            print(" | ".join(f"{num:6.2f}" for num in row))
        print("\n")

    def swap_rows(self, row1, row2):
        """Swap two rows in the matrix."""
        self.rows[row1], self.rows[row2] = self.rows[row2], self.rows[row1]
    
    def multiply_row(self, row, scalar):
        """Multiply a row by a nonzero scalar."""
        if scalar == 0:
            print("⚠️ Warning: Cannot multiply a row by zero.")
            return
        self.rows[row] = [scalar * num for num in self.rows[row]]

    def add_multiple_of_row(self, target_row, source_row, scalar):
        """Add a multiple of one row to another row."""
        self.rows[target_row] = [
            self.rows[target_row][i] + scalar * self.rows[source_row][i]
            for i in range(self.num_cols)
        ]

    def row_echelon_form(self):
        """Convert matrix to Row Echelon Form (REF)."""
        print("\nConverting to Row Echelon Form...\n")
        for i in range(min(self.num_rows, self.num_cols)):
            if self.rows[i][i] == 0:
                for j in range(i + 1, self.num_rows):
                    if self.rows[j][i] != 0:
                        self.swap_rows(i, j)
                        break
                else:
                    print(f" Warning: Column {i} contains only zeros. Skipping pivot.")
                    continue
            pivot = self.rows[i][i]
            self.multiply_row(i, 1 / pivot)
            for j in range(i + 1, self.num_rows):
                factor = -self.rows[j][i]
                self.add_multiple_of_row(j, i, factor)
        self.display()

    def reduced_row_echelon_form(self):
        """Convert matrix to Reduced Row Echelon Form (RREF)."""
        print("\nConverting to Reduced Row Echelon Form...\n")
        for i in range(min(self.num_rows, self.num_cols)):
            if self.rows[i][i] == 0:
                for j in range(i + 1, self.num_rows):
                    if self.rows[j][i] != 0:
                        self.swap_rows(i, j)
                        break
                else:
                    print(f" Warning: Column {i} contains only zeros. Skipping pivot.")
                    continue
            pivot = self.rows[i][i]
            self.multiply_row(i, 1 / pivot)
            for j in range(self.num_rows):
                if j != i:
                    factor = -self.rows[j][i]
                    self.add_multiple_of_row(j, i, factor)
        self.display()


def get_matrix_input():
    """Prompt the user to enter a matrix row by row with error handling."""
    print("\nEnter your matrix row by row. Type 'done' when finished.")
    matrix_data = []
    while True:
        row_input = input("Enter row (separate numbers by space): ")
        if row_input.lower() == "done":
            break
        try:
            row = list(map(float, row_input.split()))
            matrix_data.append(row)
        except ValueError:
            print(" Invalid input. Please enter numbers only.")
    
    if not matrix_data:
        print(" No valid matrix entered. Returning to main menu.")
        return None

    num_cols = len(matrix_data[0])
    if any(len(row) != num_cols for row in matrix_data):
        print(" All rows must have the same number of elements. Try again.")
        return None

    return Matrix(matrix_data)


def show_definitions():
    """Display definitions of key matrix concepts."""
    print("\n Definitions:")
    print("1️ Row Echelon Form (REF): A matrix form where each leading coefficient is 1 and below it are zeros.")
    print("2️ Reduced Row Echelon Form (RREF): Like REF, but each leading coefficient is the only nonzero entry in its column.\n")


def show_examples():
    """Display examples of matrix transformations."""
    print("\n Examples:")
    print("Example 1: Converting to Row Echelon Form")
    print("[[2, 4, 6, 18], [4, 5, 6, 24], [3, 1, -2, 4]] → [[1, 2, 3, 9], [0, 1, 2, 4], [0, 0, 1, 3]]\n")
    print("Example 2: Converting to Reduced Row Echelon Form")
    print("[[2, 4, 6, 18], [4, 5, 6, 24], [3, 1, -2, 4]] → [[1, 0, 0, 4], [0, 1, 0, -2], [0, 0, 1, 3]]\n")


def get_valid_choice(prompt, valid_choices):
    """Ensures the user selects a valid choice."""
    while True:
        choice = input(prompt)
        if choice in valid_choices:
            return choice
        print(" Invalid choice. Please try again.")


def main():
    """Main interactive loop for the program with better input handling."""
    print("\n Welcome to the Matrix Learning Hub! ")
    while True:
        print("\nWhat would you like to do?")
        print("1️ Enter a new matrix")
        print("2️ Read a fun fact about matrices")
        print("3️ See definitions")
        print("4️ See examples")
        print("5️ Quit")

        choice = get_valid_choice("Enter your choice (1-5): ", {"1", "2", "3", "4", "5"})
        
        if choice == "1":
            matrix = get_matrix_input()
            if matrix:
                while True:
                    print("\nWhat do you want to do with the matrix?")
                    print("1️ Convert to Row Echelon Form (REF)")
                    print("2️ Convert to Reduced Row Echelon Form (RREF)")
                    print("3️ Return to Main Menu")

                    action = get_valid_choice("Enter your choice (1-3): ", {"1", "2", "3"})
                    if action == "1":
                        matrix.row_echelon_form()
                    elif action == "2":
                        matrix.reduced_row_echelon_form()
                    elif action == "3":
                        break
        elif choice == "2":
            show_definitions()
        elif choice == "3":
            show_examples()
        elif choice == "4":
            print("\nThank you for learning matrices with us! Goodbye! ")
            sys.exit()

if __name__ == "__main__":
    main()
