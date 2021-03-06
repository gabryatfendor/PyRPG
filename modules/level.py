"""Single map properties"""
import random

from .graphics import Tiles
from .ai import Npc

class Level:
    """Level properties"""
    def __init__(self, level_path, player_direction, tile_background):
        """Initializer with level properties"""
        self.level_path = level_path
        self.player_direction = player_direction
        self.tile_background = Tiles.environment[tile_background]
        self.array_map = Level.import_map(self.level_path)
        self.dimension = [len(self.array_map[0]), len(self.array_map)]
        self.walkability_map = Level.draw_walk_map(self.array_map)
        self.tile_map = Level.convert_map_to_tile(self.array_map)
        self.exit_coords = self.set_coords_with_char('X')
        self.player_coords = self.set_coords_with_char('S')
        self.npc_array = self.set_npc_array('K')

    def set_coords_with_char(self, char_to_search):
        """set coordinates from char, to be searched in the map"""
        exit_coords = [x for x in self.array_map if char_to_search in x][0]
        exit_coords = [self.array_map.index(exit_coords), exit_coords.index(char_to_search)]
        return exit_coords

    def set_npc_array(self, npc_char):
        """npc_array creation"""
        npc_array = []
        for idx, i in enumerate(self.array_map):
            for jdx, j in enumerate(i):
                if j == npc_char:
                    new_npc = Npc(idx, jdx, Tiles.knight)
                    npc_array.append(new_npc)
        return npc_array

    @staticmethod
    def convert_map_to_tile(map_array):
        """Convert every single char from the configuration in the path to the tile to be drawn"""
        tile_array = []
        tile_column = []
        for column in map_array:
            for char in column:
                if char == ' ' or char == 'K' or char == 'S':
                    tile_column.append(Tiles.environment['grass'])
                elif char == 'W':
                    tile_column.append(random.choice(Tiles.environment['water']))
                elif char == 'T':
                    tile_column.append(random.choice(Tiles.environment['tree']))
                elif char == '#':
                    tile_column.append(Tiles.environment['wall'])
                elif char == '-':
                    tile_column.append(Tiles.environment['nothing'])
                elif char == 'X':
                    tile_column.append(Tiles.environment['exit'])
            tile_array.append(tile_column)
            tile_column = []

        return tile_array

    @staticmethod
    def draw_walk_map(map_array):
        """Write the walkability map to be used when we move the char directly from the array map imported from the file (nothing dynamic in it)"""
        map_to_return = []
        column_to_append = []
        for column in map_array:
            for char in column:
                if char == ' ' or char == 'X' or char == '-' or char == 'K' or char == 'S':
                    column_to_append.append(True)
                else:
                    column_to_append.append(False)
            map_to_return.append(column_to_append)
            column_to_append = []

        return map_to_return

    @staticmethod
    def import_map(file_path):
        """Importing map from file line by line"""
        array_to_return = []
        with open(file_path, "r") as ins:
            line_array = []
            for line in ins:
                line_array.append(line)

        for line in line_array:
            array_to_return.append(line[:-1])

        return list(zip(*array_to_return))

    @staticmethod
    def set_level_name(level_path):
        """level name is after _ in file name"""
        full_path = level_path
        full_path = ''.join([i for i in full_path if not i.isdigit()]).replace("_", "")
        return full_path
