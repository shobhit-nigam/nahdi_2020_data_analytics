def search (p,e):
    # We are creating a function searching in a path (p) for an extension(e)
    path='C:\\Users\\hegazy.mh\\Desktop\\Python 20200915\\'+p
    # Now, we make the path as a two step, one is fixed & the other is variable to be added to each search step.
    import os
    list_files = os.listdir(path)
    # We make a variable called "List_files", that contains all directory in the path
    Final = []
    # We craete a new list called "Final & empty to append the product to it
    for x in list_files:
        if x[-3:]=="ynb":
            Final.append(x)
    return(Final)
######################################## Not required that line
def search_replace(p,e):
    print("coding is not completed yet")
    print("Liberary under construction")
 #######################################  Not required that line 
