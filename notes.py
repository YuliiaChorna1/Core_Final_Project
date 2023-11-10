#Зміни (Настя):
    # теги зберігає в список, замість словнику
    # файл для збереження змінено з .plk на  .bin  та тимчасово змынено назву на test_notes
    # додано def __str__ для виводу нотаток
    # змінено формат виводу на таблицю
    # відкореговано def _parse_tags та додано def _parse_text з тим, 
            # щоб теги не дублювалися в текст нотатки
    # додано remove, edit


import re
from collections import UserList
import pickle


class Note:
    def __init__(self, title: str, text:str)  -> None:
        self._title = title
        self._text = self._parse_text(text)
        self._tags = []
        self._parse_tags(text)

    def __str__(self) -> str:
        num = notes_list.index(note)+1
        tags = ', '.join(tag for tag in note._tags)
        
        return ("{:<5} {:<20} {:<20} {:<50}".format(num, note.title, tags, note.text))

    @property
    def title(self):
        return self._title

    @property
    def text(self):
        return self._text

    @property
    def tags_dict(self):
        return self._tags

    def _parse_tags(self, text: str) -> None:
        # Регулярний вираз для пошуку хештегів в тексті
        pattern = r"#\w+"
        tags = re.findall(pattern, text)

        for tag in tags:
            tag = tag[1:]  # Видаляємо символ "#" з тегу
            self._tags.append(tag)

    def _parse_text(self, text: str) -> str:
        return " ".join(word for word in text.split() if not word.startswith("#")) 

    @text.setter
    def text(self, new_text: str) -> None:
        self._text = new_text
        self._parse_tags()

class NotesList(UserList):
    def __init__(self) -> None:
        super().__init__()
        self.filename = "notes.bin"  # Назва файлу для збереження нотаток

        # Перевизначення методу append для автоматичного збереження при додаванні нотаток
    def append(self, note: Note) -> None:
        super().append(note)
        self._save_notes_to_file()


    def remove(self, num: int) -> None:
        notes_list.pop(num-1)
        self._save_notes_to_file()


    def edit(self, num: int, title: str, text: str):
    
        note = Note(title, text)
        notes_list[num-1] = note
        self._save_notes_to_file()

        # Збереження нотаток у файл
    def _save_notes_to_file(self)-> None:
        with open(self.filename, 'wb') as file:
            pickle.dump(self.data, file)

        # Завантаження нотаток з файлу
    def load_notes_from_file(self) -> None:
        try:
            with open(self.filename, 'rb') as file:
                self.data = pickle.load(file)
        except (FileNotFoundError, EOFError):
            self.data = []

    # Код для збереження та завантаження нотаток
notes_list = NotesList()
notes_list.load_notes_from_file()

# note1 = Note("Title 1", "Text of Note 1 #tag1 #tag2")
# note2 = Note("Title 2", "Text of Note 2 #tag2 #tag3")
# notes_list.append(note1)  # Автоматичне збереження при додаванні
# notes_list.append(note2)
# notes_list.remove(1)     # видалення нотатки за номером
notes_list.edit(3, "Title 3", "Text of Note 3 #tag3 #tag4")

# Виведення нотаток
print("{:^5} {:<20} {:<20} {:<50}".format("num", "title", "tags", "text"))
for note in notes_list:
    print(note)