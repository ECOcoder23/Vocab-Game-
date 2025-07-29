path_to_file = "/workspaces/Vocab-Game-"
file = "vocab.txt"
while True:
    menu_options = input("1 - Create new friend record\n2 - Search for a friend\n3 - Run reports\n4 - Exit\n: ")
    numeric = int(menu_options)
    if numeric == 4:
        prompt_1 = "Application closed, Goodbye"
        with open(path_to_file + file, "wt") as record:
            record.write(prompt_1)
        print("Application closed, Goodbye")
        break 