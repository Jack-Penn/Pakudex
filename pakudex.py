from gc import get_stats

from pakuri import Pakuri

class Pakudex:
    def __init__(self, capacity = 20):
        self.capacity = capacity
        self.speciesList = []
    def get_size(self):
        return len(self.speciesList)
    def get_capacity(self):
        return self.capacity
    def get_species_array(self):
        if(self.get_size() == 0):
            return None
        return [pakuri.get_species() for pakuri in self.speciesList]
    def get_stats(self, species: str):
        try:
            p: Pakuri = next(p for p in self.speciesList if p.get_species() == species)
            return [p.attack, p.defense, p.speed]
        except StopIteration:
            return None
    def sort_pakuri(self):
        self.speciesList.sort(key=lambda p: p.get_species())
    def add_pakuri(self, species: str):
        if(self.get_size() < self.capacity and self.get_stats(species) == None):
            self.speciesList.append(Pakuri(species))
            return True
        return False
    def evolve_species(self, species: str):
        try:
            p: Pakuri = next(p for p in self.speciesList if p.get_species() == species)
            p.evolve()
            return True
        except StopIteration:
            return False