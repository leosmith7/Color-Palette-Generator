import numpy as np
from PIL import Image
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for flash messages

@app.route('/', methods=["POST", "GET"])
def extract():
    if request.method == 'POST':
        file = request.files.get('image')
        if file:
            try:
                img = Image.open(file)
                img = img.resize((100, 100))
                img = img.convert('RGB')
                img_array = np.array(img)
                pixels = img_array.reshape(-1, 3)
                unique_colors, counts = np.unique(pixels, axis=0, return_counts=True)
                color_counts = list(zip(counts, unique_colors.tolist()))
                color_counts.sort(reverse=True, key=lambda x: x[0])
                flash('File uploaded successfully!', 'success')
                return render_template('index.html', colors=color_counts[:10])
            except:
                flash('Error processing the image. Please try again.', 'danger')
                return render_template('index.html')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)