L = [76, 92.3, "hello", True, 4, 76]

L.append("apple")
L.append(76)
L.insert(3, "cat")
L.insert(0, "hello")

C = L.count(76)
L.remove(76)
L.pop(L.index(True))