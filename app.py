from flask import Flask, render_template, request
from sudoku import generate_full_grid, remove_numbers

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        difficulty = request.form["difficulty"]
        solution = generate_full_grid()
        puzzle = remove_numbers(solution, difficulty)
        return render_template("puzzle.html", puzzle=puzzle)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)