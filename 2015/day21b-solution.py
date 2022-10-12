#!/usr/bin/python3
import json
import copy

# Opening JSON file
with open('day21-puzzle-input.txt') as json_file:
    data = json.load(json_file)


gear_options = []

gear = []
cost = 0
damage = 0
armor = 0

#Weapons: pick one of 5
#Armor: pick one of 6
#Rings: pick two of 8

for weapon_name in data['weapons']:
    weapon = data['weapons'][weapon_name]
    gear = {
        "weapon": weapon_name,
        "shield": "",
        "rings": [],
        "cost": 0,
        "armor": 0,
        "damage": 0
    }
    gear['cost'] = weapon['cost']
    gear['armor'] = weapon['armor']
    gear['damage'] = weapon['damage']
    
    shields = copy.deepcopy(data['armor'])

    for shield_name in shields:
        
        shield = shields[shield_name]
        
        shield_gear_1 = copy.deepcopy(gear)
        shield_gear_1["shield"] = shield_name
        shield_gear_1["cost"] += shield["cost"]
        shield_gear_1["armor"] += shield["armor"]
        shield_gear_1["damage"] += shield["damage"]
    
        rings = copy.deepcopy(data['rings'])
        
        for ring_name in rings:
        
            ring = rings[ring_name]
        
            rings_gear_1 = copy.deepcopy(shield_gear_1)
            rings_gear_1["rings"].append(ring_name)
            rings_gear_1["cost"] += ring["cost"]
            rings_gear_1["armor"] += ring["armor"]
            rings_gear_1["damage"] += ring["damage"]
            
            rings2 = copy.deepcopy(rings)
            rings2.pop(ring_name)

            for ring_name_2 in rings2:
            
                ring = rings2[ring_name_2]
            
                rings_gear_2 = copy.deepcopy(rings_gear_1)
                rings_gear_2["rings"].append(ring_name_2)
                rings_gear_2["cost"] += ring["cost"]
                rings_gear_2["armor"] += ring["armor"]
                rings_gear_2["damage"] += ring["damage"]
                
                rings_gear_2["rings"] = sorted(rings_gear_2["rings"])
                
                if rings_gear_2 not in gear_options:
                    gear_options.append(rings_gear_2)

gear_list = sorted(gear_options, key=lambda d: d['cost']) 

boss = {
    "hit_points" : 100,
    "damage" : 8,
    "armor" : 2
}

player = {
    "hit_points": 100,
    "damage": 0,
    "armor": 0
}

def attack(a, b):
    
    damage = a["damage"] - b["armor"]
    damage = damage if damage > 1 else 1
    b["hit_points"] -= damage;

    return b

max_game_over_amount = 0
for gear in gear_list:
    player["hit_points"] = 100
    player["damage"] = gear["damage"]
    player["armor"] = gear["armor"]
   
    boss["hit_points"] = 100

    player_moves = True
    while boss["hit_points"] >= 0 and player["hit_points"] >= 0:
        if player_moves:
            boss = attack(player, boss)
            player_moves = False
        else:
            player = attack(boss, player)
            player_moves = True

        if player["hit_points"] < 0:
            max_game_over_amount = gear["cost"]
            break

print("Boss wins!")
print("And the shopkeeper cleaned me out for", max_game_over_amount, "gold")
#---> 158 gold 
