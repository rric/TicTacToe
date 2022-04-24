# TicTacToe.py
# Copyright 2020-2022 Roland Richter

# TOUR-1 This sketch uses two separate classes, and some additional code:
#
#   (1) The game object represents the current state of the TicTacToe game.
#       It stores the game as an 3 x 3 array of numbers, like this:
#
#            0  0  1
#            0  0  1
#            2  0  0
#
#     Here, 0 means the cell is empty; 1 means the cell was marked by
#     player 1, and 2 means the cell was marked by player 2.
#
#   (2) The renderer takes a game object, and renders it; i.e, it produces
#       a visualization of the game. For instance, the method renderGame() 
#       of ConsoleRenderer prints to the console; the game above would look
#       like this:
#
#       --X
#       --X
#       O--
#       Player's 2 move?
#
#   (3) You can play TicTacToeJava with your mouse. 
#       
#       Therefore, a TicTacToeMouseRenderer has to be used, and some code in
#       the draw() and mousePressed() functions is necessary to connect game 
#       and renderer, and to handle mouse actions.
#  
#     
#   This software design pattern is called "model-view-controller", or MVC. 
#   It consists of three parts:
#
#   (1) the model: holds the underlying data structure (here: the game)
#   (2) a view: offers a visualization of the model (here: a renderer)
#   (3) the controller: accepts input to change the model (and, perhaps, the view)
#         (here: code in the mousePressed() funtion)
#
#   Further reading: https:#en.wikipedia.org/wiki/Model–view–controller
#

# HOMEWORK 4-a Find three other uses of the model-view-controller pattern.
#   Describe them, and upload your text, including references.

from TicTacToeGame import *
from TicTacToeRenderer import *


def setup():
    size(400, 400)
    
    global tttGame, renderer, gameChanged
    
    tttGame = TicTacToeGame()
    renderer = TicTacToeRenderer(50, 50, 300, 300)

    gameChanged = True
    

# TOUR-4 The draw() function of this sketch is rather simple:
#   It just draws the game, and the mouse pointer, onto the display;
#   additionally, it prints the game to the console.
def draw():
    global tttGame, renderer, gameChanged
    
    renderer.renderGameAndPointer(tttGame, mouseX, mouseY)

    if gameChanged:
        print(tttGame.getAsString())
        gameChanged = False


# TOUR-5 When the mouse is pressed, one has to distinguish two different cases:
#   - the game is not yet over: place a mark ('X' or 'O') at the current mouse
#     position, if possible
#  - the game is over: start a new tic tac toe game!
def mousePressed():
    global tttGame, renderer, gameChanged
    
    if tttGame.isGameOver():
        tttGame.reset()
        gameChanged = True
    elif renderer.isMouseInGrid(mouseX, mouseY):
        col = renderer.getColumnOf(mouseX)
        row = renderer.getRowOf(mouseY)
        player = tttGame.getCurrentPlayer()

        if tttGame.markCell(col, row):
            print("Player " + str(player) + " marked cell " + str(col) + ", " + str(row))
            gameChanged = True


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
