from scipy.spatial.distance import cosine

content = {
    'space exploration': [0.8, -0.3, 0.6],
    'astronomy': [0.7, -0.2, 0.8],
    'rocket technology': [0.6, -0.1, 0.7]
}

interests = ['space exploration', 'cosmic discoveries']
embedding = [0.75, -0.25, 0.7]

related = []
for con, embed in content.items():
    sim = 1 - cosine(embedding, embed)
    related.append((con, sim))

related.sort(key=lambda x: x[1], reverse=True)
suggested = [c for c,_ in related]

print("Suggested content:", suggested)

'''
output:
Suggested content: ['astronomy', 'space exploration', 'rocket technology']
'''
