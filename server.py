from flask import Flask, render_template

app = Flask(__name__)
print(__name__)

@app.route("/<string:page_name>")
def my_home(page_name):
    return render_template(page_name)
