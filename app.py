import random
from flask import Flask, render_template, request
from recommender import random_recommender, MOVIES

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('home.html')

#@app.route('/')
# def recommender():
    # top_two = random_recommender()
    # return f'{top_two}'  
    
# @app.route('/results')
# def recommender():
#     print(request.args)
#     return f'Here are some recommended movies: {random_recommender()}'

@app.route('/results')
def recommender():
    user_query = request.args.to_dict()
    user_query = {key:int(value) for key,value in user_query.items()}
    top_two = random_recommender()
    return render_template('results.html', movies = top_two)


if __name__ == '__main__':
    app.run(port=5002, debug=True)


# expand brower by that:
# ?t=ffab&q=in+the+mouth+of+madness&ia=web

