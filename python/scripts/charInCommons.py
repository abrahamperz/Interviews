s1 ="and"
s2 ="art"
s3 ="be"

def commonChar(s1,s2):
    dict={}
    size1 = len(s1)
    size2 = len(s2)
    for i in range(size1):
        key = s1[i]
        if key not in dict:
            dict[key] = 1
    
    for i in range(size2):
        key = s2[i]
        if key in dict:
            dict[key] = dict[key] + 1

    for key,value in dict.items():
        if(value == 2):
            print("yes")
            break
        else:
            print("no")
            break

commonChar(s1,s3)




