#CryptCoin-Final Project
#David Armstrong
#Group 1
class Coin:
    def __init__(self, name, price, toughness):
        self.name = name
        self.price = price
        self.toughness = toughness
    def __str__(self):
        return f"Name: {self.name}, Price: {self.price}, Toughness: {self.toughness}"
class Player:
    def __init__(self, name, hp, dmg):
        self.name = name
        self.hp = (int)hp
        self.dmg = (int)dmg
    def attack(self, enemy):
        enemy.hp -= self.dmg
class Goblin(self, name, hp, dmg):
    def __init__(self, name, hp, dmg):
        self.name = "goblin"
        self.hp = (int)20
        self.dmg = (int)5
    def attack(self, player):
        player.hp -= self.dmg
class Troll(self, name, hp, dmg):
    def __init__(self, name, hp, dmg):
        self.name = "Troll"
        self.hp = (int)30
        self.dmg = (int)8
    def attack(self, player):
        player.hp -= self.dmg
class Dwarf(self, name, hp, dmg):
    def __init__(self, name, hp, dmg):
        self.name = "Dwarf"
        self.hp = (int)40
        self.dmg = (int)12
    def attack(self, player):
        player.hp -= self.dmg
class Shade(self, name, hp, dmg):
    def __init__(self, name, hp, dmg):
        self.name = "Dwarf"
        self.hp = (int)75
        self.dmg = (int)29
    def attack(self, player):
        player.hp -= self.dmg
coinDictionary = {
    "DOGE": Coin("Dogecoin", 0.15, 4.0),
    "ADA": Coin("Cardano", 0.45, 3.8),
    "DOT": Coin("Polkadot", 7.20, 6.0),
    "AVAX": Coin("Avalanche", 50.00, 6.7),
    "LTC": Coin("Litecoin", 95.00, 6.2),
    "SOL": Coin("Solana", 140.00, 7.5),
    "XMR": Coin("Monero", 160.00, 7.1),
    "BNB": Coin("Binance Coin", 600.00, 8.2),
    "ETH": Coin("Ethereum", 3200.00, 8.5),
    "BTC": Coin("Bitcoin", 67000.00, 9.8)
}
promptFile = open("CryptCoin.txt", 'r')
def loadData():
    with open("PlayerStats.txt", "r") as file:
        line = file.readline()
        while line:
            parts = line.strip().split(", ")
            name, hp, dmg = parts
            if len(parts) == 4:
                Player = Player(name, hp, dmg)
            
