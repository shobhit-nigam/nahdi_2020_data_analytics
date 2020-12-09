def search(p, e=6):
    path = "/Users/shobhit/Desktop/nahdi/"+p
    import os
    list_files = os.listdir(path)

    if e==6:
        print("extension not provided, giving list of all files")
        return list_files
    
    final = []
    for x in list_files:
        if x[-3:] == e:
            final.append(x)
    
    return final

#############################################

def search_replace(p, e):
    print("coding not yet complete")
    print("library under construction")

#############################################
