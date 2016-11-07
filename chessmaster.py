#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Playing chess"""

import time


class ChessPiece(object):
    """A class that represents start position

    Args:
        position(str): a string for the position of chess.
        moves(list): a list of tuples for the information about each move of
        the chess piece..

    Attributes:
        prefix(str): an empty strin.
        position(str): represents a starting position
        moves(list): stores tuples of information
    """

    prefix = ''

    def __init__(self, position, moves=None):
        self.position = position
        self.moves = moves
        self.moves = []
        myposition = self.algebraic_to_numeric(position)
        if myposition is None:
            excep = "'{}' is not a legal start position"
            raise ValueError(excep.format(position))

    def algebraic_to_numeric(self, tile):
        """Takes a single string argument and converts it to a tuple
        with two values.

        Args:
            tile(str): a single stringargument.

        Returns:
            a tuple: a tuple with two values.

        Examples:

            >>> piece.algebraic_to_numeric('e7')
            (4, 6)
            >>> piece.algebraic_to_numeric('j9')
            >>> piece.move('j9')
        """
        self.tile = tile
        letter_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        number_list = ['1', '2', '3', '4', '5', '6', '7', '8']
        letter_number_dict = {'a': 0,
                              'b': 1,
                              'c': 2,
                              'd': 3,
                              'e': 4,
                              'f': 5,
                              'g': 6,
                              'h': 7}
        if self.tile[1] in number_list:
            if self.tile[0] in letter_list:
                letter_num = letter_number_dict[self.tile[0]]
                return (letter_num, int(self.tile[1]) - 1)
        else:
            return None

    def is_legal_move(self, position):
        """Ensures the starting position is legal

        Args:
            position(str): position of the start piece

        Returns:
            Returns True if the move is legal, False if not
        """
        self.position = position
        move = self.algebraic_to_numeric(position)
        if move is not None:
            return True
        else:
            return False

    def move(self, position):
        """Moving a piece.

        Args:
            position(str): represents the algebraic notation of the
            new position to which the piece should be moves.
            is_this_legal: tests to see if the position is legal

        Returns:
            position(str): moves the chess piece.
            is_this_legal(bool): returns a tuple if legal, False if
            not legal.
        Examples:
            >>> piece.move('j9')
            False
            >>> piece.move('e7')
            ('j9', 'e7', 1478476479.851767)
        """
        oldposition = self.position
        newposition = position
        piece_move = self.is_legal_move(newposition)
        if piece_move is True:
            timestamp = time.time()
            n_position = self.prefix + newposition
            o_position = self.prefix + oldposition
            self.moves.append((o_position, n_position, timestamp))
            self.position = newposition
            return (o_position, n_position, timestamp)
        else:
            return False


class Rook(ChessPiece):
    """Moves any number of squares along the x or y axis.

    Args:
        position(str): position of chess piece.
        moves(str): the move of the chess piece.
    """
    prefix = 'R'

    def __init__(self, position, moves=None):
        self.position = position
        ChessPiece.__init__(self, position, moves=None)

    def is_legal_move(self, position):
        """Checks if the move is legal.

        Args:
            position(str): the position of Rook.

        Returns:
            True if the move is legal and False if it is not.

        Examples:

            >>> rook = Rook('a1')
            >>> rook.is_legal_move('k5')
            False
        """
        move2 = self.algebraic_to_numeric(position)
        move1 = self.algebraic_to_numeric(self.position)
        move2 = list(move2)
        move1 = list(move1)
        m1_x = move1[0]
        m1_y = move1[1]
        m2_x = move2[0]
        m2_y = move2[1]
        if m1_x != m2_x and m1_y != m2_y:
            return False
        else:
            self.position = position
            return True


class Bishop(ChessPiece):
    """Bishop moves, any number of squares in a diagonal line.

    Args:
        position(str): the Bishop's position.
        moves(list): tuples.

    Attributes:
        prefix(str): a class attribute with the value of B.
    """
    prefix = 'B'

    def __init__(self, position, moves=None):
        self.position = position
        ChessPiece.__init__(self, position, moves=None)

    def is_legal_move(self, position):
        """Checks if the move is legal.

        Args:
            position(str): the position of Rook.

        Returns:
            True if the move is legal and False if it is not.

        Examples:

            >>> rook = Bishop('a2')
            False
        """
        move2 = self.algebraic_to_numeric(position)
        move1 = self.algebraic_to_numeric(self.position)
        move2 = list(move2)
        move1 = list(move1)
        m1_x = move1[0]
        m1_y = move1[1]
        m2_x = move2[0]
        m2_y = move2[1]
        if abs(m1_x - m2_x) == abs(m1_y - m2_y):
            self.position = position
            return True
        else:
            return False


class King(ChessPiece):
    """The king can moves in any direction one space at a time.

    Args:
        position(str): the king's position.
        moves(list): tuples with information about king's moves

    Attributes:
        prefix(str): a class attribute with the value of K.
    """
    prefix = 'K'

    def __init__(self, position, moves=None):
        self.position = position
        ChessPiece.__init__(self, position, moves=None)

    def is_legal_move(self, position):
        """Checks if the move is legal.

        Args:
            position(str): the position of King.

        Returns:
            True if the move is legal and False if it is not.

        Examples:

            >>> king.move('a3')
            False
        """
        move2 = self.algebraic_to_numeric(position)
        move1 = self.algebraic_to_numeric(self.position)
        move2 = list(move2)
        move1 = list(move1)
        m1_x = move1[0]
        m1_y = move1[1]
        m2_x = move2[0]
        m2_y = move2[1]
        if abs(m1_x - m2_x) == 1 or abs(m1_y - m2_y) == 1:
            self.position = position
            return True
        else:
            return False


class ChessMatch(object):
    """A class that functions as the gameboard and tracks our moves.

    Args:
        position(str): the chess piece's position.
        pieces(list): a dictionary of pieces keyed by their position
        on the board.
    """

    def __init__(self, pieces=None):
        if pieces is None:
            self.reset()
        else:
            self.pieces = pieces
            self.log = []

    def reset(self):
        """Resets the match log to an empty list and places our
        pieces back at their starting positions

        Args:
            pieces(str): instance attribute in a dictionary."""
        self.log = []
        self.pieces = {'Ra1': Rook('a1'),
                       'Rh1': Rook('h1'),
                       'Ra8': Rook('a8'),
                       'Rh8': Rook('h8'),
                       'Bc1': Bishop('c1'),
                       'Bf1': Bishop('f1'),
                       'Bc8': Bishop('c8'),
                       'Bf8': Bishop('f8'),
                       'Ke1': King('e1'),
                       'Ke8': King('e8')}

    def move(self, full_notation, position):
        """Move pieces to a new position

        Args:
            full_notation(str): Full notation of a piece position.
            position(str): pieces position

        Attributes:
            log(str): log attribute.
            pieces(str): pieces attribute.
            prefix(str): prefix attribute
            """
        result = self.pieces[full_notation].move(position)
        if result is not False:
            self.log.append(result)
            ent = self.pieces[full_notation].prefix + position
            self.pieces[ent] = self.pieces.pop(full_notation)
        return False

    def __len__(self):
        return len(self.log)
