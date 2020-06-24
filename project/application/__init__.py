from flask import Flask, flash, render_template, request, redirect, url_for
import logging 
import boto3
from botocore.client import Config
from botocore.exceptions import ClientError
import requests
from werkzeug.utils import secure_filename

app =Flask(__name__)



@app.route("/", methods= ["GET","POST"])
def index():
    return render_template("index.html")



@app.route("/home", methods= ["GET","POST"])
def home():
    #download s3 client in the right configuration
    s3_client = boto3.client('s3', region_name="eu-west-2", config=Config(signature_version='s3v4'))
    bucket_name= 'image-rekog-lambda-1922'
    
    #Getting the file which is sent from the index.html page
    if "user_file" not in request.files:
        flash("No user_file key in request.files")
    #user_file is the name of the file input on our form
    file    = request.files["user_file"]
    """
        These attributes are also available

        file.filename               # The actual name of the file
        file.content_type
        file.content_length
        file.mimetype
    """
    if file.filename == "":
        flash("Please select a file")
    if file:
        
        #sanitizing the filename
        file.filename= secure_filename(file.filename)
        
        #Generate presigned URL for uploading
        try:
            response = s3_client.generate_presigned_post(bucket_name, file.filename, Fields=None, Conditions=None, ExpiresIn=3600)

        except ClientError as e:
            logging.error(e)
            return None
        
        if response is None:
            exit(1)
        #requests function expects the file with 2 variables. will throw an error if not compressed like this
        files= {'file':(file.filename, file)}

        #Use presigned Url to upload the file
        http_response = requests.post(response['url'], data=response['fields'], files=files)
        return '{} Uploaded'.format(file.filename)
    #if one of the tests fail we redirect the user to the homepage
    else:
        return redirect("/")



    




