import os 
from datetime import datetime

def get_entries():
    entries = [f for f in os.listdir() if f.endswith(".txt")]
    return entries


def create_entry():
    entry = input("Write your journal entry: Press 'Enter' when done\n")
    title = input("Name your journal entry\n")

    if not title:
        title = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    filename = f"{title}.txt"

    # Create file
    with open(filename, "w") as file:
        file.write(entry)
    print(f"Journal Entry '{title}' saved successfully. \n")

def read_entry():
    
    entries = get_entries()

    if not entries:
        print("No journal entries")
        return

    for idx, entry in enumerate(entries, 1):
        print(f"{idx}. {entry}")
    choice =  int(input("Select journal entry to view: ")) - 1
    
    if 0 <= choice < len(entries):
        with open(entries[choice], "r") as file:
            print(file.read())
    pass

def delete_entry():
    entries = get_entries()
     # Lists all text files
    if not entries:
        print("No entries to delete.\n")
        return

    # Prints entries to display
    for idx, entry in enumerate(entries, 1):
        print(f"{idx}. {entry}")

    # Based on User choice it will delete the chosen entry
    choice = int(input("Select entry to delete: ")) - 1
    if 0 <= choice < len(entries):
        os.remove(entries[choice])
        print(f"Entry '{entries[choice]}' deleted.\n")
    else:
        print("Invalid choice.\n")
    pass

def update_entry():
    # Lists all text files
    entries = get_entries()

    # Lets user know if there aren't any entries
    if not entries:
        print("No journal entries to edit.\n")
        return

    # Shows the User a list of Journal Entries with Numbers for selection
    for idx, entry in enumerate(entries, 1):
        print(f"{idx}. {entry}")

    # User chooses with a number what journal entry they want to edit
    choice = int(input("Select journal entry to edit: ")) - 1

    # If the user chooses a valid journal entry
    if 0 <= choice < len(entries):
        # Open inputed journal entry
        with open(entries[choice], "r") as file:
            content = file.read()
        print(f"Current content:\n{content}\n")

        # Gets the user to input a new entry and rewrite over the previous entry
        new_content = input("Enter new content: (Press 'Enter' to submit)\n")
        with open(entries[choice], "w") as file:
            file.write(new_content)

        print(f"Entry '{entries[choice]}' updated.\n")
    else:
        print("Invalid choice.\n")
    pass

def main():
    print("Journal App")
    while True:
        print(
                "Menu:\n1. Write New Entry\n2. Read Entries\n3. Update Entry\n4. Delete Entry\n"
                )
        choice = input("Choose and action(1-5)")
        if choice == '1':
            create_entry()
        elif choice == '2':
            read_entry()
        elif choice == '3':
            update_entry()
        elif choice == '4':
            delete_entry()
        else: 
            print("done")

if __name__ == "__main__":
    main()
