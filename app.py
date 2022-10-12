from flask import Flask, request
from pytube import YouTube

app = Flask(__name__)


@app.route('/test')
def val():
    link = str(request.args.get('link'))
    key, vall, = [], []
    ttl = YouTube(link).title
    for i in YouTube(link).streams.filter(type="video").order_by("resolution"):
        if i.resolution not in key:
            key.append(i.resolution)
            vall.append(i.url)
    for i in range(len(key)):
        ab.update({"quality": key[i]})
        ab.update({"link": vall[i]})
    return ab


if __name__ == "__main__":
    app.run(debug=True)
