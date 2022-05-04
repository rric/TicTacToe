# TicTacToeGame.py
# Copyright 2020-2022 Roland Richter

from __future__ import division, print_function

# TOUR-2 
# TicTacToeGame holds the current state of a tic tac toe game.
# Additionally, it keeps track who the next player is (1 or 2), whether
# the game is over, and who has won the game if there is a winner, or
# whether the game is a draw.
# 
# The game is stored as an 3 x 3 array of numbers, like this:
#
#            0  0  1
#            0  0  1
#            2  0  0
#
#   0 ... the cell is empty, i.e. not yet marked by a player
#   1 ... the cell was marked by player 1, usually displayed as 'X'
#   2 ... the cell was marked by player 2, usually displayed as 'O'
#
# Column and row indices are 1-based; all methods use (col, row) order.
#
#    column  1   2   3
#            |   |   |
#            V   V   V
#          +---+---+---+
# row 1 -> |   |   | X |
#          +---+---+---+
# row 2 -> |   |   | X |
#          +---+---+---+
# row 3 -> | O |   |   |
#          +---+---+---+
# 
# In this case, a call of method getCell(col, row) would return:
#
#   getCell(3, 1) -> returns 1
#   getCell(1, 3) -> returns 2
#   getCell(2, 2) -> returns 0
#

class TicTacToeGame:
    
    def __init__(self):
        self.reset()

    # clear the complete grid, and reset current player to player 1
    def reset(self):
        self.cell = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.player = 1
        

    # Return a string which shows the current state of the game
    def getAsString(self):
        result = ""

        for row in [1, 2, 3]:
            for col in [1, 2, 3]:
                if self.getCell(col, row) == 1:
                    result += "X"
                elif self.getCell(col, row) == 2:
                    result += "O"
                else:
                    result += "-"

            result += "\n"

        if self.isGameOver():
            result += "Game over; player " + str(self.getWinner()) + " wins"
        else:
            result += "Player's " + str(self.getCurrentPlayer()) + " move"

        return result

        
    def getCell(self, col, row):
        return self.cell[col-1][row-1]
    
    
    # Let the current player mark the given cell, if possible.
    # Return True if successful, False if not.
    def markCell(self, col, row):
        if self.cell[col-1][row-1] != 0:
            return False
        else:
            self.cell[col-1][row-1] = self.player
            self.player = 3 - self.player   # switch between 1 and 2
            return True
    
    
    def getCurrentPlayer(self):
        return self.player
    
    
    def isGameOver(self):
        # HOMEWORK 4-b Method isGameOver() is not finished yet:
        #   It returns True only if there is a winner. However, if the
        #   game ends in a tie (no free cell left, and no winner), the 
        #   method erroneously returns False.
        #   Fix this: implement the correct behaviour in case of a tie.
        return (self.getWinner() != 0)


    # Return the winner of this game, if there is one.
    #   0 ... no one has won the game (yet).
    #   1 ... player 1 won the game; the game is over.
    #   2 ... player 2 won the game; the game is over.
    def getWinner(self):
        for plyr in [1, 2]:
            for row in [1, 2, 3]:
                if self.count(plyr, 1, row, 2, row, 3, row) == 3:
                    return plyr

            for col in [1, 2, 3]:
                if self.count(plyr, col, 1, col, 2, col, 3) == 3:
                    return plyr

            if self.count(plyr, 1, 1, 2, 2, 3, 3) == 3:
                return plyr

            if self.count(plyr, 1, 3, 2, 2, 3, 1) == 3:
                return plyr

        return 0
    
    
    # counts how often state occurs at cells (col1, row1), (col2, row2), and (col3, row3).
    def count(self, state, col1, row1, col2, row2, col3, row3):
        sum = 0
        sum += 1 if self.cell[col1-1][row1-1] == state else 0
        sum += 1 if self.cell[col2-1][row2-1] == state else 0
        sum += 1 if self.cell[col3-1][row3-1] == state else 0
        
        return sum


# ----------------------------------------------------------------------
# This file is part of TicTacToe.
#
# TicTacToe is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http:#www.gnu.org/licenses/>.
