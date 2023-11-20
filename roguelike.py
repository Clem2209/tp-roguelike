
# Importer le module random pour générer de l'aléatoire
import random


# Définir les caractéristiques du joueur
player = {
    "name": "Cédric",
    "hp": 1000, 
    "atk": 100, 
    "def": 5, 
    "inv": [] 
}

# Définir les caractéristiques des monstres
monsters = [
    {
        "name": "Goblin",
        "hp": 20,
        "atk": 5,
        "def": 2
    },
    {
        "name": "Orc",
        "hp": 40,
        "atk": 10,
        "def": 4
    },
    {
        "name": "Dragon",
        "hp": 100,
        "atk": 20,
        "def": 10
    }
]

# Définir les caractéristiques des objets
items = [
    {
        "name": "Potion",
        "effect": lambda p: p.update({"hp": min(p["hp"] + 20, 100)}) 
    },
    {
        "name": "Sword",
        "effect": lambda p: p.update({"atk": p["atk"] + 5}) 
    },
    {
        "name": "Shield",
        "effect": lambda p: p.update({"def": p["def"] + 5}) 
    }
]

# Définir une fonction pour afficher le menu principal
def main_menu():
    print("Bienvenue dans le jeu Rogue MAALSI !")
    print("1. Commencer une nouvelle partie")
    print("2. Quitter le jeu")
    choice = input("Que voulez-vous faire ? ")
    if choice == "1":
        start_game() 
    elif choice == "2":
        exit() 
    else:
        print("Choix invalide !")
        main_menu() 

# Définir une fonction pour lancer le jeu
def start_game():
    print("Vous entrez dans le donjon...")
    level = 1 
    while level <= 5: 
        print(f"Vous êtes au niveau {level}")
        explore_level(level) 
        level += 1 
    print("Vous avez vaincu le dragon et vous sortez du donjon !")
    print("Félicitations, vous avez gagné le jeu !")

# Définir une fonction pour explorer un niveau
def explore_level(level):
    global player 
    rooms = 5 
    while rooms > 0: 
        print(f"Il vous reste {rooms} salles à explorer.")
        print("1. Explorer une salle")
        print("2. Voir votre inventaire")
        print("3. Voir vos caractéristiques")
        choice = input("Que voulez-vous faire ? ")
        if choice == "1":
            explore_room(level) 
            rooms -= 1 
        elif choice == "2":
            show_inventory() 
        elif choice == "3":
            show_stats() 
        else:
            print("Choix invalide !")
        if player["hp"] <= 0: 
            print("Vous êtes mort !")
            print("Game over !")
            exit() 

# Définir une fonction pour explorer une salle
def explore_room(level):
    global player 
    event = random.randint(1, 3) 
    if event == 1: 
        print("Vous trouvez un objet !")
        item = random.choice(items) 
        print(f"Vous trouvez une {item['name']}")
        print("1. Ramasser l'objet")
        print("2. Laisser l'objet")
        choice = input("Que voulez-vous faire ? ")
        if choice == "1":
            player["inv"].append(item) 
            print(f"Vous ramassez la {item['name']}")
        elif choice == "2":
            print(f"Vous laissez la {item['name']}")
        else:
            print("Choix invalide !")
    elif event == 2: 
        print("Vous rencontrez un monstre !")
        monster = random.choice(monsters[:level]) 
        print(f"Vous rencontrez un {monster['name']}")
        fight(monster) 
    elif event == 3: 
        print("Vous ne trouvez rien dans cette salle.")

# Définir une fonction pour combattre un monstre
def fight(monster):
    global player 
    while True: 
        print(f"Votre vie : {player['hp']}")
        print(f"Vie du monstre : {monster['hp']}")
        print("1. Attaquer")
        print("2. Utiliser un objet")
        print("3. Fuir")
        choice = input("Que voulez-vous faire ? ")
        if choice == "1":
            attack(monster) 
            if monster["hp"] <= 0: 
                print(f"Vous avez vaincu le {monster['name']} !")
                break 
        elif choice == "2":
            use_item() 
        elif choice == "3":
            flee(monster) 
            break 
        else:
            print("Choix invalide !")
        monster_attack(monster) 
        if player["hp"] <= 0: 
            print("Vous êtes mort !")
            print("Game over !")
            exit() 

# Définir une fonction pour attaquer un monstre
def attack(monster):
    global player 
    damage = player["atk"] - monster["def"] 
    if damage > 0:
        monster["hp"] -= damage 
        print(f"Vous infligez {damage} points de dégâts au {monster['name']}")
    else: 
        print(f"Vous ne parvenez pas à blesser le {monster['name']}")

# Définir une fonction pour utiliser un objet
def use_item():
    global player 
    if player["inv"]: 
        print("Voici votre inventaire :")
        for i, item in enumerate(player["inv"], 1): 
            print(f"{i}. {item['name']}") 
        choice = input("Quel objet voulez-vous utiliser ? ")
        try: 
            index = int(choice) - 1 
            item = player["inv"].pop(index) 
            item["effect"](player) 
            print(f"Vous utilisez la {item['name']}")
        except: 
            print("Choix invalide !")
    else: 
        print("Vous n'avez pas d'objet à utiliser !")

# Définir une fonction pour fuir un monstre
def flee(monster):
    global player 
    chance = random.randint(1, 10)
    if chance <= 3: 
        print(f"Vous parvenez à fuir le {monster['name']} !")
    else: 
        print(f"Vous ne parvenez pas à fuir le {monster['name']} ")
        monster_attack(monster) 

# Définir une fonction pour que le monstre attaque le joueur
def monster_attack(monster):
    global player 
    damage = monster["atk"] - player["def"] 
    if damage > 0: 
        player["hp"] -= damage 
        print(f"Le {monster['name']} vous inflige {damage} points de dégâts")
    else: 
        print(f"Vous parvenez à bloquer l'attaque du {monster['name']}")

# Définir une fonction pour afficher l'inventaire du joueur
def show_inventory():
    global player 
    if player["inv"]: 
        print("Voici votre inventaire :")
        for item in player["inv"]: 
            print(f"- {item['name']}")
    else: 
        print("Vous n'avez pas d'objet dans votre inventaire !")

# Définir une fonction pour afficher les caractéristiques du joueur
def show_stats():
    global player 
    print("Voici vos caractéristiques :")
    print(f"- Nom : {player['name']}")
    print(f"- Vie : {player['hp']}")
    print(f"- Attaque : {player['atk']}")
    print(f"- Défense : {player['def']}")

# Appeler la fonction main_menu pour lancer le jeu
main_menu()        