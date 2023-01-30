a = {2: "a", 1: "b"}

print(dict(sorted(a.items(), key=lambda x: x[0])))