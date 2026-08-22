"""A minimal Flask web app exposing the calculator over HTTP."""

from flask import Flask, jsonify, request

from app.calculator import add, divide


def create_app() -> Flask:
    app = Flask(__name__)

    @app.get("/health")
    def health():
        return jsonify(status="ok")

    @app.get("/add")
    def add_route():
        a = request.args.get("a", type=float)
        b = request.args.get("b", type=float)
        if a is None or b is None:
            return jsonify(error="pass numeric ?a= and ?b="), 400
        return jsonify(result=add(a, b))

    @app.get("/divide")
    def divide_route():
        a = request.args.get("a", type=float)
        b = request.args.get("b", type=float)
        if a is None or b is None:
            return jsonify(error="pass numeric ?a= and ?b="), 400
        try:
            return jsonify(result=divide(a, b))
        except ValueError as exc:
            return jsonify(error=str(exc)), 400

    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
