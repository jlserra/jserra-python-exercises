class Pokemon:
    def __init__(self, species, damage, health = 100):
        self.species = species
        self.damage = damage
        self.health = health

    def attack(self,enemyPokemon):
        enemyPokemon.health -= self.damage

    def displayStatistics(self):
        print "Pokemon Statistics"
        print "Species: ", self.species
        print "Damage: ", self.damage
        print "Health: ", self.health
        
Pikachu = Pokemon("Electric Type", 120, 200)
Squirtle = Pokemon("Water Type", 100, 150)

Pikachu.displayStatistics()
Squirtle.displayStatistics()

Pikachu.attack(Squirtle)
Squirtle.attack(Pikachu)

Pikachu.displayStatistics()
Squirtle.displayStatistics()

