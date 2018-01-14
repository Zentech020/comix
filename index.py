from flask import Flask, render_template, request,send_file
app = Flask(__name__)
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import textwrap
import uuid

@app.route('/')
def student():
   return render_template('student.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():

   if request.method == 'POST':
      x = uuid.uuid4()
      one = request.form['one']
      two = request.form['two']
      three = request.form['three']


      img = Image.open("comix.png")
      draw = ImageDraw.Draw(img)
      font = ImageFont.truetype('/Library/Fonts/comic_font.ttf', 20)
      text = textwrap.fill(one,width=30)
      text2 = textwrap.fill(two,width=32)
      text3 = textwrap.fill(three,width=10)



      draw.text((38,34),text,(0,0,0),font=font)
      draw.text((260,16),text2,(0,0,0),font=font)
      draw.text((496,45),text3,(0,0,0),font=font)

      img_file = "/Users/zennobruinsma/Desktop/MachineLearning/github_ml/python_comics/upload/%s.png" %(x)
      print(img_file)
      img.save(img_file)

      return render_template('result.html',id = x)

@app.route('/download/<pid>',methods = ['POST', 'GET'])
def download(pid):
	try:
		return send_file('/Users/zennobruinsma/Desktop/MachineLearning/github_ml/python_comics/upload/'+pid+'.png', attachment_filename=pid+'.jpg')
	except Exception as e:
		return str(e)


if __name__ == '__main__':
   app.run(debug = True)
