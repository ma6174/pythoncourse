# wfp 6/18
# wfp, updated names, 10/11
# phone book

phonebook_dict = {}

def add_pair():
    name,number= input("Add who (: separated pair): ").split(":")
    name = name.strip()
    number = number.strip()
    phonebook_dict[name]=number
    print("Added ",name," to the book with number: ",number)

def delete_pair():
    name = input("Remove who: ").strip()
    if name in phonebook_dict:
        print("Removed ",name," from the book with number: ",phonebook_dict[name])
        phonebook_dict.pop(name)
    else:
        print("Sorry, ",name," isn't in the book")

def lookup():
    name = input("Look up who: ").strip()
    if name in phonebook_dict:
        print("For ",name," the number is: ",phonebook_dict[name])
    else:
        print("Sorry, ",name," isn't in the book")   

def init_from_file():
    fileName = input("Initialize from what file: ").strip()
    fileH = open(fileName,"r")
    for line in fileH:
        name,number = line.strip().split()
        phonebook_dict[name]=number

def print_book():
    print("Our present phone book contains:")
    for name,number in phonebook_dict.items():
        print("{:10s} : {:s}".format(name,number))
        
def main():
    print("Welcome to the phone book program")
    print("Possible commands are:")
    print("{:10s} : {:s}".format("init","fill the phonebook with numbers from a file"))
    print("{:10s} : {:s}".format("lookup","lookup a number in the phonebook"))
    print("{:10s} : {:s}".format("add","add an entry to the phonebook"))
    print("{:10s} : {:s}".format("del","delete an entry from the phonebook"))
    print("{:10s} : {:s}".format("print","print the entire phonebook"))
    print("{:10s} : {:s}".format("quit","quit the program"))
    print
    command_dict={"init":init_from_file,"lookup":lookup,"add":add_pair,"del":delete_pair,"print":print_book}
    response_str = ""
    while response_str != "quit":
        response_str = input("Please give a command: ")
        if response_str in command_dict:
            command_dict[response_str]()
        elif response_str!="quit" :
            print("Bad command, try again")
    print()
    print("Thanks for playing")
    
        
