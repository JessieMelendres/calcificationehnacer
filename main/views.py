from django.shortcuts import render
from .models import Files

def index(response):
    if response.method =='POST':
        files=response.FILES.getlist('files')
        file_list=[]
        for file in files:
            new_file=Files(
                file=file
            )
            new_file.save()
            file_list.append(new_file.file.url)

        return render(response, "main/index.html", {'new_urls':file_list})
    else:
        return render(response, 'main/index.html')
