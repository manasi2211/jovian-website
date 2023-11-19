from flask import Flask

#creating flask app
app = Flask(__name__)

#registered an route 
@app.route("/")
def hello_worl():
  return "hello, world"

#checking if we are running as python script
if __name__ == "__main__":
  app.run(host="0.0.0.0",debug=True)