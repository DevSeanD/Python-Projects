print("Hello this application is designed to keep a To-Do list")
print(" it will allow you to continually add new items just press enter")
print("  * To quit enter \" :wq \" * ")

count = 1                 # the counter for the print out

while 1 < 2:              # this condition will always be true

    print(count, ")")     # print out for displaying counter
    my_list = input()     # allows for the continued input
    print("\n")
    int(count)            # turns the counter back into and integer value so it can be incremented
    count += 1
    if my_list == ":wq":  # if the user enters :wq (write and quit) then end then break the while loop
        break
