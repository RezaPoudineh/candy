def are_adjacent(item1, item2):
    """
    Check if the two items are adjacent. They are adjacent if they are
    in the same row or column and the distance between them is 1.

    Args:
        item1 (tuple[int]): The row and column of the first item
        item2 (tuple[int]): The row and column of the second item
    Returns:
        are_adjacent (bool): True if the two items are adjacent, False otherwise

    Examples:
        >>> are_adjacent((0, 0), (0, 1))
        True
        >>> are_adjacent((0, 0), (1, 0))
        True
        >>> are_adjacent((0, 0), (1, 1))
        False
        >>> are_adjacent((0, 0), (0, 0))
        False
    """
    pass


def is_in_board(board, item1):
    """
    Check if the item is in the board. The item is in the board if the row and column
    of the item are valid.

    Args:
        board (list): The board of the game with all elements. Board is a 2D list (a list of several lists).
        item1 (tuple[int]): The row and column of the item
    Returns:
        is_in_board (bool): True if the item is in the board, False otherwise

    Examples:
        >>> is_in_board([[1, 2, 3], [4, 5, 6], [7, 8, 9]], (0, 0))
        True
        >>> is_in_board([[1, 2, 3], [4, 5, 6], [7, 8, 9]], (0, 3))
        False
    """
    pass


def swap(board, item1, item2):
    """
    Swap two items in the board.

    Args:
        board (list): The board of the game with all elements. Board is a 2D list (a list of several lists).
        item1 (tuple[int]): The row and column of the first item
        item2 (tuple[int]): The row and column of the second item
    Returns:
        new_board (list): The board after the swap

    Examples:
        >>> swap([[1, 2, 3], [4, 5, 6], [7, 8, 9]], (0, 0), (0, 1))
        [[2, 1, 3], [4, 5, 6], [7, 8, 9]]
    """
    pass


def check_similar_consecutive_items(items):
    """
    Check if there are three or more similar consecutive items in a list

    Args:
        items (list): A list of items
    Returns:
        True if there are three or more consecutive items with same value, False otherwise

    Examples:
        >>> check_similar_consecutive_items([2, 1, 1, 1])
        True
        >>> check_similar_consecutive_items([2, 1, 2, 1])
        False
    """
    pass


def check_crush(board):
    """
    Check if there is a crush in the board. A crush exists if there are three or more
    similar consecutive items in a row or column.

    Args:
        board (list): The board of the game with all elements. Board is a 2D list (a list of several lists).
    Returns:
        if_crush_exists (bool): True if there is a crush, False otherwise

    Examples:
        >>> check_crush([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        False
        >>> check_crush([[1, 2, 3], [4, 2, 6], [7, 2, 9]])
        True
    """
    if_crush_exists = False
    # Check rows
    ...
    # Check columns
    ...
    return if_crush_exists


def get_crushes(board):
    """
    Get the crushes in the board.

    Args:
        board (list): The board of the game with all elements. Board is a 2D list (a list of several lists).
    Returns:
        crushes (list[Tuple[int]]): A list of crushes. Each tuple is the row and column of an item that is crushed.
    """
    pass


def fill_board(board, crushes):
    """
    Fill the board after crushes. The items in the crushes will be replaced with items above them.
    The items on the top of the board will be replaced with new random items.

    Args:
        board (list): The board of the game with all elements. Board is a 2D list (a list of several lists).
        crushes (list[Tuple[int]]): A list of crushes. Each tuple is the row and column of an item that is crushed.
    Returns:
        new_board (list): The board after filling

    Examples:
        >>> fill_board([[1, 2, 3], [4, 5, 6], [0, 0, 0]], [(2, 0), (2, 1), (2, 2)])
        [[2, 9, 4], [1, 2, 3], [4, 5, 6]]
    """
    import random

    pass


def make_move(board, item1, item2, points):
    board = swap(board, item1, item2)
    crushes = get_crushes(board)
    new_points = len(crushes)
    board = remove_crushes(board, crushes)
    print_board(board, points)
    board = fill_board(board, crushes)
    print_board(board, points)

    ######################################
    #      Complete this function        #
    ######################################
    # # TODO: crush until there is no more crush
    raise NotImplementedError

    return board, new_points


######################################################################
#                   COMPLETED FUNCTIONS                              #
######################################################################
def initialize_board():
    """
    Initialize the board with random numbers

    Args:
        None
    Returns:
        board (list): The board of the game with all elements. Board is a 2D list (a list of several lists).
    """
    board = [
        [1, 1, 2, 4, 3, 2, 1],
        [4, 4, 3, 2, 1, 3, 4],
        [2, 3, 4, 1, 2, 3, 4],
        [1, 2, 3, 4, 1, 2, 3],
        [4, 3, 2, 1, 4, 3, 2],
        [3, 2, 1, 3, 2, 1, 4],
        [2, 1, 4, 3, 2, 1, 3],
    ]
    return board


def print_board(board, points):
    """
    Print the board and the points

    Args:
        board (list): The board of the game with all elements. Board is a 2D list (a list of several lists).
        points (int): The points of the player up to this point.

    Returns:
        None
    """
    print(f"Points: {points}")
    for row in board:
        print(row)


def user_choice():
    """
    Get the user's choice of items to swap

    Args:
        None
    Returns:
        item1 (tuple[int]): The row and column of the first item
        item2 (tuple[int]): The row and column of the second item
    """
    item1_row = int(input("Enter the row of the first item: ")) - 1
    item1_col = int(input("Enter the column of the first item: ")) - 1
    item2_row = int(input("Enter the row of the second item: ")) - 1
    item2_col = int(input("Enter the column of the second item: ")) - 1
    item1 = (item1_row, item1_col)
    item2 = (item2_row, item2_col)
    return item1, item2


def check_swap(board, item1, item2):
    """
    Check if the swap is valid. The swap is valid if the two
    items are adjacent and it leads to a crush.

    Args:
        board (list): The board of the game with all elements. Board is a 2D list (a list of several lists).
        item1 (tuple[int]): The row and column of the first item
        item2 (tuple[int]): The row and column of the second item
    Returns:
        is_swap_valid (bool): True if the swap is valid, False otherwise
    """
    is_swap_valid = True
    # Check if the two items are in the board
    if not is_in_board(board, item1) or not is_in_board(board, item2):
        is_swap_valid = False
    # Check if the two items are adjacent
    if not are_adjacent(item1, item2):
        is_swap_valid = False
    # Check if the swap leads to a crush
    if not check_crush_if_swap(board, item1, item2):
        is_swap_valid = False

    return is_swap_valid


def check_crush_if_swap(board, item1, item2):
    """
    Check if the swap leads to a crush. The swap leads to a crush if
    there is a crush after the swap.

    Args:
        board (list): The board of the game with all elements. Board is a 2D list (a list of several lists).
        item1 (tuple[int]): The row and column of the first item
        item2 (tuple[int]): The row and column of the second item
    Returns:
        if_crush_exists (bool): True if there is a crush, False otherwise
    """
    new_board = swap(board, item1, item2)
    return check_crush(new_board)


def remove_crushes(board, crushes):
    """
    Remove the crushes from the board.

    Args:
        board (list): The board of the game with all elements. Board is a 2D list (a list of several lists).
        crushes (list[Tuple[int]]): A list of crushes. Each tuple is the row and column of an item that is crushed.
    Returns:
        new_board (list): The board after removing the crushes.
    """
    for item in crushes:
        board[item[0]][item[1]] = 0
    return board


def check_game_over(points, max_points=100):
    """
    Check if the game is over. The game is over if the player has more than `max_points` points.

    Args:
        points (int): The points of the player up to this point.
        max_points (int): The maximum points the player can have before the game is over.
    Returns:
        if_game_over (bool): True if the game is over, False otherwise
    """
    if points > max_points:
        return True
######################################################################
#                       GAME FUNCTION                                #
######################################################################
def game():
    """
    Runs a Candy Crush game.

    Args:
        None
    Returns:
        None
    """
    board = initialize_board()
    game_over = False
    points = 0
    while not game_over:
        print_board(board, points)
        # Get user's choices
        item1, item2 = user_choice()
        # check if the swap is valid
        is_swap_valid = check_swap(board, item1, item2)
        if is_swap_valid:
            board, move_points = make_move(board, item1, item2, points)
            points += move_points
        else:
            print("Invalid move. Try again.")
        # check if the game is over
        game_over = check_game_over(points)

    print("Game over!")


######################################################################
#                      Test Your Code                                #
######################################################################
game() # Is everything working as expected...?