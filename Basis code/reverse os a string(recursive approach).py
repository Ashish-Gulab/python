#reverse of a string using recursive approach
def reverse(str):
    if str=='':
        return str
    else:
        return str[-1]+reverse(str[:-1])
def main():
    str=input("Enter the string")
    string_reverse=reverse(str)
    print("Reverse of string",str,"is",string_reverse)
if __name__=='__main__':
    main()
