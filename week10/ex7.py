def replace(s, old, new):
    return new.join(s.split(old))

print(replace("Mississippi", "i", "I"))