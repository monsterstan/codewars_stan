def count_positives_sum_negatives(list_de_base):
    list = [0, 0]
    for element in list_de_base:
        if element > 0: 
            list[0] += 1 # RAJOUTE 1
        elif element < 0:
            list[1] += element # RAJOUTE l'élément
        
        
    if len(list_de_base) < 1:
       list = []

    return list