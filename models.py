import json


class LibraryBook:
  def __init__(self):
    try:
      with open("librarybook.json", "r") as f:
        self.librarybook = json.load(f)
    except FileNotFoundError:
      self.librarybook = []

  def all(self):
    return self.librarybook

  def get(self, id):
    # return self.library[id]
    book = [book for book in self.all() if book['id'] == id]
    if book:
      return book[0]
    return []

  def create(self, data):
    self.librarybook.append(data)
    self.save_all()

  def delete(self, id):
    book = self.get(id)
    if book:
      self.librarybook.remove(book)
      self.save_all()
      return True
    return False  

  def save_all(self):
    with open("librarybook.json", "w") as f:
      json.dump(self.librarybook, f)

  def update(self, id, data):
    book = self.get(id)
    if book:
      index = self.librarybook.index(book)
      self.librarybook[index] = data
      self.save_all()
      return True
    return False
  
librarybook = LibraryBook()