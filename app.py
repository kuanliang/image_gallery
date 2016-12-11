import os
from flask import Flask, render_template, request, send_from_directory

__author__ = 'kuan-liang liu'



app = Flask(__name__, static_folder='images')


APP_ROOT = os.path.dirname(os.path.abspath(__file__))


# test.com/uploads
@app.route('/')
def index():
    return render_template("upload.html")


@app.route('/upload', methods=['POST'])
def upload():
    target = os.path.join(APP_ROOT, "images")
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for upload in request.files.getlist("file"):
        print(upload)
        filename = upload.filename
        destination = "/".join([target, filename])
        print("Accept incoming file:", filename)
        print("Save it to:", destination)
        upload.save(destination)

    return render_template("complete.html", image_name=filename)


@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)

@app.route('/gallery')
def get_gallery():
    
    image_names = os.listdir("./images")

    return render_template("gallery.html", image_names=image_names)

    
if __name__ == '__main__':
    app.run(port=4555, debug=True)