from prettytable import PrettyTable

def infer_components(assembly):
    components = {}
    new_tuples_generated = True

    while new_tuples_generated:
        new_tuples_generated = False
        for part, subpart, qty in assembly:
            if part not in components:
                components[part] = []
            if subpart not in components:
                components[subpart] = []
            if (subpart, qty) not in components[part]:
                components[part].append((subpart, qty))
                components[part].extend(components.get(subpart, []))
                new_tuples_generated = True

    return components

def get_all_subparts(part, components):
    all_subparts = []
    for subpart, qty in components[part]:
        all_subparts.append((subpart, qty))
        all_subparts.extend(get_all_subparts(subpart, components))
    return all_subparts

def print_table(data):
    table = PrettyTable()
    table.field_names = ["Part", "Subpart", "Quantity"]
    for part, subparts in data.items():
        for subpart, qty in subparts:
            table.add_row([part, subpart, qty])
    print(table)

# Ask for assembly relationships input from the user
assembly = []
while True:
    part = input("Enter part (press Enter to stop): ").strip()
    if not part:
        break
    subpart = input("Enter subpart: ").strip()
    quantity = int(input("Enter quantity: "))
    assembly.append((part, subpart, quantity))

# Get the inferred components relation
components_relation = infer_components(assembly)

# Print the first table
print_table(components_relation)

# Ask for input part
input_part = input("Enter a part: ").strip()

if input_part in components_relation:
    all_subparts = get_all_subparts(input_part, components_relation)
    print_table({input_part: all_subparts})
else:
    print("Part not found.")
