def seperate_list(names_list):
    # even and odd list are initially empty
    even_list = []
    odd_list = []
    # iterate through list names_list
    for i in names_list:
        # if length is even
        if len(i) % 2 == 0:
            # add name to even list
            even_list.append(i)
        # if length is even
        else:
            # add name to odd list
            odd_list.append(i)
    # iterate though length of even list
    for j in range(len(even_list)):
        # First character is replaced with 'b' 
        even_list[j] = 'b' + even_list[j][1:]
    # iterate though length of odd list
    for k in range(len(odd_list)):
        # Last character is replaced with 'a #c'
        odd_list[k] = odd_list[k][:-1] + 'a #c'
    # print even and odd list 
    print("Even list = ", even_list)
    print("Odd list = ", odd_list)
    # return even list
    return even_list

names_list = ["bob","jimmy","max b", "bernie", "jordan", "future hendrix"]
print(seperate_list(names_list))
