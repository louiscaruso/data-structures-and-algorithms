open_list = ["[", "{", "("]
close_list = ["]", "}", ")"]

def bracket_type(bracketStr):
    stack = []
    for x in bracketStr:
        if x in open_list:
            stack.append(x)

        elif x in close_list:
            post = close_list.index(x)
            if ((len(stack)> 0) and (open_list[post] == stack[len(stack)- 1])):
                stack.pop
        
            else: 
                return False
    if len(stack) == 0:
        return True
    else:
        return True


        
# https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-python/#:~:text=One%20approach%20to%20check%20balanced,%2C%20return%20Balanced%20otherwise%2C%20Unbalanced.


# value_string = "{}"
# print(value_string,"-", bracket_type(value_string))
# value_string = "{}(){}"
# print(value_string,"-", bracket_type(value_string))
# value_string = "[({}]"
# print(value_string,"-", bracket_type(value_string))
# value_string = "(]("
# print(value_string,"-", bracket_type(value_string))

# if __main__ == "__main__":
#  print()











# if __name__ == "__main__":