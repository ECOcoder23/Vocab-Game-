path_to_file = "/workspaces/Vocab-Game-/"
file = "vocab.txt"
while True:
    prompt_1 = "Application closed, Goodbye"
    menu_options = input("1 - Create new friend record\n2 - Search for a friend\n3 - Run reports\n4 - Exit\n-> ")
    numeric = int(menu_options)
    if numeric == 2: 
        load = open(path_to_file + file, "r")
        for line in load:
            print(f"Data found: {line}")
    elif numeric == 4:
        record = open(path_to_file + file, "wt")
        record.write(prompt_1)
        record.close()
        print(prompt_1)
        break 

class Thing:

    def __init__(self, does_exist, is_real):
        self.does_exist = does_exist
        self.is_real = is_real

