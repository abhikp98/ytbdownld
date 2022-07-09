from flask import Flask, request
from pytube import YouTube

app = Flask(__name__)


@app.route('/test')
def val():
    link = str(request.args.get('link'))
    ab = set()
    for res in YouTube(link).streams.filter(type="video"):
        ab.add(res.resolution)
    ab = (sorted(ab))
    print(type(ab))
    return {"res": ab}


if __name__ == "__main__":
    app.run(debug=True)
