from flask import Blueprint, request, render_template
from flaskblog.models import Post

main = Blueprint('main', __name__)


@main.route("/posts")
def home():
    page = request.args.get('page', 1, type=int)
    posts_list = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=3)
    return render_template('home.html', posts=posts_list)

@main.route("/")
@main.route("/home")
@main.route("/about")
def about():
    return render_template('about.html', title='About')