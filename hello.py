from flask import Flask
app = Flask(_name)

@app.route('/')
def hello_world():
    return 'Hello World'

if __name__== "_main_":
    app.run()