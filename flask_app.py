from flask import Flask, render_template, request
from flask.ext.uploads import UploadSet, configure_uploads, IMAGES
import base64
from app import main
app = Flask(__name__)

photos = UploadSet('photos', IMAGES)
app.config['UPLOADED_PHOTOS_DEST'] = 'static/img'
configure_uploads(app, photos)
@app.route('/')
def lqs():
	s = "Hello World"
	print s

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'photo' in request.files:
        #filename = photos.save(base64.decodestring(request.files['photo']))
        return filename
	return render_template('upload.html')

if __name__ == "__main__":
	try:
		app.run(host='192.168.194.6',debug=False,port=9999)
	except:
		raise