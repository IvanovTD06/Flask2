@app.errorhandler(HTTPException)
def handle_exception(e):
    return jsonify({"message": e.description}), e.code