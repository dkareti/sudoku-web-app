from flask import Flask, render_template, request, session, redirect, url_for
from sudoku import generate_full_grid, remove_numbers
import os
import json

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        difficulty = request.form["difficulty"]
        solution = generate_full_grid()
        puzzle = remove_numbers(solution, difficulty)
        session["solution"] = json.dumps(solution)
        session["puzzle"] = json.dumps(puzzle)
        return render_template("puzzle.html", puzzle=puzzle)
    return render_template("index.html")


@app.route("/check", methods=["POST"])
def check():
    # Load the solution from the session
    if "solution" not in session:
        return redirect(url_for("home"))

    solution = json.loads(session["solution"])
    correct = True

    for i in range(9):
        for j in range(9):
            key = f"cell-{i}-{j}"
            val = request.form.get(key)
            sol_val = solution[i][j]
            if sol_val != 0:  # Skip if the original value was blank
                if not val or int(val) != sol_val:
                    correct = False

    message = "✅ Correct! Well done!" if correct else "❌ Incorrect. Try again!"
    return f"<h1>{message}</h1><a href='/'>Play Again</a>"
if __name__ == "__main__":
    app.run(port=5001)