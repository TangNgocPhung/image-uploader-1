from django.shortcuts import render, redirect
from .models import Image, File
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
# Create your views here.
from django.http import FileResponse

def home(request):
  img = Image.objects.all()
  file = File.objects.all()
  return render(request, 'myapp/home.html', {'img':img, 'file' : file})

def AddImage(request):
  print(request.method == "POST")
  if request.method == 'POST':
    FileImage = request.FILES['file']
    
    print('FileImage',FileImage)
    fss = FileSystemStorage(location = settings.MEDIA_ROOT+'\myimage')
    print('MEDIA_root',settings.MEDIA_ROOT + '\myimage')
    
    print('fss', fss)
    print('fss.url',fss.url)
    print('FileImage.name', FileImage.name)
    print("FileImage", FileImage)
    
    saveimg = fss.save(FileImage.name, FileImage)
    print('saveimg', saveimg)
    print("photo", fss.url(saveimg))
    img = Image()
    img.photo = './media/myimage/' + saveimg
    img.save()
    return redirect('myapp:home')
  return redirect('myapp:home')

def AddFile(request):
  if request.method == 'POST':
        uploaded_file = request.FILES['file_path']
        file_path = './media/file/' + uploaded_file.name
        print("file_path",file_path)
        # Save the file to the desired location using the file_path
        with open(file_path, 'wb') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)
        file = File()
        file.file = file_path
        file.save()
        # Other processing or redirection logic
        return redirect('myapp:home')
  return redirect('myapp:home')
            
def DeleteImage(request, idphoto):
  img = Image.objects.get(id=idphoto)
  print("img", img.photo)
  print(os.path.exists(img.photo))
  if os.path.exists(img.photo):
    os.remove(img.photo)
    img.delete()
    return redirect('myapp:home')
  return redirect('myapp:home')

def downloadFile(request, file_id):
  file = File.objects.get(id=file_id)
  full_path = os.path.abspath(file.file)
  if not os.path.exists(full_path):
    return HttpResponse("File not found", status = 404)
  file_name = os.path.basename(full_path)
  
  response = FileResponse(open(full_path, 'rb'),as_attachment = True)
  response['Content-Disposition'] = f'attachment; filename="{file_name}"'
  return response
