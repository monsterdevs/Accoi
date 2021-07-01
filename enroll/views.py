from django.shortcuts import render
from enroll import logs
from django.http import HttpResponse
# from .forms import StudentRegistration
from .forms import UserForm

# Create your views here.
# def showformdata(request):
#     fm=StudentRegistration()
#     return render(request,'enroll/userregistration.html',{'form':fm})

def showformdetails(request):
    # fm1=UserForm()
    # return render(request,'enroll/recordtracker.html',{'form':fm1})
    return render(request,'enroll/index.html')

def analyze(request):
    # Get the text
    djtext=request.POST.get('text','default')


    purpose=""
    params={'ip':'198.18.118.213','reqId':}
    return render(request, 'analyze.html', params)





# Check checkbox values
    # DDC_AccessLogs=request.POST.get('DDC_AccessLogs','off')
    # Cache_Logs=request.POST.get('Cache_Logs','off')
    # Header_Logs=request.POST.get('Header_Logs','off')
    # Metadata_Trace=request.POST.get('Metadata_Trace','off')

















# from django.http import HttpResponseRedirect
# from django.shortcuts import render,redirect
# from .models import Whizz_Home, Active
#
#
# def home(request):
# ActiveIP = []
# ActiveRunData ={}
# ActiveRunData['ActiveData'] = Whizz_Home.objects.exclude(Status='Completed')
# for data in ActiveRunData['ActiveData']:
# print(data.id)
# return render(request, 'home.html', ActiveRunData)
#
#
# def progress(request):
# if request.GET:
# contextnew = {}
# GetData = request.GET
# object_id = GetData.get('ID')
# for data in Whizz_Home.objects.all():
# if data.id == int(object_id):
# contextnew = {
# 'Status': data.Status,
# 'EmailId': data.EmailId,
# 'Flag': data.Flag,
# 'Ip':data.IP
# }
# break
# return render(request,'progresspage.html',contextnew)
# else:
# PostData = request.POST
# IP = PostData.get('IP')
# EmailId = PostData.get('EmailId')
#
# # check for IP validation!:ask anupam bhaiya for all the valid ips
# HomeData = Whizz_Home(IP=IP, EmailId=EmailId)
# HomeData.save()
# Flag = GhostInfo.CheckFlag(IP) #getting flags from server
# HomeData.Flag = Flag
# if Flag == '0':
# #print('hi')
# HomeData.Status = "Completed"
# ActiveData = Active(First_Flag=Flag, Current_Flag=Flag, Status=HomeData.Status)
# ActiveData.save()
# else:
# HomeData.Status = "Running"
# HomeData.save()
# # [TODO]
# GetData = Whizz_Home.objects.all().last()
# context = {
# 'Flag': GetData.Flag,
# 'EmailId': GetData.EmailId,
# 'Ip': GetData.IP,
# 'Status': GetData.Status
# }
# print(context)
# if GetData.Flag == 0:
# return render(request, 'successpage.html', context)
# else:
# return render(request, 'progresspage.html', context)


# def success(request):
# return HttpResponse('Success!!')




