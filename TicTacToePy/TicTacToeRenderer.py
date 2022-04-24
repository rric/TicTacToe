# TicTacToeRenderer.py
# Copyright 2020-2022 Roland Richter

from __future__ import division, print_function

# TOUR-3
# TicTacToeRenderer creates a visualization of a TicTacToeGame object.
#
# - renderGame(game) draws the game onto Processing's display, using a 'X' symbol
#     for player 1, and a 'O' symbol for player 2
#
# - renderGameAndPointer(game, mX, mY) first draws the game onto Processing's display,
#     as described before; then it draws a mouse pointer, either 'X' or 'O', to indicate 
#     the next move (if the mouse was pressed)
#
 
# HOMEWORK 4-c Write your own TicTacToeRenderer.
#   This renderer draws red crosses and blue circles into a quadratic  grid.
#   Use other shapes, other colors, images etc. to create your own visualization
#   of tic tac toe.

class TicTacToeRenderer:
    
    def __init__(self, upperLeftX, upperLeftY, gridWidth,  gridHeight):
        self.ulX = upperLeftX
        self.ulY = upperLeftY
        self.grW = gridWidth
        self.grH = gridHeight

        self.bgClr = color(255, 250, 240)  # background color
        self.grClr = color(176, 101, 0)    # grid color
        self.fpClr = color(255, 8, 0)      # first player color
        self.spClr = color(21, 96, 189)    # second player color


    def renderGame(self, game):
        background(self.bgClr)

        stroke(self.grClr)
        strokeWeight(10)

        # draw horizontal and vertical lines of 3 x 3 grid
        for hl in [1, 2, 3, 4]:
            line(self.cellLeftX(1), self.cellUpperY(hl), self.cellRightX(3), self.cellUpperY(hl))

        for vl in [1, 2, 3, 4]:
            line(self.cellLeftX(vl), self.cellUpperY(1), self.cellLeftX(vl), self.cellLowerY(3))

        for row in [1, 2, 3]:
            for col in [1, 2, 3]:
                cell = game.getCell(col, row)

                if cell == 1:
                    self.drawCross(col, row, self.fpClr)
                elif cell == 2:
                    self.drawCircle(col, row, self.spClr)

        if game.isGameOver():
            fill('#303030')
            textSize(108)
            text(str(game.getWinner()) + "!", self.cellLeftX(2), self.cellLowerY(2))


    def renderGameAndPointer(self, game, mX, mY):
        self.renderGame(game)

        if not game.isGameOver() and self.isMouseInGrid(mX, mY):
            col = self.getColumnOf(mX)
            row = self.getRowOf(mY)

            if game.getCell(col, row) == 0:
                if game.getCurrentPlayer() == 1:
                    paleClr = lerpColor(self.fpClr, color(255, 255, 255), 0.5)
                    self.drawCross(col, row, paleClr)
                elif game.getCurrentPlayer() == 2:
                    paleClr = lerpColor(self.spClr, color(255, 255, 255), 0.5)
                    self.drawCircle(col, row, paleClr)
    

    def drawCross(self, col, row, clr):
        fill(self.bgClr)
        stroke(clr)
        strokeWeight(10)

        crossWidth = round(0.35 * self.cellWidth())
        crossHeight = round(0.35 * self.cellHeight())

        line(self.cellCenterX(col) - crossWidth, self.cellCenterY(row) - crossHeight, 
            self.cellCenterX(col) + crossWidth, self.cellCenterY(row) + crossHeight)
        line(self.cellCenterX(col) - crossWidth, self.cellCenterY(row) + crossHeight, 
            self.cellCenterX(col) + crossWidth, self.cellCenterY(row) - crossHeight)


    def drawCircle(self, col, row, clr):
        fill(self.bgClr)
        stroke(clr)
        strokeWeight(10)

        extentX = round(0.7 * self.cellWidth())
        extentY = round(0.7 * self.cellHeight())

        ellipse(self.cellCenterX(col), self.cellCenterY(row), extentX, extentY)


    def isMouseInGrid(self, x, y):
        inHoriz = (x >= self.cellLeftX(1) and x <= self.cellRightX(3))
        inVert  = (y >= self.cellUpperY(1) and y <= self.cellLowerY(3))
        return inHoriz and inVert

    def getColumnOf(self, x):
        return floor(map(x, self.cellLeftX(1), self.cellRightX(3)+1, 1.0, 4.0))


    def getRowOf(self, y):
        return floor(map(y, self.cellUpperY(1), self.cellLowerY(3)+1, 1.0, 4.0))

    #
    # To draw to Processing's display, a number of helper functions is used:
    #
    #     cellLeftX(    1   2   3     )
    #                   |   |   |
    #                   V   V   V
    # cellUpperY(1) ->  +---+---+---+
    #                   |   |   | X |
    # cellUpperY(2) ->  +---+---+---+ <- cellLowerY(1)
    #                   |   |   | X |
    # cellUpperY(3) ->  +---+---+---+ <- cellLowerY(2)
    #                   | O |   |   |
    #                   +---+---+---+ <- cellLowerY(3)
    #                       ^   ^   ^
    #                       |   |   |
    #     cellRightX(       1   2   3   )
    #
    # Column and row indices are 1-based, i.e. counting starts at 1 (not 0).
    #
    # Examples:
    #   cellLeftX(2) returns the x-coordinate of the left edge of a cell in column 2
    #   cellLowerY(3) returns the y-coordinate of the lower edge of a cell in row 3
    #   cellCenterX(1) returns the x-coordinate of the center of a cell in column 1
    #
    # Several of these values are equal, e.g. cellRightX(1) == cellLeftX(2), 
    # cellUpperY(3) == cellLowerY(2), and so on.
    #
    
    def cellWidth(self):
        return self.grW / 3.0


    def cellLeftX(self, col):
        return self.ulX + (col-1) * self.cellWidth()


    def cellCenterX(self, col):
        return round(self.ulX + (col - 0.5) * self.cellWidth())


    def cellRightX(self, col):
        return self.ulX + (col) * self.cellWidth()


    def cellHeight(self):
        return self.grH / 3.0


    def cellUpperY(self, row):
        return self.ulY + (row-1) * self.cellHeight()


    def cellCenterY(self, row):
        return round(self.ulY + (row - 0.5) * self.cellHeight())


    def cellLowerY(self, row):
        return self.ulY + (row) * self.cellHeight()


# ----------------------------------------------------------------------
# self file is part of TicTacToe.
#
# TicTacToe is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# self program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with self program. If not, see <http:#www.gnu.org/licenses/>.
    
