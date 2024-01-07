from flask import Flask, render_template, request, redirect, url_for
import imdb

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
movie_access = imdb.Cinemagoer()

@app.route('/', methods=['GET', 'POST'])
def home():
  if request.method == "POST":
    search = request.form["search"]

    if request.form['submit_btn'] == "movie":   
      return redirect(url_for('search', name=search))
    elif request.form['submit_btn'] == 'series':
      return redirect(url_for('series', name=search))

  return render_template('home.html')

 
@app.route('/search',methods=['POST','GET'])
def search():
  if request.method == "POST":
    search = request.form["search"]
    
    if request.form['submit_btn'] == "movie":   
      return redirect(url_for('search', name=search))
    elif request.form['submit_btn'] == 'series':
      return redirect(url_for('series', name=search))
  
  try:
    name = request.args['name']
    results = movie_access.search_movie(name)
    movies = []

    for i in range(5):
      id = results[i].movieID
      movies.append("https://multiembed.mov/directstream.php?video_id=tt" + str(id))
      
    
    return render_template('search.html',results=movies,search=name)
  except:
    return redirect('/')

@app.route('/series',methods=['POST','GET'])
def series():
  if request.method == "POST":
    search = request.form["search"]

    if request.form['submit_btn'] == "movie":   
      return redirect(url_for('search', name=search))
    elif request.form['submit_btn'] == 'series':
      return redirect(url_for('series', name=search))

  try:
    name = request.args['name']
    results = movie_access.search_movie(name)
    series = []

    for i in range(5):
      id = results[i].movieID
      series.append("https://vidsrc.xyz/embed/tv/tt" + str(id))


    return render_template('search.html',results=series,search=name)
  except:
    return redirect('/')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=81, debug=True)
