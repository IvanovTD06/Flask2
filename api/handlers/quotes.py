@app.route("/quotes")
def get_quotes():
    """ Сериализация: list[quotes] -> list[dict] -> str(JSON) """
    quotes_db = QuoteModel.query.all()
    quotes = []
    for quote_db in quotes_db:
        quotes.append(quote_db.to_dict())
    
    return jsonify(quotes), 200


@app.get("/quotes/<int:quote_id>")
def get_quote_by_id(quote_id):
    quote = QuoteModel.query.get(quote_id)
    if quote:
        return jsonify(quote.to_dict()), 200
    abort(404, f"Quote with id={quote_id} not found")


@app.post("/quotes")
def create_quote():
    data = request.json

    new_quote = QuoteModel(**data)

    db.session.add(new_quote)
    try:
        db.session.commit()
        return jsonify(new_quote.to_dict()), 200
    except:       
        abort(400, "NOT NULL constraint failed")



@app.delete("/quotes/<int:quote_id>")
def delete(quote_id):
    quote = db.session.get(QuoteModel, quote_id)
    if quote is not None:
        db.session.delete(quote)
        db.session.commit()
        return jsonify(message=f"Row with id={quote_id} deleted."), 200
    abort(404, f"Quote id = {quote_id} not found")


@app.put("/quotes/<int:quote_id>")
def edit_quote(quote_id):
    data = request.json
    quote = QuoteModel.query.get(quote_id)
    if not quote:
        abort(404, f"Quote id = {quote_id} not found")

    # Валидация данных
    data = validate(data, "put")
        
    # Универсальный случай
    for key, value in data.items():
        setattr(quote, key, value)

    try:
        db.session.commit()
        return jsonify(quote.to_dict()), 200
    except:
        abort(500)


@app.route("/quotes/filter")
def get_quotes_by_filter():
    kwargs = request.args

    # Универсальное решение  
    quotes_db = QuoteModel.query.filter_by(**kwargs).all()

    if quotes_db:
        quotes = []
        for quote in quotes_db:
            quotes.append(quote.to_dict())      
        return jsonify(quotes), 200
    return jsonify([]), 200