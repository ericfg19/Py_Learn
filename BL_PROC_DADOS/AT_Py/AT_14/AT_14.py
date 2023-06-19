def slot_items_backpack(file_path):
    with open(file_path, 'r') as file:
        backpacks_contents = file.readlines()

    common_items = []
    for backpack_content in backpacks_contents:
        half_length = len(backpack_content) // 2
        compartment1 = set(backpack_content[:half_length])
        compartment2 = set(backpack_content[half_length:])

        common_items.append(compartment1.intersection(compartment2))

    return common_items


file_path = 'exemplo.txt'
result = slot_items_backpack(file_path)
for index, common_items in enumerate(result, start=1):
    print(f"Tipo de item repetido no slot [{index}] da mochila: {', '.join(common_items)}")
