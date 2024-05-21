from blog.app import app
from flask import Flask, json, request
import logging
import git



app = Flask(__name__)


@app.route('/update_server', methods=['POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo('mysite')
        origin = repo.remotes.origin
        origin.pull()
        return "Updates PythonAnywhere successfully", 200
    else:
        return "Wrong ever tipe", 400


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        debug=True,
    )
