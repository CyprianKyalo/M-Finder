from flask import Flask, render_template, Response, flash, request, redirect, url_for, session, jsonify
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
# from flask_mysqldb import MySQL
from datetime import datetime

from tensorflow.keras.models import load_model
from model import SiameseModel
from utils import verify_predict, extract_face
from location import get_location

import cv2
import os
# import MySQLdb
import re

import psycopg2

model_path = "./my_encoder"
model = load_model(model_path, custom_objects={"SiameseModel": SiameseModel})

UPLOAD_FOLDER = 'static/uploads/'
 
app = Flask(__name__)

app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'mfinder'
# app.config['TESTING'] = True
# app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PASSWORD'] = ''
# app.config['MYSQL_DATABASE_DB'] = 'm_finder'
# app.config['MYSQL_DATABASE_HOST'] = 'localhost'

# mysql = MySQL(app)
# # mysql.init_app(app)
# with app.app_context():
#     cur = mysql.connection.cursor()


conn = psycopg2.connect(dbname="m_finder", user="postgres", password="root", host="localhost")
cursor = conn.cursor()

global capture, switch
capture = 0
switch = 1

FILE_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

video = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# def loadModel():
#     global model
#     model = load_model(model_path, custom_objects={"SiameseModel": SiameseModel})
#     print("The model has loaded")

def get_connection():
    try:
        db_connection = MySQLdb.connect("localhost", 'root', '', 'm_finder')
    except Exception as e:
        print("Can't connect to the database")
        return 0

    return db_connection

def close_connection(db_connection):
    db_connection.close()


@app.route("/registration")
def registration():
    return render_template("registration.html")

@app.route("/register_post", methods=['POST'])
def register_post():
    message = ""
    if request.method == "POST" and 'name' in request.form and 'password' in request.form and 'email' in request.form:
        name = request.form['name']
        password = request.form['password']
        email = request.form['email']
        location = request.form['location']
        contact = request.form['contact']

        # cursor = mysql.connection.cursor()
        try:
            cursor.execute("SELECT * FROM users WHERE email = %s", (email, ))
            account = cursor.fetchone()
        except:
            conn.rollback()

        if account:
            message = "The account already exists! Please log in."
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            message = "Invalid email address!!"
        elif not name or not email or not password:
            message = "Please fill in the whole form!!"
        else:
            query = "INSERT INTO users (name, location, contact, email, password) VALUES (%s, %s, %s, %s, %s)"
            values = (name, location, contact, email, generate_password_hash(password))

            cursor.execute(query, values)
            # Commit the changes to the database
            cursor.execute("COMMIT")
            # cursor.execute('INSERT INTO users VALUES (NULL, % s, % s, % s, % s, % s)', (name, location, contact, email, generate_password_hash(password), ))
            # mysql.connection.commit()
            # cursor.close()
            print(values)
            message = "You have successfully registered! Please proceed to log in."
    elif request.method == "POST":
        message = "Please fill in the form!!"
    return render_template('registration.html', message=message)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/login_post", methods=['POST'])
def login_post():
    message = ""
    if request.method == "POST" and "email" in request.form and "password" in request.form:
        email = request.form['email']
        password = request.form['password']

        # cursor = mysql.connection.cursor()
        # try:
        #     query = 'SELECT * FROM users WHERE email = %s'
        #     value = (email)
        #     print("Vlue is ", query, value)
        #     print("Execution ", cursor.execute(query, value))
        #     user = cursor.fetchone()
        #     print("User is ", user)
        #     # user = cursor.execute('SELECT * FROM users WHERE email = %s', (email, )).fetchone()
        # except:
        #     message = "No user Exists"
        #     conn.rollback()
            # return render_template('login.html', message=message)
        try:
            cursor.execute("SELECT * FROM users WHERE email = %s", (email, ))
            user = cursor.fetchone()
        except:
            conn.rollback()

        if not user:
            message = "Wrong Email or Password! Kindly re-enter your credentials."
            
        elif not check_password_hash(user[5], password):
            message = "Wrong Password! Kindly re-enter your credentials."
        else:
            session['loggedin'] = True
            session['userID'] = user[0]
            session['name'] = user[1]
            session['email'] = user[4]
            message = 'You have successfully logged in!!'
            # cursor.close()
            return render_template("index.html", message=message)
            
        # flash(message)
        return render_template('login.html', message=message)


        # cursor.execute('SELECT * FROM user WHERE email = %s AND password = %s', (email, password, ))
        
        # user = cursor.fetchone()
        # if user:
        #     session['loggedin'] = True
        #     session['userID'] = user['userID']
        #     session['name'] = user['name']
        #     session['email'] = user['email']
        #     message = 'You have successfully logged in!!'
        #     return render_template("index.html", message=message)
        # else:
        #     message = "Wrong Email or Password! Kindly re-enter your credentials."
        # return render_template('login.html', message=message)
    else:
        message = "There was an error! Please Try again"
        return render_template('login.html', message=message)

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('userID', None)
    session.pop('email', None)
    session.clear()
    return redirect(url_for('login'))

@app.route("/upload_image")
def upload_form():
    return render_template("upload_image.html")

def allowed_image(image_name):
    return '.' in image_name and image_name.rsplit('.', 1)[1].lower() in FILE_EXTENSIONS

@app.route("/upload_image", methods=['POST'])
def upload_image():
    message = ''
    # loggedin = session["loggedin"]
    if "loggedin" not in session:
        flash("Please Login to upload an image")
        return redirect(request.url)

    if 'image' not in request.files:
        # message = "No image uploaded"
        flash("No image uploaded")
        return redirect(request.url)
    
    image = request.files['image']
    if image.filename == '':
        flash("No image selected for uploading")
        return redirect(request.url)

    if request.method == "POST" and image and allowed_image(image.filename) and 'name' in request.form:
        filename = secure_filename(image.filename)
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        userID = session['userID']
        name = request.form['name']
        time = request.form['last_seen_time']
        location = request.form['last_seen_location']
        age = request.form['age']
        description  = request.form['description']
        phone = request.form['phone']
        status = "Not Found"
        updated_at = datetime.now()

        print("Userid is", userID)

        query = "INSERT INTO images (userid, name, time, location, age, description, phone, filename, status, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        # "INSERT INTO users (name, location, contact, email, password) VALUES (%s, %s, %s, %s, %s)"
        values = (userID, name, time, location, age, description, phone, filename, status, updated_at)
        # cursor = mysql.connection.cursor()
        # cursor.execute('INSERT INTO images VALUES (NULL, % s, % s, % s, % s, % s, % s, % s, % s, % s, % s)', (userID, name, time, location, age, description, phone, filename, status, updated_at, ))
        # mysql.connection.commit()
        # cursor.close()
        cursor.execute(query, values)

        cursor.execute("COMMIT")

        flash("Image successfully uploaded")
        return render_template("upload_image.html", filename=filename)
    else:
        flash("File type not accepted - Please upload a png, jpg or jpeg")
        return redirect(request.url)

@app.route('/view_images')
def view_images():
    # path = "Path to Image storage"
    # path = "C:\\Users\\Cyprian\\Desktop\\IS Project\\M-Finder\\static\\uploads"
    # images = os.listdir(path)
    # return render_template("View_images.html", images=images)

    # cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM images')
    data = cursor.fetchall()
    # print(data)
    # cursor.close()
    return render_template("view_images.html", data=data)

@app.route("/livesearch", methods=["POST", "GET"])
def livesearch():
    if request.method == 'POST':
        print("Here pssing")
        search_word = request.form.get('query')
        print("Word is ", search_word)
        if search_word is None:
            query = "SELECT * from images"
            cursor.execute(query)
            data = cursor.fetchall()
        else:    
            query = "SELECT * from images WHERE name ILIKE '%{}%' OR phone ILIKE '%{}%' OR location ILIKE '%{}%'".format(search_word,search_word,search_word)
            cursor.execute(query)
            print("Query is ", query)
            data = cursor.fetchall()
            print("Data is ", data)
    return jsonify({'htmlresponse': render_template('response.html', data=data)})


@app.route("/video_url")
def video_url():
    return render_template("video.html")

@app.route('/requests', methods=['POST', 'GET'])
def tasks():
    global switch, video
    if request.form.get('click') == 'Capture':
        global capture
        capture = 1
    elif request.form.get('stop') == 'Stop/Start':
        if (switch == 1):
            switch = 0
            video.release()
            cv2.destroyAllWindows()
        else:
            video = cv2.VideoCapture(0)
            switch = 1


    return render_template("video.html")

# @app.route("/video")
def gen(video):
    global capture
    while True:
        success, image = video.read()

        if success:
            if(capture):
                capture = 0
                # cv2.imwrite("my_taken_image.jpg", image)
                idx = verify_predict(model)
                print("The index is ", idx)
                if idx:
                    update_images_table(idx)
                    print("Image Updated")
                else:
                    print("Image not found")

        try:
            frame_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            frame_gray = cv2.equalizeHist(frame_gray)

            faces = face_cascade.detectMultiScale(frame_gray)

            for (x, y, w, h) in faces:
                center = (x + w//2, y + h//2)
                cv2.putText(image, "X: " + str(center[0]) + " Y: " + str(center[1]), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
                image = cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

                cv2.imwrite("my_taken_image.jpg", image)
                # cv2.imwrite("my_image.jpg", image)

                faceROI = frame_gray[y:y+h, x:x+w]
            ret, jpeg = cv2.imencode('.jpg', image)

            frame = jpeg.tobytes()
        
        # if cv2.waitKey(1) & 0xFF == ord('v'):
        #     print("Saving Image")
        #     cv2.imwrite(os.path.join('static', 'imgs', 'input_image.jpg'), image)
        #     print("The index is ", verify_predict(model))


        # if cv2.waitKey(1) & 0xFF == ord('v'):
        #     print("Saving Image")
        #     cv2.imwrite(os.path.join('static', 'imgs', 'input_image.jpg'), image)

        #     print("The index is ", verify_predict(model))
        
        # try:
            # ret, jpg = cv2.imencode(".jpg", image)
            # frame = jpg.tobytes()

            yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

        except Exception as e:
            print("The exception is ", e)

@app.route('/video_feed')
def video_feed():
    global video
    return Response(gen(video),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

def update_images_table(index):
    img_name = os.listdir(UPLOAD_FOLDER)[index]

    cursor.execute("SELECT * FROM images WHERE filename = 'my_image1.jpg'")
    img = cursor.fetchone()


    if img and img[9] == "Not Found":
        # print("Passed through here")
        location_data = get_location()
        try:
            # Start a database transaction
            cursor.execute('START TRANSACTION')

            query = "INSERT INTO location (city, region, country, latitude, longitude) VALUES (%s, %s, %s, %s, %s) RETURNING locationid"
            values = (location_data['city'], location_data['region'], location_data['country'], location_data['latitude'], location_data['longitude'])

            # print("Values are ", values)

            cursor.execute(query, values)

            # print("It did pass honestly")

            # Retrieve the primary key value for the new row
            cursor.execute("SELECT lastval()")
            new_id = cursor.fetchone()[0]

            # print("The new id is ", new_id)

            cursor.execute("Update images SET temp_status = %s, updated_at = %s, locationid = %s WHERE filename = %s", (1, datetime.now(), new_id, img_name, ))
            
            cursor.execute("COMMIT")

            print("Success!!!")
        except:
            print("There was error")
            conn.rollback()
        return "Temporary Status updated successfully"
    else:
        cur.close()
        return "Image Not Found"


@app.route('/found')
def found():
    cursor.execute('SELECT * FROM images WHERE EXTRACT(WEEK FROM updated_at) = EXTRACT(WEEK FROM current_timestamp) AND temp_status = 1;')
    data = cursor.fetchall()
    return render_template('found.html', data=data)


@app.route('/map')
def map():
    return render_template('map.html')


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    # loadModel()
    app.run(debug=True)
