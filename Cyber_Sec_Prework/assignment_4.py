names_list = ["bob", "jimmy", "max b", "bernie", "jordan", "future hendrix"]

max_len = -1
for name in names_list:
    if len(name) > max_len:
        max_len = len(name)
        resulted_name = name
print(resulted_name)
