# import zipfile

def line_number(key, place):
    line = ["1","2","3","4","5","6","7","8","9"]
    if place:
        return ["{}{}".format(key,a) for a in line]
    return ["{}{}".format(a,key) for a in line]

def cube(row, col):
    rows = [1,2,3]
    cols = rows.copy()
    if not int(row) / 6 <= 1:
        rows = [a+6 for a in rows]
    elif not int(row) / 3 <= 1:
        rows = [a+3 for a in rows]

    if not int(col) / 6 <= 1:
        cols = [a+6 for a in cols]
    elif not int(col) / 3 <= 1:
        cols = [a+3 for a in cols]

    hold = []
    for r in rows:
        for c in cols:
            hold.append("{}{}".format(r,c))
    return hold

def build_element(items):
    for i in range(1,10):
        for j in range(1,10):
            items["{}{}".format(i,j)] = []
    return items
    

if __name__ == "__main__":
    items = build_element({})
    
    for k,v in items.items():
        print(k, end=" ")
        neighbours = set([*line_number(k[0], True), *line_number(k[1], False), *cube(k[0], k[1])])
        neighbours.remove(k)
        items[k] = neighbours
        print(k, items[k], len(items[k]), end="\n\n\n")  

    with open("adjacency_list.txt", "w+") as f:
        for k, v in items.items():
            f.write("{}:{}\n".format(k, ",".join(list(v)))) 

  