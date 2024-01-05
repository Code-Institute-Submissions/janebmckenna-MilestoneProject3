import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import date
from werkzeug.security import (
    generate_password_hash, check_password_hash)

if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

@app.route("/")
@app.route("/blog_posts")
def blog_posts():
    blogs = list(mongo.db.blogs.find())
    return render_template("blogs.html", blogs=blogs)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get('query')
    blogs = list(mongo.db.blogs.find({"$text": {"$search":query}}))
    return render_template("blogs.html", blogs=blogs)


@app.route("/search_profile", methods=["GET", "POST"])
def search_profile():
    query = request.form.get('query')
    blogs = list(mongo.db.blogs.find({"$text": {"$search":query}}))
    username =mongo.db.users.find_one(
    {"username": session["user"]})["username"]
    return render_template("profile.html", blogs=blogs, username=username)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        # check if email already exists
        existing_email = mongo.db.users.find_one(
        {"email": request.form.get("email").lower()})

        if existing_email:
            flash("Email already in use")
            return redirect(url_for("register"))

        password = request.form.get("password")
        confirm = request.form.get("confirm")
        
        # checks to see if the passwords match before registering the user
        if password == confirm:
            register = {
                "email": request.form.get("email").lower(),
                "username": request.form.get("username").lower(),
                "password": generate_password_hash(request.form.get("password")),
                "is_admin": "No"
            }
            mongo.db.users.insert_one(register)

            # put the new user into 'session' cookie
            session['user'] = request.form.get("username").lower()
            flash("Registration successful!")
            return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session users username from the database
    username =mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    blogs = list(mongo.db.blogs.find())

    if session["user"]:
        return render_template("profile.html", username=username, blogs=blogs)

    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in DB
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            print(existing_user)
            for key, val in existing_user.items():
                if key == "is_admin":
                    admin = val
                    print(admin)
            # ensure passwords match
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # passwords dont match
                flash ("Incorrect username and/or password")
                return redirect(url_for("login"))

        else:
            # username doesnt exist
            flash ("Incorrect username and/or password")
            return redirect(url_for("login"))
    return render_template("login.html")


@app.route("/logout")
def logout():
    # remove user from session cookies
    flash ("You have been logged out")
    session.pop('user')
    return redirect(url_for("login"))


@app.route("/new_blog", methods=["GET", "POST"])
def new_blog():
    # gets current date
    today = date.today().strftime('%d %b %Y')
    print(today)
    if request.method == "POST":
        blog = {
            "category_name": request.form.get("category_name"),
            "title": request.form.get("title"),
            "blog_content": request.form.get("blog_content"),
            "date": today,
            "user": session["user"]
        }
        mongo.db.blogs.insert_one(blog)
        flash("Thank you, blog successfully added")
        return redirect(url_for("blog_posts"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("new_blog.html", categories = categories)


@app.route("/edit/<blog_id>", methods=["GET", "POST"])
def edit(blog_id):
    # gets current date
    today = date.today().strftime('%d %b %Y')
    print(today)
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "title": request.form.get("title"),
            "blog_content": request.form.get("blog_content"),
            "date": today,
            "user": session["user"],
            "updated": "yes"
        }
        mongo.db.blogs.update_one({"_id": ObjectId(blog_id)}, {"$set": submit})
        flash("Thank you, blog successfully updated")
        return redirect(url_for("blog_posts"))

    blog = mongo.db.blogs.find_one({"_id": ObjectId(blog_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit.html", blog=blog, categories = categories)


@app.route("/delete/<blog_id>")
def delete(blog_id):
    mongo.db.blogs.delete_one({"_id": ObjectId(blog_id)})
    flash("Blog succesfully deleted")
    return redirect(url_for("blog_posts"))


@app.route("/categories")
def categories():
    categories = list(mongo.db.categories.find().sort("category_name",1))
    return render_template("categories.html", categories=categories)


@app.route("/new_category", methods=["GET", "POST"])
def new_category():
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("New Category Added")
        return redirect(url_for("categories"))

    return render_template("new_category.html")


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.update_one({"_id": ObjectId(category_id)}, {"$set": submit})
        flash("Category Successfully Updated")
        return redirect(url_for('categories'))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)



@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.delete_one({"_id": ObjectId(category_id)})
    flash("Category succesfully deleted")
    return redirect(url_for("categories"))
  


# NOTE TO SELF: UPDATE TO DEBUG=False prior to submitting
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), 
        port =int(os.environ.get("PORT")),
        debug=True)
