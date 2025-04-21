#CryptCoin-Final Project
#David Armstrong
#Group 1
class Coin:
    def __init__(self, name, price, toughness, hp):
        self.name = name
        self.price = price
        self.toughness = toughness
        self.hp = hp
    def __str__(self):
        return f"Name: {self.name}, Price: {self.price}, Toughness: {self.toughness}"
class Player:
    def __init__(self, name, hp, money):
        self.name = name
        self.hp = int(hp)
        self.money = int(money)
    def attack(self, enemy):
        enemy.hp -= self.dmg
class npc:
    def __init__(self, name):
        self.name = name
        self.reputation = reputation
class ShopKeeper(npc):
    def __init__(self, reputation):
        self.reputation = reputation
        super().__init__("Sherman")
class Enemy:
    def __init__(self, name, hp, dmg):
        self.name = name
        self.hp = hp
        self.dmg = dmg
    def attack(self, player):
        player.hp -= self.dmg
class Goblin(Enemy):
    def __init__(self):
        super().__init__("Goblin", 20, 5)

class Troll(Enemy):
    def __init__(self):
        super().__init__("Troll", 30, 8)

class Dwarf(Enemy):
    def __init__(self):
        super().__init__("Dwarf", 40, 12)

class Shade(Enemy):
    def __init__(self):
        super().__init__("Shade", 75, 29)
class Tool():
    def __init__(self, name, dmg, coinDmg, price):
        self.name = name
        self.dmg = dmg
        self.coinDmg = coinDmg
        self.durability = 100
        self.price = price
    def __str__(self):
        return f"{self.name}, dmg: {self.dmg}, durability: {self.durability}, price: {self.price}"
coinDictionary = {
    "DOGE": Coin("Dogecoin", 0.15, 4.0, 10),
    "ADA": Coin("Cardano", 0.45, 3.8, 20),
    "DOT": Coin("Polkadot", 7.20, 6.0, 50),
    "AVAX": Coin("Avalanche", 50.00, 6.7, 200),
    "LTC": Coin("Litecoin", 95.00, 6.2, 500),
    "SOL": Coin("Solana", 140.00, 7.5, 700),
    "XMR": Coin("Monero", 160.00, 7.1, 750),
    "BNB": Coin("Binance Coin", 600.00, 8.2, 1500),
    "ETH": Coin("Ethereum", 3200.00, 8.5, 10000),
    "BTC": Coin("Bitcoin", 67000.00, 9.8, 100000)
}
toolDictionary = {
    "Axe": Tool("Axe", 15, 2, 10.00),
    "Mace": Tool("mace", 10, 4, 50.00),
    "Pickaxe": Tool("Pickaxe", 5, 15, 100.00),
    "Zweihander": Tool("Zweihander", 30, 1, 250.00),
    "GreatAxe": Tool("Great Axe", 50, 4, 500.00),
    "Drill": Tool("Drill", 8, 70, 500.00),
    "SledgeHammer": Tool("Sledge Hammer", 65, 50, 400.00),
    "GreatDrill": Tool("Great Drill", 35, 200, 1000.00)
}

def loadData():
    with open("PlayerStats.txt", "r") as file:
        line = file.readline()
        if line:
            parts = line.strip().split(", ")
            if len(parts) == 4:
                name, hp, money = parts
                return Player(name, hp, money)
    print("Data Loaded")
def saveData(player):
    with open("PlayerStats.txt", 'w') as file:
        file.write(f"{player.name}, {player.hp}, {player.money}")
    print("Data Saved.")
def gameStart():
    while(True):
        choice = input("(1)new game, (2)load saved game")
        if choice == "1":
            with open("CryptCoin.txt", "r") as file:
                line = file.readline()
                while(line):
                    print(line)
                    line = file.readline()
            name = input("What is your name?")
            player = Player(name, 50, 50)
            return player
        elif choice == "2":
            player = loadData()
            return player
        else:
            print("invalid choice, try again")

player = gameStart()
            
