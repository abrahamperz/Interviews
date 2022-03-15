def repeat(string):
    dict = {}
    size = len(string)
    for i in range(size):
        key = string[i]
        if key not in dict:
            dict[key] = 1
        else:
            dict[key] = dict[key] + 1
    for key,value in dict.items():
        if(value==1):
            print(key)
            break
    

repeat("abcdxerfgabcdef")
#print(dict.items())
