# length of the string using recursive approach
def length(str):
    if str=='':
        return 0
    else:
        return 1+length(str[1:])
def main():
    str=input("Enter the string")
    length_str=length(str)
    print("Length of the string",str,"is",length_str)
if __name__=='__main__':
    main()
