def characterFrequency(str1):
    str1 = str1.replace(" ","")
    dict1={}
    for c in str1:
        if c not in dict1:
            dict1[c] = 1
        else:
            dict1[c] += 1
    print(dict1)

characterFrequency("da aron aj ude")