#This program sorts a list in order from
#least to greatest

#define the main
def main():
    # user_list = list(input("Enter numbers to sort (no spaces): "))

    #to test
    user_list = [0,1,4, 45, 76, 23,65,98,12,76,433,2,5,34,455,1,23,45,78,9,65]
  

    #print results
    print(sort_list(user_list))



#define the sort_list function
def sort_list(user_list):

    #define the variables used to keep the loops running
    is_switch = 'yes'
    index = 0
    count = 0

    #begin the first loop
    for number in range(len(user_list) - 1):
       # while is_switch == 'yes':
            while index < len(user_list) - 1:
                count+=1
                if user_list[index + 1] < user_list[index]:
                    switch(user_list, index)
                index += 1
            index = 0
        
    print(f"Count: {count}")
    return user_list
   # print(user_list)


#define the switch function; it works.
def switch(user_list,index):
    prev_item = user_list[index]
    user_list[index] = user_list[index + 1]
    user_list[index + 1] = prev_item
    return user_list


#run sort list to test
main()

#run the main
#main()








