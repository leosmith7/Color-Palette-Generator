import numpy as np
from PIL import Image
from flask import Flask, jsonify, render_template, request, redirect, url_for, flash

app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def extract():
    if request.method == 'POST':
        file = request.files.get('image')
        print(file)

        if file:
            img = Image.open(file)
            img = img.resize((100, 100))

            img = img.convert('RGB')

            img_array = np.array(img)

            pixels = img_array.reshape(-1, 3)

            unique_colors, counts = np.unique(pixels, axis=0, return_counts=True)

            color_counts = list(zip(counts, unique_colors.tolist()))

            color_counts.sort(reverse=True, key=lambda x: x[0])

            print("Most Common Colors:")
            for count, color in color_counts[:10]:
                print(f"Color: {color}, Count: {count}")

            return render_template('index.html', colors=color_counts[:10])

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
