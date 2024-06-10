knowledge_base = []

def is_parent(x, y):
    return (x, "parent", y) in knowledge_base

def is_grandparent(x, y):
    for z in knowledge_base:
        if z[1] == "parent" and z[2] == y:
            return is_parent(x, z[0])
    return False

def add_knowledge(knowledge, fact):
    if fact not in knowledge:
        knowledge.append(fact)

def infer_grandparent(knowledge, x, y):
    for z in knowledge:
        if z[1] == "parent" and z[2] == y:
            if is_parent(x, z[0]):
                return True
    return False

add_knowledge(knowledge_base, ("John", "parent", "Alice"))
add_knowledge(knowledge_base, ("Alice", "parent", "Bob"))
print(is_parent("John", "Alice")) 
print(infer_grandparent(knowledge_base, "John", "Bob"))
