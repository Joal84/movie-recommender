from flask import Flask, render_template, request
from recommender import get_recommendation, get_movie_data


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():

    return render_template("index.html")


@app.route("/recommendation", methods=["GET", "POST"])
def recommender():

    if request.method == "POST":
        movie_ratings = {}
        for i in range(1, 6):
            movie_name = request.form.get(f"movie{i}")
            rating = request.form.get(f"rating{i}")
            movie_ratings[movie_name] = rating

    new_user = get_recommendation(movie_ratings)
    movie_data = get_movie_data(new_user.index)

    return render_template("/recommender.html",  data=movie_data.items())

print(__name__)
if __name__ == "__main__":
    app.run(debug=True, port=5000)
