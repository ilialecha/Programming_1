from easyinput import read_line

data = read_line()
total_pairs = 0
pairs = []
queries = []
while data is not None:
    if total_pairs ==0:
        total_pairs = int(data)
    else:
        if len(pairs) < total_pairs:
            pairs.append(data.split())
            
        else:
            queries.append(data.strip())
    data = read_line()

print(pairs)
outputs = []

for query in queries:
    
    for pair in pairs:
        if query in pair[0]:
            outputs.append(pair[0])
        else:
            outputs.append(pair[0])
print(outputs)