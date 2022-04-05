from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
all_posts = json.loads(response.text)
print(all_posts)

@app.route('/')
def home():
    response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
    all_posts = json.loads(response.text)
    print(all_posts)
    return render_template("index.html", posts=all_posts)

@app.route('/post/<num>')
def get_post(num):
    print(num)
    return render_template("post.html", posts=all_posts, post=all_posts[int(num)-1])

if __name__ == "__main__":
    app.run(debug=True)
