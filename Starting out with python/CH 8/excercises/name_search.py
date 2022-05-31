#This program reads the girls and boys
#names files into two lists. It then tells the user ifm the name they
#entered is among the names

def main():
    #read the contents of the girls file
    infile = open('GirlNames.txt','r')
    girls_names = infile.readlines()
    infile.close()

    #strip the newline
    index = 0
    while index < len(girls_names):
        girls_names[index] = girls_names[index].rstrip('\n')
        index += 1

    #read the contents of the boys file
    infile = open('BoyNames.txt','r')
    boys_names = infile.readlines()
    infile.close()

    #strip the newline
    index = 0
    while index < len(boys_names):
        boys_names[index] = boys_names[index].rstrip('\n')
        index += 1
    
    #get the names from the user
    girl_name = str(input('enter a girl name to search:'))
    boy_name = str(input('enter a boy name to search:'))

    #search them in the list
    girlname = 0
    boyname = 0
    for item in girls_names:
        if item == girl_name :
            girlname = 'yes'
            print(f'The name {girl_name} is among the most popular!')
    
            
    for item in boys_names:
        if item == boy_name :
            boyname = 'yes'
            print(f'The name {boy_name} is among the most popular!')
            
    if girlname != 'yes':
        print(f'The name {girl_name}is not among the most popular')

    if boyname != 'yes':
        print(f'The name {boy_name} is not among the most popular')
    

#run the main
main()