from django.shortcuts import render,redirect #for rendering htmls
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.forms import inlineformset_factory
from .models import *

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


def home(request):
    
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
                import torch
                from torchvision import transforms
                import warnings
                import cv2
                from torch import nn
                from torch.autograd import Variable
                from torchvision import models
                import time
                from PIL import Image
                warnings.filterwarnings("ignore")

                # create a dataset transformer
                transformer_input = transforms.Compose(transforms=[

                    transforms.Grayscale(num_output_channels=3),
                    transforms.Resize((256, 256)),
                    transforms.ToTensor(),
                    transforms.Normalize((0.3,), (0.2,))])

                """load image, returns tensor"""
                image = Image.open(os.path.join(BASE_DIR,'images/'+image_name))
                image = transformer_input(image).float()
                image = Variable(image, requires_grad=True)

                # load the saved model
                loaded_model = models.resnet18()
                num_ftrs = loaded_model.fc.in_features
                loaded_model.fc = nn.Linear(num_ftrs, 3)
                loaded_model = torch.load(os.path.join(BASE_DIR,'Model/covid19_model.pth'), map_location='cpu')
                loaded_model.eval()

                output_single = loaded_model(image.view(1, 3, 256, 256))
                output_single_proba = torch.exp(output_single)
                output_sigle_proba_array = output_single_proba.detach().numpy().ravel()
                proba_user, predict_single = output_single_proba.topk(1, dim=1)

                # labels dictionary
                labels_dict = {'covid': 0, 'normal': 1, 'pneumonia': 2}
                prediction = ''
                for class_name, class_code in labels_dict.items():  # for name, age in dictionary.iteritems():  (for Python 2.x)
                    if class_code == predict_single.item():
                        prediction = class_name

                context = {'uploadform': uploadform,'prediction':prediction}
                return render(request,'pages/home.html',context=context)

            else:
                upladform = UploadImage()

                format_message="Unsupported format, supported format are .png and .jpg ";

                return render(request,'pages/home.html',{'fmsg':format_message,'uploadform':upladform})

        else:
            return render(request,template_name="pages/home.html",context=context)

    return render(request,template_name="pages/home.html",context=context)
