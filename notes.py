import pickle
import os


def add_note(command: str):
    tags = []
    body = ""
    for word in command.split(" ")[1:]:
        if word.startswith("#"):
            tags.append(word)
        else:
            body += word + " "
    note = [tags, body]
    notes.append(note)
    save_to_file()


def load_from_file():
    filename = "notes.bin"
    with open (filename, "rb") as file:
        notes = pickle.load(file)
    return notes


def print_notes(notes: list):
    for note in notes:
        num = notes.index(note)+1
        tags = ', '.join(tag for tag in note[0])
        body = note[1]
        print("{:^5} {:<40} {:<60}".format(num, tags, body))


def remove(num: int):
    notes.pop(num-1)
    save_to_file()


def edit(num: int, text: str):
    tags = []
    body = ""
    for word in text.split(" "):
        if word.startswith("#"):
            tags.append(word)
        else:
            body += word + " "
    note = [tags, body]
    notes[num-1] = note
    save_to_file()
    

def save_to_file():
    filename = "notes.bin"
    with open (filename, "wb") as file:
        pickle.dump(notes, file)


# def main():
#     while True:
#         pass

notes = []


if __name__ == "__main__":
    # main()
    stat = os.stat("notes.bin")
    size = stat.st_size
    if size > 0:
        notes = load_from_file()
    else:
        notes = []


    add_note("add #test_1 #test_2 test note 1 for first note in notebook")
    # add_note("add #test_3 #test_4 some other note to test the work and design")
    # add_note("add #test_5 #test_6 #test_7 i have no idea what to write here but i have to write something")
    # add_note("add #test_5 #test_6 #test_7 i have no idea what to write here but i have to write something")

    # remove(4)
    # edit(2, "#test_3_1 #test_4_1 edited note ")

    print_notes(notes)
