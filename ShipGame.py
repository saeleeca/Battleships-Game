# Author: Calvin Saelee
# GitHub username: saeleeca
# Date: 3/09/2022
# Description: This program contains a two-player game called ShipGame that is based off of the tabletop game Battleship
# Players must first place their battleships and then player 1 may make the first move by calling the fire_torpedo
# method. Afterwards the players alternate turns until one player's ship have all been sunk and the other player wins.

import random
from enum import Enum


class ShipGame:
    """ A class to represent the popular board-game Battleship that contains essential dictionary-lists and methods
    to initialize and play the game Battleship. """

    def __init__(self):
        """ Takes no parameters but initializes the necessary empty lists and the all-important "board" as a dictionary.
        Will also contain another dictionary that stores information about the players, including their ships, where
        they are placed, and the status of these ships. self._board_P1 and P2 are the individual players' boards and
         reflect the spaces their ships occupy. """

        self._board_P1 = {
            "A1": "empty",
            "A2": "empty",
            "A3": "empty",
            "A4": "empty",
            "A5": "empty",
            "A6": "empty",
            "A7": "empty",
            "A8": "empty",
            "A9": "empty",
            "A10": "empty",
            "B1": "empty",
            "B2": "empty",
            "B3": "empty",
            "B4": "empty",
            "B5": "empty",
            "B6": "empty",
            "B7": "empty",
            "B8": "empty",
            "B9": "empty",
            "B10": "empty",
            "C1": "empty",
            "C2": "empty",
            "C3": "empty",
            "C4": "empty",
            "C5": "empty",
            "C6": "empty",
            "C7": "empty",
            "C8": "empty",
            "C9": "empty",
            "C10": "empty",
            "D1": "empty",
            "D2": "empty",
            "D3": "empty",
            "D4": "empty",
            "D5": "empty",
            "D6": "empty",
            "D7": "empty",
            "D8": "empty",
            "D9": "empty",
            "D10": "empty",
            "E1": "empty",
            "E2": "empty",
            "E3": "empty",
            "E4": "empty",
            "E5": "empty",
            "E6": "empty",
            "E7": "empty",
            "E8": "empty",
            "E9": "empty",
            "E10": "empty",
            "F1": "empty",
            "F2": "empty",
            "F3": "empty",
            "F4": "empty",
            "F5": "empty",
            "F6": "empty",
            "F7": "empty",
            "F8": "empty",
            "F9": "empty",
            "F10": "empty",
            "G1": "empty",
            "G2": "empty",
            "G3": "empty",
            "G4": "empty",
            "G5": "empty",
            "G6": "empty",
            "G7": "empty",
            "G8": "empty",
            "G9": "empty",
            "G10": "empty",
            "H1": "empty",
            "H2": "empty",
            "H3": "empty",
            "H4": "empty",
            "H5": "empty",
            "H6": "empty",
            "H7": "empty",
            "H8": "empty",
            "H9": "empty",
            "H10": "empty",
            "I1": "empty",
            "I2": "empty",
            "I3": "empty",
            "I4": "empty",
            "I5": "empty",
            "I6": "empty",
            "I7": "empty",
            "I8": "empty",
            "I9": "empty",
            "I10": "empty",
            "J1": "empty",
            "J2": "empty",
            "J3": "empty",
            "J4": "empty",
            "J5": "empty",
            "J6": "empty",
            "J7": "empty",
            "J8": "empty",
            "J9": "empty",
            "J10": "empty",
        }

        self._board_P2 = {
            "A1": "empty",
            "A2": "empty",
            "A3": "empty",
            "A4": "empty",
            "A5": "empty",
            "A6": "empty",
            "A7": "empty",
            "A8": "empty",
            "A9": "empty",
            "A10": "empty",
            "B1": "empty",
            "B2": "empty",
            "B3": "empty",
            "B4": "empty",
            "B5": "empty",
            "B6": "empty",
            "B7": "empty",
            "B8": "empty",
            "B9": "empty",
            "B10": "empty",
            "C1": "empty",
            "C2": "empty",
            "C3": "empty",
            "C4": "empty",
            "C5": "empty",
            "C6": "empty",
            "C7": "empty",
            "C8": "empty",
            "C9": "empty",
            "C10": "empty",
            "D1": "empty",
            "D2": "empty",
            "D3": "empty",
            "D4": "empty",
            "D5": "empty",
            "D6": "empty",
            "D7": "empty",
            "D8": "empty",
            "D9": "empty",
            "D10": "empty",
            "E1": "empty",
            "E2": "empty",
            "E3": "empty",
            "E4": "empty",
            "E5": "empty",
            "E6": "empty",
            "E7": "empty",
            "E8": "empty",
            "E9": "empty",
            "E10": "empty",
            "F1": "empty",
            "F2": "empty",
            "F3": "empty",
            "F4": "empty",
            "F5": "empty",
            "F6": "empty",
            "F7": "empty",
            "F8": "empty",
            "F9": "empty",
            "F10": "empty",
            "G1": "empty",
            "G2": "empty",
            "G3": "empty",
            "G4": "empty",
            "G5": "empty",
            "G6": "empty",
            "G7": "empty",
            "G8": "empty",
            "G9": "empty",
            "G10": "empty",
            "H1": "empty",
            "H2": "empty",
            "H3": "empty",
            "H4": "empty",
            "H5": "empty",
            "H6": "empty",
            "H7": "empty",
            "H8": "empty",
            "H9": "empty",
            "H10": "empty",
            "I1": "empty",
            "I2": "empty",
            "I3": "empty",
            "I4": "empty",
            "I5": "empty",
            "I6": "empty",
            "I7": "empty",
            "I8": "empty",
            "I9": "empty",
            "I10": "empty",
            "J1": "empty",
            "J2": "empty",
            "J3": "empty",
            "J4": "empty",
            "J5": "empty",
            "J6": "empty",
            "J7": "empty",
            "J8": "empty",
            "J9": "empty",
            "J10": "empty",
        }

        self._column_legend = {
            "A": 1,
            "B": 2,
            "C": 3,
            "D": 4,
            "E": 5,
            "F": 6,
            "G": 7,
            "H": 8,
            "I": 9,
            "J": 10,

            1: "A",
            2: "B",
            3: "C",
            4: "D",
            5: "E",
            6: "F",
            7: "G",
            8: "H",
            9: "I",
            10: "J",
            11: "K"
        }  # this dictionary allows the place_ship method to iterate through letters for placement and validation

        self._P1_ships = {}  # dictionary that holds lists representing battleships

        self._P2_ships = {}

        self._turn = "first"  # Initialized to player 1, as player 1 starts the game after battleships are placed.

        self._status = "UNFINISHED"
        # The status of the game will be initialized to unfinished as the game is either finished or it is not.
        # At the end of fire_torpedo, if a player has no more ships then this is changed to FIRST_WON or SECOND_WON

    def get_current_state(self):
        """ This method returns the current state of the game. """
        return self._status

    def get_P1_ships(self):
        """ Returns the dictionary of player 1's currently active ships. """
        return self._P1_ships

    def get_P2_ships(self):
        """ Returns the dictionary of player 2's currently active ships. """
        return self._P2_ships

    def get_P1_board(self):
        """ Returns the current state of player 1's board. """
        return self._board_P1

    def get_P2_board(self):
        """ Returns the current state of player 2's board. """
        return self._board_P2

    def place_ship(self, player, length, coordinates, orientation):
        """ Checks the values of the passed parameters and return False if any are not valid. The
       method will call an additional helper method to further validate passed parameters and then create the ship
       objects, place them on player boards, and update the list of player ships."""
        if player != 'first' and player != 'second':  # some initial data validations before placing ships
            return False
        if length > 10 or length <= 1:  # ships must be at least 2 and no more than 10 in length
            return False
        if orientation != 'C' and orientation != 'R':
            return False
        if orientation == "R":  # initial data validation for ships placed as a "row" orientation
            if length + int(coordinates[1]) > 11:
                return False
            if len(coordinates) > 3:  # ships must be at least 2 in length, so an attempt on the 10th column is invalid
                return False
            if len(coordinates) == 3:
                return False
        if orientation == "C":
            if length + self._column_legend[coordinates[0]] > 11:  # if the ship is not fully on the board vertically
                return False
        if coordinates[0] not in self._column_legend:  # ensures passed coordinates are on the board
            return False
        if len(coordinates) >= 4:
            return False

        if player == 'first':
            if orientation == 'R':  # further validates and places ships that are "row" oriented
                if self.is_valid(length, coordinates, orientation, self._board_P1) == False:  # helper validation method
                    return False
                space = coordinates[0] + coordinates[1]
                place = int(coordinates[1])  # allows us to iterate horizontally across specified row
                self._P1_ships[coordinates] = []  # creates the empty list to be filled and put into P1_ships dictionary
                for segments in range(length):
                    self._board_P1[space] = "occupied"
                    self._P1_ships[coordinates] += [space]  # appends coordinates to current ship's occupied spaces
                    place += 1
                    space = coordinates[0] + str(place)
                return True

            if orientation == 'C':  # further validates and places ships that are "column" oriented
                if self.is_valid(length, coordinates, orientation, self._board_P1) == False:
                    return False
                space = coordinates[0] + coordinates[1]
                if len(coordinates) == 3:  # special case for when we have a coordinate that starts on the 10th column
                    space = coordinates[0] + coordinates[1] + coordinates[2]
                place = int(self._column_legend[coordinates[0]])  # we convert the letter to a number so we can iterate
                self._P1_ships[coordinates] = []
                for segments in range(length):
                    self._board_P1[space] = "occupied"
                    self._P1_ships[coordinates] += [space]
                    place += 1
                    if len(coordinates) == 3:  # edge case if we have a coordinate that starts on the 10th column
                        space = self._column_legend[place] + coordinates[1] + coordinates[2]
                    else:
                        space = self._column_legend[place] + coordinates[1]
                return True

        if player == 'second':
            if orientation == 'R':  # further validates and places ships that are "row" oriented
                if self.is_valid(length, coordinates, orientation, self._board_P2) == False:
                    return False
                space = coordinates[0] + coordinates[1]
                place = int(coordinates[1])
                self._P2_ships[coordinates] = []
                for segments in range(length):
                    self._board_P2[space] = "occupied"
                    self._P2_ships[coordinates] += [space]
                    place += 1
                    space = coordinates[0] + str(place)
                return True

            if orientation == 'C':  # further validates and places ships that are "column" oriented
                if self.is_valid(length, coordinates, orientation, self._board_P2) == False:
                    return False
                space = coordinates[0] + coordinates[1]
                if len(coordinates) == 3:  # edge case if we have a coordinate that starts on the 10th column
                    space = coordinates[0] + coordinates[1] + coordinates[2]
                place = int(self._column_legend[coordinates[0]])
                self._P2_ships[coordinates] = []
                for segments in range(length):
                    self._board_P2[space] = "occupied"
                    self._P2_ships[coordinates] += [space]
                    place += 1
                    if len(coordinates) == 3:
                        space = self._column_legend[place] + coordinates[1] + coordinates[2]
                    else:
                        space = self._column_legend[place] + coordinates[1]
                return True

    def is_valid(self, length, coordinates, orientation, board):
        """ Helper method called to check whether or not the ship placement is valid. Is passed the length, coordinates,
        orientation of the ship, and the specified player's board."""
        if orientation == 'R':
            space = coordinates[0] + coordinates[1]
            place = int(coordinates[1])
            for tiles in range(length):
                if board[space] == "occupied":
                    return False
                place += 1
                space = coordinates[0] + str(place)

        if orientation == 'C':
            space = coordinates[0] + coordinates[1]
            if len(coordinates) == 3:  # edge case if we have a coordinate that starts on the 10th column
                space = coordinates[0] + coordinates[1] + coordinates[2]
            place = int(self._column_legend[coordinates[0]])
            for tiles in range(length - 1):
                if board[space] == "occupied":
                    return False
                place += 1
                if len(coordinates) == 3:
                    space = self._column_legend[place] + coordinates[1] + coordinates[2]
                else:
                    space = self._column_legend[place] + coordinates[1]
        return

    def fire_torpedo(self, player, coordinates):
        """ Fires a torpedo at the specified coordinates by the passed player. """
        if player != 'first' and player != 'second':
            return False
        if player != self._turn:
            return False
        if self._status == 'FIRST_WON' or self._status == 'SECOND_WON':
            return False

        if player == 'first':
            self._board_P2[coordinates] = 'empty'
            for ships in self._P2_ships:
                if coordinates in self._P2_ships[ships]:
                    self._P2_ships[ships].remove(coordinates)  # remove tile from list of occupied spaces for that ship

            for ships in self._P2_ships:
                if self._P2_ships[ships] == []:
                    del self._P2_ships[ships]
                    break  # exists the loop as soon as the ship is deleted to avoid key error, then runs rest of code

            if len(self.get_P2_ships()) == 0:  # checks if P2 has any ships remaining
                self._status = "FIRST_WON"
                return True
            self._turn = 'second'  # turn ends, other player's turn now
            return True

        if player == 'second':
            self._board_P1[coordinates] = 'empty'
            for ships in self._P1_ships:
                if coordinates in self._P1_ships[ships]:
                    self._P1_ships[ships].remove(coordinates)

            for ships in self._P1_ships:
                if self._P1_ships[ships] == []:
                    del self._P1_ships[ships]
                    break
            if len(self.get_P1_ships()) == 0:
                self._status = "SECOND_WON"
                return True
            self._turn = 'first'
            return True

    def get_num_ships_remaining(self, player):
        """ Takes as argument specific player and returns the number of ship objects player has left. """
        if player == 'first':
            return len(self.get_P1_ships())
        if player == 'second':
            return len(self.get_P2_ships())
        else:
            return False


class ShipGameOnePlayer:
    """ A class to represent the popular board-game Battleship that contains essential dictionary-lists and methods
    to initialize and play the game Battleship. """

    def __init__(self):
        """ Takes no parameters but initializes the necessary empty lists and the all-important "board" as a dictionary.
        Will also contain another dictionary that stores information about the players, including their ships, where
        they are placed, and the status of these ships. self._board_P1 and P2 are the individual players' boards and
         reflect the spaces their ships occupy. """

        self._board_P1 = {
            "A1": "empty",
            "A2": "empty",
            "A3": "empty",
            "A4": "empty",
            "A5": "empty",
            "A6": "empty",
            "A7": "empty",
            "A8": "empty",
            "A9": "empty",
            "A10": "empty",
            "B1": "empty",
            "B2": "empty",
            "B3": "empty",
            "B4": "empty",
            "B5": "empty",
            "B6": "empty",
            "B7": "empty",
            "B8": "empty",
            "B9": "empty",
            "B10": "empty",
            "C1": "empty",
            "C2": "empty",
            "C3": "empty",
            "C4": "empty",
            "C5": "empty",
            "C6": "empty",
            "C7": "empty",
            "C8": "empty",
            "C9": "empty",
            "C10": "empty",
            "D1": "empty",
            "D2": "empty",
            "D3": "empty",
            "D4": "empty",
            "D5": "empty",
            "D6": "empty",
            "D7": "empty",
            "D8": "empty",
            "D9": "empty",
            "D10": "empty",
            "E1": "empty",
            "E2": "empty",
            "E3": "empty",
            "E4": "empty",
            "E5": "empty",
            "E6": "empty",
            "E7": "empty",
            "E8": "empty",
            "E9": "empty",
            "E10": "empty",
            "F1": "empty",
            "F2": "empty",
            "F3": "empty",
            "F4": "empty",
            "F5": "empty",
            "F6": "empty",
            "F7": "empty",
            "F8": "empty",
            "F9": "empty",
            "F10": "empty",
            "G1": "empty",
            "G2": "empty",
            "G3": "empty",
            "G4": "empty",
            "G5": "empty",
            "G6": "empty",
            "G7": "empty",
            "G8": "empty",
            "G9": "empty",
            "G10": "empty",
            "H1": "empty",
            "H2": "empty",
            "H3": "empty",
            "H4": "empty",
            "H5": "empty",
            "H6": "empty",
            "H7": "empty",
            "H8": "empty",
            "H9": "empty",
            "H10": "empty",
            "I1": "empty",
            "I2": "empty",
            "I3": "empty",
            "I4": "empty",
            "I5": "empty",
            "I6": "empty",
            "I7": "empty",
            "I8": "empty",
            "I9": "empty",
            "I10": "empty",
            "J1": "empty",
            "J2": "empty",
            "J3": "empty",
            "J4": "empty",
            "J5": "empty",
            "J6": "empty",
            "J7": "empty",
            "J8": "empty",
            "J9": "empty",
            "J10": "empty",
        }

        self._board_AI = {
            "A1": "occupied",
            "A2": "occupied",
            "A3": "occupied",
            "A4": "occupied",
            "A5": "occupied",
            "A6": "empty",
            "A7": "empty",
            "A8": "empty",
            "A9": "empty",
            "A10": "empty",
            "B1": "empty",
            "B2": "empty",
            "B3": "occupied",
            "B4": "empty",
            "B5": "empty",
            "B6": "empty",
            "B7": "empty",
            "B8": "empty",
            "B9": "empty",
            "B10": "empty",
            "C1": "empty",
            "C2": "empty",
            "C3": "occupied",
            "C4": "empty",
            "C5": "empty",
            "C6": "empty",
            "C7": "empty",
            "C8": "empty",
            "C9": "empty",
            "C10": "empty",
            "D1": "empty",
            "D2": "empty",
            "D3": "occupied",
            "D4": "empty",
            "D5": "empty",
            "D6": "empty",
            "D7": "empty",
            "D8": "empty",
            "D9": "empty",
            "D10": "empty",
            "E1": "empty",
            "E2": "empty",
            "E3": "occupied",
            "E4": "empty",
            "E5": "empty",
            "E6": "empty",
            "E7": "empty",
            "E8": "empty",
            "E9": "empty",
            "E10": "empty",
            "F1": "empty",
            "F2": "empty",
            "F3": "empty",
            "F4": "empty",
            "F5": "empty",
            "F6": "empty",
            "F7": "empty",
            "F8": "empty",
            "F9": "empty",
            "F10": "empty",
            "G1": "empty",
            "G2": "empty",
            "G3": "empty",
            "G4": "empty",
            "G5": "empty",
            "G6": "empty",
            "G7": "empty",
            "G8": "empty",
            "G9": "empty",
            "G10": "empty",
            "H1": "empty",
            "H2": "occupied",
            "H3": "occupied",
            "H4": "empty",
            "H5": "empty",
            "H6": "empty",
            "H7": "empty",
            "H8": "empty",
            "H9": "empty",
            "H10": "occupied",
            "I1": "empty",
            "I2": "empty",
            "I3": "empty",
            "I4": "empty",
            "I5": "empty",
            "I6": "empty",
            "I7": "empty",
            "I8": "empty",
            "I9": "empty",
            "I10": "occupied",
            "J1": "empty",
            "J2": "occupied",
            "J3": "occupied",
            "J4": "occupied",
            "J5": "empty",
            "J6": "empty",
            "J7": "empty",
            "J8": "empty",
            "J9": "empty",
            "J10": "occupied",
        }  # pre-initialized AI board

        self._column_legend = {
            "A": 1,
            "B": 2,
            "C": 3,
            "D": 4,
            "E": 5,
            "F": 6,
            "G": 7,
            "H": 8,
            "I": 9,
            "J": 10,

            1: "A",
            2: "B",
            3: "C",
            4: "D",
            5: "E",
            6: "F",
            7: "G",
            8: "H",
            9: "I",
            10: "J",
            11: "K"
        }  # this dictionary allows the place_ship method to iterate through letters for placement and validation

        self._P1_ships = {}  # dictionary that holds lists representing battleships

        self._AI_ships = {"A1": ["A1", "A2", "A3", "A4", "A5"],
                          "B3": ["B3", "C3", "D3", "E3"],
                          "J2": ["J2", "J3", "J4"],
                          "H10": ["H10", "I10", "J10"],
                          "H2": ["H2", "H3"], }  # pre-initialized AI Ships

        self._turn = "first"  # Initialized to player 1, as player 1 starts the game after battleships are placed.

        self._status = "UNFINISHED"
        # The status of the game will be initialized to unfinished as the game is either finished or it is not.
        # At the end of fire_torpedo, if a player has no more ships then this is changed to FIRST_WON or SECOND_WON

    def get_current_state(self):
        """ This method returns the current state of the game. """
        return self._status

    def get_P1_ships(self):
        """ Returns the dictionary of player 1's currently active ships. """
        return self._P1_ships

    def get_AI_ships(self):
        """ Returns the dictionary of player 2's currently active ships. """
        return self._AI_ships

    def get_P1_board(self):
        """ Returns the current state of player 1's board. """
        return self._board_P1

    def get_AI_board(self):
        """ Returns the current state of player 2's board. """
        return self._board_AI

    def place_ship(self, player, length, coordinates, orientation):
        """ Checks the values of the passed parameters and return False if any are not valid. The
       method will call an additional helper method to further validate passed parameters and then create the ship
       objects, place them on player boards, and update the list of player ships."""
        if player != 'first' and player != 'second':  # some initial data validations before placing ships
            return False
        if length > 10 or length <= 1:  # ships must be at least 2 and no more than 10 in length
            return False
        if orientation != 'C' and orientation != 'R':
            return False
        if orientation == "R":  # initial data validation for ships placed as a "row" orientation
            if length + int(coordinates[1]) > 11:
                return False
            if len(coordinates) > 3:  # ships must be at least 2 in length, so an attempt on the 10th column is invalid
                return False
            if len(coordinates) == 3:
                return False
        if orientation == "C":
            if length + self._column_legend[coordinates[0]] > 11:  # if the ship is not fully on the board vertically
                return False
        if coordinates[0] not in self._column_legend:  # ensures passed coordinates are on the board
            return False
        if len(coordinates) >= 4:
            return False

        if player == 'first':
            if orientation == 'R':  # further validates and places ships that are "row" oriented
                if self.is_valid(length, coordinates, orientation, self._board_P1) == False:  # helper validation method
                    return False
                space = coordinates[0] + coordinates[1]
                place = int(coordinates[1])  # allows us to iterate horizontally across specified row
                self._P1_ships[coordinates] = []  # creates the empty list to be filled and put into P1_ships dictionary
                for segments in range(length):
                    self._board_P1[space] = "occupied"
                    self._P1_ships[coordinates] += [space]  # appends coordinates to current ship's occupied spaces
                    place += 1
                    space = coordinates[0] + str(place)
                return True

            if orientation == 'C':  # further validates and places ships that are "column" oriented
                if self.is_valid(length, coordinates, orientation, self._board_P1) == False:
                    return False
                space = coordinates[0] + coordinates[1]
                if len(coordinates) == 3:  # special case for when we have a coordinate that starts on the 10th column
                    space = coordinates[0] + coordinates[1] + coordinates[2]
                place = int(self._column_legend[coordinates[0]])  # we convert the letter to a number so we can iterate
                self._P1_ships[coordinates] = []
                for segments in range(length):
                    self._board_P1[space] = "occupied"
                    self._P1_ships[coordinates] += [space]
                    place += 1
                    if len(coordinates) == 3:  # edge case if we have a coordinate that starts on the 10th column
                        space = self._column_legend[place] + coordinates[1] + coordinates[2]
                    else:
                        space = self._column_legend[place] + coordinates[1]
                return True

    def is_valid(self, length, coordinates, orientation, board):
        """ Helper method called to check whether or not the ship placement is valid. Is passed the length, coordinates,
        orientation of the ship, and the specified player's board."""
        if orientation == 'R':
            space = coordinates[0] + coordinates[1]
            place = int(coordinates[1])
            for tiles in range(length):
                if board[space] == "occupied":
                    return False
                place += 1
                space = coordinates[0] + str(place)

        if orientation == 'C':
            space = coordinates[0] + coordinates[1]
            if len(coordinates) == 3:  # edge case if we have a coordinate that starts on the 10th column
                space = coordinates[0] + coordinates[1] + coordinates[2]
            place = int(self._column_legend[coordinates[0]])
            for tiles in range(length - 1):
                if board[space] == "occupied":
                    return False
                place += 1
                if len(coordinates) == 3:
                    space = self._column_legend[place] + coordinates[1] + coordinates[2]
                else:
                    space = self._column_legend[place] + coordinates[1]
        return

    def fire_torpedo(self, player, coordinates):
        """ Fires a torpedo at the specified coordinates by the player. """
        if player != 'first' and player != 'AI':
            return False
        if player != self._turn:
            return False
        if self._status == 'FIRST_WON' or self._status == 'AI_WON':
            return False

        if player == 'first':
            self._board_AI[coordinates] = 'empty'
            for ships in self._AI_ships:
                if coordinates in self._AI_ships[ships]:
                    self._AI_ships[ships].remove(coordinates)  # remove tile from list of occupied spaces for that ship
                    print("Ship Hit!!")

            for ships in self._AI_ships:
                if self._AI_ships[ships] == []:
                    del self._AI_ships[ships]
                    print("Ship Sunk!!")
                    break  # exists the loop as soon as the ship is deleted to avoid key error, then runs rest of code

            if len(self.get_AI_ships()) == 0:  # checks if P2 has any ships remaining
                self._status = "FIRST_WON"
                return True
            self._turn = 'AI'  # turn ends, AI's turn now
            self.AI_Torpedo()
            return

    def start_game(self):
        """ Fires a torpedo at the specified coordinates by the player. """

        if self._status == 'FIRST_WON' or self._status == 'AI_WON':
            return False
        print("Turn: Player 1")
        coordinates = input("Player 1 Enter Torpedo Coordinates(A to J + 1 to 10): ")

        while coordinates not in self.get_P1_board():
            print("Invalid Space, please try again. ")
            coordinates = input("Player 1 Enter Torpedo Coordinates(A to J + 1 to 10): ")

        self._board_AI[coordinates] = 'empty'
        hit = 0
        for ships in self._AI_ships:
            if coordinates in self._AI_ships[ships]:
                self._AI_ships[ships].remove(coordinates)  # remove tile from list of occupied spaces for that ship
                hit = 1

        if hit == 0:
            print("Miss!!")
        else:
            print("Ship hit!!")

        for ships in self._AI_ships:
            if self._AI_ships[ships] == []:
                del self._AI_ships[ships]
                print("Ship Sunk!!")
                break  # exists the loop as soon as the ship is deleted to avoid key error, then runs rest of code

        if len(self.get_AI_ships()) == 0:  # checks if AI has any ships remaining
            self._status = "FIRST_WON"
            self.endgame()

        self._turn = 'AI'  # turn ends, AI's turn now
        self.AI_Torpedo()

        self.start_game()

    def AI_Torpedo(self):
        print("")
        print("Turn: AI")

        # coordinates must be randomized
        coordinates = self._column_legend[random.randint(1, 10)] + str(random.randint(1, 10))
        print("AI Hits:", coordinates)

        hit = 0
        self._board_P1[coordinates] = 'empty'
        for ships in self._P1_ships:
            if coordinates in self._P1_ships[ships]:
                self._P1_ships[ships].remove(coordinates)
                hit = 1

        if hit == 0:
            print("Miss!!")
        else:
            print("Ship hit!!")


        for ships in self._P1_ships:
            if self._P1_ships[ships] == []:
                del self._P1_ships[ships]
                print("Ship Sunk!!")
                break

        if len(self.get_P1_ships()) == 0:
            self._status = "AI_WON"
            self.endgame()

        print("")
        self._turn = 'first'
        return

    def get_num_ships_remaining(self, player):
        """ Takes as argument specific player and returns the number of ship objects player has left. """
        if player == 'first':
            return len(self.get_P1_ships())
        if player == 'second':
            return len(self.get_AI_ships())
        else:
            return False

    def endgame(self):
        """ Called when no ships remain on either player or AI side. """

        if self._status == "AI_WON":
            print("Game Over! The AI won!")
            quit()

        if self._status == "FIRST_WON":
            print("Great Job! You won!")
            quit()

game = ShipGameOnePlayer()
game.place_ship("first", 5, "A1", "R")
game.place_ship("first", 4, "B3", "C")
game.place_ship("first", 3, "J2", "R")
game.place_ship("first", 3, "H10", "C")
game.place_ship("first", 2, "H2", "R")

game.start_game()
# game.place_ship("second", 2, "D9", "R")
# game.place_ship("second", 4, "F10", "C")
#
# print(game.fire_torpedo("first", "A1"))
#
# # print(game.fire_torpedo("second", "A1"))
# print(game.fire_torpedo("first", "H2"))
# print(game.fire_torpedo("second", "A2"))
# print(game.fire_torpedo("first", "H3"))
# game.fire_torpedo("first", "K7")
# print("P1 Ships: ", game.get_P1_ships())
# print("AI Ships: ", game.get_AI_ships())
# print(game.fire_torpedo("second", "J3"))
# print(game.fire_torpedo("first", "F10"))
# print(game.fire_torpedo("second", "G10"))
# print(game.fire_torpedo("first", "F7"))
# print(game.fire_torpedo("second", "B3"))
# print(game.fire_torpedo("first", "C4"))
# print(game.fire_torpedo("second", "A3"))
# print(game.fire_torpedo("first", "F7"))
# print(game.fire_torpedo("second", "J2"))
# print(game.fire_torpedo("first", "F7"))
# print(game.fire_torpedo("second", "J4"))
#
#
#
# if __name__ == '__main__':
#     print("++++++++++++++++++++++++++++++++++++++++")
#     print("CURRENT STATE: ", game.get_current_state())
#     print("FIRST ships remaining:", game.get_num_ships_remaining("first"))
#     print("FIRST ships inventory:", game.get_P1_ships())
#     print("\n")
#     print("SECOND ships remaining:", game.get_num_ships_remaining("second"))
#     print("SECOND ships inventory:", game.get_P2_ships())
#
#     print(game.print_occupied())
