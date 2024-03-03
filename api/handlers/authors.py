def validate(in_data: dict, method="post") -> dict:
    rating = in_data.setdefault("rating", 1)
    if rating not in range(1, 6) and method == "post":
        in_data["rating"] = 1
    elif rating not in range(1, 6) and method == "put":
        in_data.pop("rating")
    in_data.setdefault("text", "text")
    return in_data


@app.route("/authors", methods=["GET", "POST"])
def handle_authors():
    if request.method == "GET":
        authors = AuthorModel.query.all()
        authors_dict = []
        for author in authors:
            authors_dict.append(author.to_dict())
        return jsonify(authors_dict), 200 
      
    if request.method == "POST":
        author_data = request.json
        author = AuthorModel(author_data.get("name", "Ivan"))
        db.session.add(author)
        try:
            db.session.commit()
            return jsonify(author.to_dict()), 201
        except:       
            abort(400, "UNIQUE constraint failed")


@app.get("/authors/<int:author_id>")
def get_author(author_id):
    author = AuthorModel.query.get(author_id)
    if author:
        return jsonify(author.to_dict()), 200
    abort(404, f"Author with id = {author_id} not found")


# GET на url: /authors/<int:id>/quotes      # получить все цитаты автора с quote_id = <int:quote_id>
@app.get("/authors/<int:author_id>/quotes")
def get_quote_by_author(author_id):
    quotes_lst = db.session.query(QuoteModel).filter_by(author_id=author_id)   
    quotes_lst_dct = []
    for quote in quotes_lst:
        quotes_lst_dct.append(quote.to_dict())
    return jsonify(quotes_lst_dct), 200


@app.put("/authors/<int:author_id>")
def edit_author(author_id):
    new_data = request.json
    author = AuthorModel.query.get(author_id)
    if not author:
        abort(404, f"Author with id = {author_id} not found")

    # Универсальный случай
    for key, value in new_data.items():
        setattr(author, key, value)
    try:
        db.session.commit()
        return jsonify(author.to_dict()), 200
    except:
        abort(400, f"Database commit operation failed.")


@app.delete("/authors/<int:author_id>")
def delete_author(author_id):
    author = AuthorModel.query.get(author_id)
    if not author:
        abort(404, f"Author with id = {author_id} not found")
    db.session.delete(author)
    try:
        db.session.commit()
        return jsonify(message=f"Author with id={author_id} deleted successfully"), 200
    except:
        abort(400, f"Database commit operation failed.")


@app.route("/authors/<int:author_id>/quotes", methods=["POST"])
def create_quote_to_author(author_id):
    """ function to create new quote to author"""
    author = AuthorModel.query.get(author_id)
    data = request.json
    # Валидация данных
    data = validate(data)

    # После валидации создаем новую цитату
    new_quote = QuoteModel(author, **data)
    db.session.add(new_quote)
    try:
        db.session.commit()
        return new_quote.to_dict(), 201
    except:
        abort(400, f"Database commit operation failed.")