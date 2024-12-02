
with open("test.txt") as f:
    content = f.read().split("\n\n")

instructions = content[0]
nodes = content[1:][0].split("\n")

nodes_dict = {}

for node in nodes:
    key = node.split(" = ")[0]
    if key not in nodes_dict:
        nodes_dict[key] = tuple(map(str, node.split(" = ")[1].replace("(", "").replace(")", "").split(", ")))

def p1(instructions, nodes):
    characters = [chr for chr in instructions]
    keys = [i for i in nodes.keys()]
    index = 0
    for chr in characters:
        print(keys[index], nodes[keys[index]])
        if chr == "R":
            index += keys.index(nodes[keys[index]][1])
        else:
            index += keys.index(nodes[keys[index]][0])
p1(instructions, nodes_dict)