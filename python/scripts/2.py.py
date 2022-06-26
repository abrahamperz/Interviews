# Python3 implementation of the approach
repeat_string="abacaba"
print(max(repeat_string))

def getString(input_str):
    # Write your code here
    dict = {}
    str = ''
    for i in range(len(input_str)):
        key = input_str[i]
        if key not in dict:
            str = str + ''.join(key)
            dict[key] = 1
    return str

print(getString(repeat_string))
