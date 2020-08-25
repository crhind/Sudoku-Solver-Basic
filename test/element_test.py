from ..src.element import Node

node = Node("11")

def add_neighbour():
    neighbour_node = Node("12")
    neighbour_node.value = 2
    node.addNeighbour(neighbour_node)
    assert neighbour_node in node.neighbours

def test_contains(value):
    new_node = Node("21")
    node.addNeighbour(new_node)
    new_node.value = 3
    assert node.contiains(value)

if __name__ == '__main__':
    add_neighbour()
    test_contains(2)