def load_words_dict(file_path):
    """loads all the words from the given dictionary and returns a dictionary
    with the words (keys) and 'True' as the value for each key"""
    f = open(file_path, 'r')
    word_dict = dict()
    for line in f.readlines():
        word = line[:-1]
        word_dict[word] = True
    return word_dict


def is_valid_path(board, path, words):
    """if the path is valid - returns the word the path represents. if the path
    is not valid or the word is not in the dictionary - returns None"""
    if len(path) != len(set(path)):
        return None
    if not path:
        return None
    prev = path[0]
    try:
        word = board[prev[0]][prev[1]]
    except IndexError:
        return None
    for i in range(1, len(path)):
        if path[i] in neighbors(board, prev[0], prev[1]):
            try:
                word += board[path[i][0]][path[i][1]]
                prev = path[i]
            except IndexError:
                return None
        else:
            return None
    if word in words:
        return word
    return None


def find_length_n_words(n, board, words):
    """returns a list of pairs (tuples).
    each pair - a tuple: (str - word , list of tuples - path_for_word).
    The lise will contain all the pairs with valid words in length 'n'"""
    if n < 1:
        return []
    words_new = n_list(n, words)
    row_size = len(board)
    list_of_paths = []
    for word in words_new:
        for i in range(row_size):
            for j in range(row_size):
                if word[:len(board[i][j])] == board[i][j]:
                    path = check_paths(board, i, j, word, [(i, j)],
                                       len(board[i][j]), [])
                    for lst in path:
                        list_of_paths.append((word, lst))
    return list_of_paths


def check_paths(board, i, j, word, lst, index, result):
    """Recursively checks all possible paths on the Boggle board for a given
    word and returns a list of valid paths"""
    if index > len(word) - 1:
        result.append(lst[:])
        return result
    cur_neighbors = neighbors(board, i, j)
    for neighbor in cur_neighbors:
        if board[neighbor[0]][neighbor[1]] == word[index:index + len(
                board[neighbor[0]][neighbor[1]])] and neighbor not \
                in lst:
            lst.append(neighbor)
            check_paths(board, neighbor[0], neighbor[1], word, lst,
                        index + len(board[neighbor[0]][neighbor[1]]), result)
            lst.pop()
    return result


def neighbors(board, i, j):
    """Returns a list of neighboring coordinates for the given (i, j)
    coordinates on the Boggle board"""
    in_middle_row, in_middle_col, is_first_row, is_first_col = \
        check_position(board, i, j)
    cord_dict = {1: (i - 1, j - 1), 2: (i - 1, j), 3: (i - 1, j + 1),
                 4: (i, j + 1), 5: (i + 1, j + 1), 6: (i + 1, j),
                 7: (i + 1, j - 1), 8: (i, j - 1)}
    if in_middle_row and in_middle_col:
        return [cord_dict[i + 1] for i in range(8)]
    if in_middle_col:
        if is_first_col:
            return [cord_dict[4], cord_dict[5],
                    cord_dict[6], cord_dict[7], cord_dict[8]]
        return [cord_dict[1], cord_dict[2], cord_dict[3], cord_dict[4],
                cord_dict[8]]
    if in_middle_row:
        if is_first_row:
            return [cord_dict[2], cord_dict[3], cord_dict[4],
                    cord_dict[5], cord_dict[6]]
        return [cord_dict[1], cord_dict[2], cord_dict[6], cord_dict[7],
                cord_dict[8]]
    if is_first_row:
        if is_first_col:
            return [cord_dict[4], cord_dict[5], cord_dict[6]]
        return [cord_dict[2], cord_dict[3], cord_dict[4]]
    if is_first_col:
        return [cord_dict[6], cord_dict[7], cord_dict[8]]
    return [cord_dict[1], cord_dict[2], cord_dict[8]]


def check_position(board, i, j):
    """Checks the position of coordinates in the Boggle board and returns a
    tuple indicating whether the coordinates are in the middle row, middle
    column, first row, or first column."""
    in_middle_row = False
    in_middle_col = False
    is_first_row = False
    is_first_col = False
    if 0 < i < len(board) - 1:
        in_middle_row = True
    if 0 < j < len(board) - 1:
        in_middle_col = True
    if not in_middle_col:
        if j == 0:
            is_first_row = True
    if not in_middle_row:
        if i == 0:
            is_first_col = True
    return in_middle_row, in_middle_col, is_first_row, is_first_col


def n_list(n, words):
    """Returns a list of words from the provided set that have a length of n"""
    words_new = []
    for word in words.keys():
        if len(word) == n:
            words_new.append(word)
    return words_new
