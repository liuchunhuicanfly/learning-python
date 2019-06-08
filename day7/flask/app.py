# encoding: utf8

import os
import uuid
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import csv


UPLOAD_FOLDER = 'static/Uploads'
ALLOWED_EXTENSIONS = set(['csv', 'xls', 'xlsx'])
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# 判断文件夹是否存在，如果不存在则创建
if not os.path.exists(UPLOAD_FOLDER):
	os.mkdir(os.path.join(UPLOAD_FOLDER))

# 判断文件后缀是否在列表中
def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def read_csv(path):
	with open(path, encoding = 'utf-8') as text:
		rows = csv.reader(text, delimiter=',')
		for r in rows:
			print(r)
	# header = rows[0].split('\t')
	# data = [[float(x) for x in y.split('\t') if len(x) >= 1] for y in rows[1:] if len(y) >= 1]
	# print(header)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/api/upload', methods = ['GET', 'POST'])
def upload_file():
	if request.method == 'POST':

		if 'file' not in request.files:
			flash('No file part')
			return 'No file part'
		file = request.files['file']

		if file.filename == '':
			flash('No selected file')
			return 'No selected file'

		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			filename = str(uuid.uuid4()) + '.' + filename.rsplit('.', 1)[1]
			path = os.path.join(UPLOAD_FOLDER, filename)
			file.save(path)
			# print(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			read_csv(path)
			return '上传成功'

	return render_template('index.html')

if __name__ == '__main__':
	app.run()