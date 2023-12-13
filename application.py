from bottle import route, post, run, template, redirect, request

import database

@route("/")
def get_index():
    return template("home.tpl")
# -------------------------------Rental List----------------------------------------
@route("/rental-list")
def get_list():
    items = database.get_items()
    return template("rental_record/rental_list.tpl", rental_list=items)

@route("/add-rental")
def get_add():
    items = database.get_movies()
    return template("rental_record/add_rental_item.tpl", movies_list=items)

@post("/add-rental")
def post_add():
    fName = request.forms.get("fName")
    lName = request.forms.get("lName")
    movie_title = request.forms.get("movie_title")
    date_borrow = request.forms.get("date_borrow")
    due_date = request.forms.get("due_date")
    item={
        "fName":fName,
        "lName": lName,
        "movie_title": movie_title,
        "date_borrow": date_borrow,
        "due_date": due_date
    }
    database.add_item(item)
    redirect("/rental-list")

@route("/delete-rental/<id>")
def get_delete(id):
    database.delete_item(id)
    redirect("/rental-list")

@route("/update-rental/<id>")
def get_update(id):
    items = database.get_items(id)
    movies_list = database.get_movies()
    if len(items) != 1:
        redirect("/rental-list")
    fName = items[0]['fName']
    lName = items[0]['lName']
    movie_title = items[0]['movie_title']
    date_borrow = items[0]['date_borrow']
    due_date = items[0]['due_date']
    return template("rental_record/update_rental_item.tpl", id=id, fName=fName,lName=lName, movie_title=movie_title, date_borrow=date_borrow, due_date=due_date, movies_list=movies_list)

@post("/update-rental")
def post_update():
     
    lName = request.forms.get("lName")
    movie_title = request.forms.get("movie_title")
    date_borrow = request.forms.get("date_borrow")
    due_date = request.forms.get("due_date")
    id = request.forms.get("id")
    database.update_item(id, fName, lName, movie_title, date_borrow, due_date)
    redirect("/rental-list")
# -------------------------Movies list--------------------------------------
@route("/movies-list")
def get_movies_list():
    items = database.get_movies()
    return template("movies_list/movies_list.tpl", movies_list=items)

@route("/add-movie")
def get_add_movie():
    return template("movies_list/add_movie_item.tpl")

@post("/add-movie")
def post_add_movie():
    title = request.forms.get("title")
    genre = request.forms.get("genre")
    year = request.forms.get("year")
    rated = request.forms.get("rated")
    runtime = request.forms.get("runtime")
    item={
        "title": title,
        "genre": genre,
        "year": year,
        "rated": rated,
        "runtime": runtime
    }
    database.add_movie(item)
    redirect("/movies-list")

@route("/delete-movie/<id>")
def get_delete_movie(id):
    database.delete_movie(id)
    redirect("/movies-list")

@route("/update-movie/<id>")
def get_update_movie(id):
    items = database.get_movies(id)
    if len(items) != 1:
        redirect("/movies-list")
    title = items[0]['title']
    genre = items[0]['genre']
    year = items[0]['year']
    rated = items[0]['rated']
    runtime = items[0]['runtime']
    return template("movies_list/update_movie_item.tpl", id=id, title= title, genre = genre, year = year, rated = rated, runtime = runtime)

@post("/update-movie")
def post_update_movie():
    title = request.forms.get("title")
    genre = request.forms.get("genre")
    year = request.forms.get("year")
    rated = request.forms.get("rated")
    runtime = request.forms.get("runtime")
    id = request.forms.get("id")
    database.update_movie(id,title,genre,year,rated,runtime)
    redirect("/movies-list")

run(host='localhost', port=8080)