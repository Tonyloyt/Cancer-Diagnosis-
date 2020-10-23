from django.shortcuts import render,redirect #for rendering htmls
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.forms import inlineformset_factory
from .models import *
from . import views
from .forms import *

from .forms import UploadImage
from .forms import SavePatientDetails
from .models import PatientDetails
from .models import Insert
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages



# Create your views here.
# def index(request):
#     return HttpResponse("Hello world. You're at the Elixir_app")
# BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
def elixir_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('elixir_dashboard')
        else:
            messages.info(request,'Username OR Password is incorrect')


        #  context={'form':form}
    return render(request,'elixir_app/elixir_login.html')

def logoutUser(request):
    logout(request)
    return redirect('elixir_login')

    
def elixir_dashboard(request):
    patient_form = SavePatientDetails()
    if request.method == 'POST':
        patient_form = SavePatientDetails(request.POST)
        if patient_form.is_valid():
            patient_form.save()
        

    context = {'patient_form': patient_form}
    return render(request, 'elixir_app/elixir_dashboard.html', context)
    
    #
""" Model uploading class below"""


BASE_DIR = os.path.dirname(os.path.dirname(os.path.relpath(__file__)))

def PredictImage(request):

    uploadform = UploadImage()

    context = {'uploadform': uploadform}

    if request.method == 'POST' and request.FILES['filename']:

        uploadform = UploadImage(request.POST,request.FILES)

        if uploadform.is_valid():

            file_path = request.FILES['filename']

            image_name = file_path.name

            image_name = str(image_name)

            if image_name.endswith(".jpg") or image_name.endswith(".png"):

                new_file = Insert(filepaths=file_path, filename=image_name)

                new_file.save()

                # import all import libraries
                import os
                import cv2
                import numpy as np 
                import pandas as pd
                import tensorflow as tf
                from tensorflow import keras
                from PIL import Image
                from keras.preprocessing.image import load_img
                from keras.preprocessing.image import img_to_array

                #covert image into greyscale
                # load the image
                img = load_img(new_file)
                 

                # convert to numpy array
            
                # img = cv2.imread(new_file)
                # image_array = Image.fromarray(img, 'RGB')
                image_array = img_to_array(img)
                # resize_img = image_array.resize((50 , 50))
                # resize_img = np.array(resize_img).reshape(1,50,50,3)/255.

                #try to load the Model
                loaded_model = keras.models.load_model('/Model/saved_model.h5')
                print(loaded_model)

                #predictions
                prediction = loaded_model.predict(image_array)
                index = np.argmax(prediction)

                # labels dictionary
                labels_dict = {'Normal': 0, 'Cancer': 1}
                predictions = ''
                for class_name, class_code in labels_dict.items():  # for name, age in dictionary.iteritems():  (for Python 2.x)
                    if class_code == index.item():
                        predictions = class_name

                context = {'uploadform': uploadform,'prediction':predictions}
                return render(request,'elixir_app/elixir_dashboard.html',context=context)

            else:
                upladform = UploadImage()

                format_message="Unsupported format, supported format are .png and .jpg "

                return render(request,'elixir_app/elixir_dashboard.html',{'fmsg':format_message,'uploadform':upladform})

        else:
            return render(request,template_name="elixir_app/elixir_dashboard.html",context=context)

    return render(request,template_name="elixir_app/elixir_dashboard.html",context=context)
