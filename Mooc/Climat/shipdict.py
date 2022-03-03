class Position():
    pass

class Ship():
    pass

class ShipDict():
    def __init__(self):
        self.ship_dict = []

    def add_chunk(self, chunk):
        self.ship_dict.append(chunk)

    def clean_unnamed(self):
        for ship in self.ship_dict:
            if ship[6] == '':
                self.ship_dict.remove(ship)

    def sort(self, key="default"):
        pass

    def all_ships(self):
        return self.ship_dict
    
    def ships_by_name(self, name):
        new_ship_dict = []
        for ship in self.ship_dict:
            if ship[6] == name:
                new_ship_dict.append(ship)
        return new_ship_dict