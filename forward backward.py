class Rule:
    def __init__(self, c, a):
        self.c, self.a = c, a

def forward_chain(r, f):
    n = set()
    while True:
        o = len(f)
        for rule in r:
            if all(a in f for a in rule.a):
                n.add(rule.c)
        f |= n
        if len(f) == o:
            break
    return f

def backward_chain(r, g, f):
    if g in f: return True
    for rule in r:
        if rule.c == g and all(backward_chain(r, a, f) for a in rule.a):
            return True
    return False

rules = [Rule("happy", ["sunny"]), Rule("sunny", ["no rain"]), Rule("no rain", ["no clouds"])]

initial_facts = {"no clouds"}
goal = "happy"

inferred_facts = forward_chain(rules, initial_facts)

print("Inferred facts:", inferred_facts)

'''
output:
Inferred facts: {'no clouds', 'no rain', 'sunny', 'happy'}
Goal is achievable!
'''
if backward_chain(rules, goal, initial_facts):
    print("Goal is achievable!")
else:
    print("Goal is not achievable.")
