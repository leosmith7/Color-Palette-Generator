import flask, numpy as np
from PIL import Image
from flask import Flask, jsonify, render_template, request, redirect, url_for, flash


app = flask.Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def extract():
    if request.method == 'POST':
        file = request.files['image']

        if file:
            img = Image.open(file)
            img = img.resize((100, 100))
            img_array = np.array(img)

            #process

            return render_template('index.html', colors=img_array)  #

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)






