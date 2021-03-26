
class Board:
    """Count territories of each player in a Go game

    Args:
        board (list[str]): A two-dimensional Go board
    """

    def __init__(self, board):
        self.board = board
        for i in board:
            for j in i:
                print(j)

    def territory(self, x, y):
        """Find the owner and the territories given a coordinate on
           the board

        Args:
            x (int): Column on the board
            y (int): Row on the board

        Returns:
            (str, set): A tuple, the first element being the owner
                        of that area.  One of "W", "B", "".  The
                        second being a set of coordinates, representing
                        the owner's territories.
        """
        row = self.board[y]
        piece = row[x]
        return BLACK, {(0, 0), (0, 1), (1, 0)}

    def territories(self):
        """Find the owners and the territories of the whole board

        Args:
            none

        Returns:
            dict(str, set): A dictionary whose key being the owner
                        , i.e. "W", "B", "".  The value being a set
                        of coordinates owned by the owner.
        """
        pass


class BLACK:
    def __init__(self):
        return 'B'


class WHITE:
    def __init__(self):
        return 'W'


class NONE:
    def __init__(self):
        return ''
