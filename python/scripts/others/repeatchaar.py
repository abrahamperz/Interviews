s="abcdxefbcdef"

def re(string):
    dict={}
    size=len(string)
    for i in range(size):
        key=string[i]
        if key not in dict:
            dict[key] =1 
        else:
            print([key])
            break
            #dict[key] = dict[key] + 1
   # print(dict)
    #for key,value in dict.items():
     #   if(value ==2):
      #      print(key,value)
       #     break


        
re(s)  
