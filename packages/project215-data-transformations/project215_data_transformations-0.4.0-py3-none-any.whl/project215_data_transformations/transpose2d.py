def transpose2d(input_matrix: list[list[float]]) -> list[list[float]]:
    """
    Transpose a 2D matrix represented as a list of lists.

    Args:
        input_matrix (List[List[float]]): The input matrix as a list of lists of real numbers.

    Returns:
        List[List[float]]: The transposed matrix as a list of lists.

    Raises:
        ValueError: If the input matrix is not a non-empty list of lists of real numbers, 
        or if the rows do not have the same number of columns for transposition.
    """
    if not input_matrix or not all(isinstance(row, list) for row in input_matrix):
        raise ValueError("Input matrix must be a non-empty list of lists of real numbers.")

    num_columns = len(input_matrix[0])
    if not all(len(row) == num_columns for row in input_matrix):
        raise ValueError("All rows must have the same number of columns for transposition.")

    transposed_matrix = [[row[i] for row in input_matrix] for i in range(num_columns)]

    return transposed_matrix