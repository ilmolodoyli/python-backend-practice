helmets = [12000, 8000, 15000, 13000, 10000]
diff = 5000
def fuck(helmets, diff):
    for go in range(len(helmets)):
        for gogo in range(len(helmets)):
            if go != gogo:
                if helmets[go] - helmets[gogo] == diff:
                    return[helmets[go], helmets[gogo]]
print(fuck(helmets, diff))