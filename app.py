from flask import Flask
import urllib2
import sys


githubUrl = str(sys.argv[1])
githubUrl = githubUrl.replace('github.com','raw.github.com') + '/master/'
print 'Github Url:'+ githubUrl
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello from Dockerized Flask App!!"


@app.route("/v1/<fileName>")
def github1(fileName):
    response = urllib2.urlopen(githubUrl + fileName)
    html = response.read()
    return html


@app.route("/v2/")
def github2():
    return "Hello github2"

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
