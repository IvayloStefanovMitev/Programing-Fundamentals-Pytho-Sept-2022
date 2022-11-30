materials = {'shards': 0, 'fragments': 0, 'motes': 0}
curr_materials = input().split()
obtained = False
while not obtained:

    for material in range(0, len(curr_materials), 2):
        quantity = int(curr_materials[material])
        picked_materials = curr_materials[material + 1].lower()
        if picked_materials not in materials.keys():
            materials[picked_materials] = 0
        materials[picked_materials] += quantity
        if materials['shards'] >= 250:
            print("Shadowmourne obtained!")
            materials['shards'] -= 250
            obtained = True
        elif materials['fragments'] >= 250:
            print("Valanyr obtained!")
            materials['fragments'] -= 250
            obtained = True
        elif materials['motes'] >= 250:
            print("Dragonwrath obtained!")
            materials['motes'] -= 250
            obtained = True
        if obtained:
            break
    if obtained:
        break
    curr_materials = input().split()
for picked_materials, quantity in materials.items():
    print(f'{picked_materials}: {quantity}')