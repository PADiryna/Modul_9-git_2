from flask import Flask, jsonify, abort, make_response, request
                         
from forms import LibraryBookForm
from models import librarybook

app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"

@app.route("/api/v1/librarybook/", methods=["GET"])
def librarybook_list_api_vi():
  return jsonify(librarybook.all())


@app.route("/api/v1/librarybook/<int:book_id>/", methods=["GET"])
def get_book(book_id):
  book = librarybook.get(book_id)
  if not book:
    abort(404)
  return jsonify({"book": book})

@app.errorhandler(404)
def not_found(error):
  return make_response(jsonify({'error': 'Not found', 'status_code': 404}), 404)

@app.route("/api/v1/librarybook/", methods=["POST"])
def create_book():
  if not request.json or not 'title' in request.json:
    abort(400)
  book = {
    'id': librarybook.all()[-1]['id'] + 1,
    'title': request.json['title'],
    'ganre': request.json['ganre'],
    'author': request.json['autor'],
    'date': request.json['date'],
    'description': request.json.get('description', "")
  }
  librarybook.create(book)
  return jsonify({'book': book}), 201

@app.errorhandler(400)
def bad_request(error):
  return make_response(jsonify({'error': 'Bad request', 'status_code': 400}), 400)

@app.route("/api/v1/librarybook/<int:book_id>", methods=['DELETE'])
def delete_book(book_id):
  result = librarybook.delete(book_id)
  if not result:
    abort(404)
  return jsonify({'result': result})

@app.route("/api/v1/librarybook/<int:book_id>", methods=["PUT"])
def update_book(book_id):
  book = librarybook.get(book_id)
  if not book:
    abort(404)
  if not request.json:
    abort(400)
  data = request.json
  if any([
    'title' in data and not isinstance(data.get('title'), str),
    'ganre' in data and not isinstance(data.get('ganre'), str),
    'author' in data and not isinstance(data.get('author'), str),
    'date' in data and not isinstance(data.get('date'), str), 
    'description' in data and not isinstance(data.get('description'), str)
  ]):
    abort(400)
  book = {
    'title': data.get('title', book['title']),
    'ganre': data.get('ganre', book['ganre']),
    'author': data.get('author', book['author']),
    'date': data.get('date', book['date']),
    'description': data.get('description',book['description'])
  }
  librarybook.update(book_id, book)
  return jsonify({'book': book})

if __name__ == "__main__":
  app.run(debug=True)
  