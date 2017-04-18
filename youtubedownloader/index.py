from flask import Flask, render_template, request, redirect, url_for
from pytube import YouTube
import os

app = Flask(__name__)

@app.route('/')
def index():
	filename = request.args.get('filename')
	resolutions0 = request.args.get('resolutions0')
	resolutions1 = request.args.get('resolutions1')
	url = request.args.get('url')
	
	return render_template('index.html', filename=filename, resolutions0=resolutions0, resolutions1=resolutions1, url=url)

@app.route('/done')
def done():
	filename = request.args.get('filename')
	return render_template('done.html', filename=filename)

@app.route('/backindex', methods=['POST'])
def backinde():
	return render_template('index.html')


@app.route('/sumbit', methods=['POST'])
def post_sumbit():
	yt = YouTube()
	url = request.form.get('url')
	yt.url = url
	video = yt.get('mp4', '360p')
	filename = yt.filename

	if os.path.exists(filename+".mp4"):
		os.remove(filename+".mp4")
	
	#video.download('./')

	#print(len(yt.videos))

	#for i in range(0,len(yt.videos)):
	#	print(resolutions[i])

	resolutions = yt.filter('mp4')

	#print (len(resolutions))

	#print(yt.filter('mp4')[-1])

	#print (resolutions)
	#resolutions0 = str(resolutions[0])
	#resolutions1 = str(resolutions[1])
	#resolutions2 = str(yt.videos[2])
	
	#print (resolutions0)
	#print (resolutions1)
	#print (resolutions2)
	


	#print (yt)
	#print (filename)
	#a = yt.get_videos()
	#print (type(a))

	#return redirect(url_for('index', filename=filename))

	if len(resolutions) == 2:
		resolutions0 = str(resolutions[0])
		resolutions1 = str(resolutions[1])
		return redirect(url_for('index',url=url, filename=filename, resolutions0=resolutions0, resolutions1=resolutions1))
	else:
		resolutions0 = str(resolutions[0])
		return redirect(url_for('index',url=url, filename=filename, resolutions0=resolutions0))

@app.route('/download', methods=['POST'])
def post_download():
	yt = YouTube()
	url = request.form.get('url')
	yt.url = url
	video = yt.get('mp4', '360p')
	filename = yt.filename

	if os.path.exists(filename+".mp4"):
		os.remove(filename+".mp4")
	
	video.download('./')

	return redirect(url_for('done', filename=filename))

if __name__ == '__main__':
	app.run(port=9000,debug=True)