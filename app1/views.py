from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import About, Title,Contact,Faculties,Other,News,Events,Faculty_Detail,Student_detail,Academy,Gallery,carousel
from django.contrib.auth.models import User, auth


import requests

from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.decorators.csrf import csrf_exempt
import random

from .PayTm import Checksum


MERCHANT_KEY = 'bKMfNxPPf_QdZppa'



# Create your views here.
def index(request):
    title=Title.objects.all()
    fac=Faculties.objects.all()
    hist=About.objects.all()
    other=Other.objects.all()
    news=News.objects.all()
    events=Events.objects.all()
    aca=Academy.objects.all()
    car=carousel.objects.all()
    contact(request)
    return render(request, "index.html",{'title':title,'fac':fac,'hist':hist,'other':other,'news':news,'events':events,'aca':aca,'car':car})

def gallery(request):
    gal=Gallery.objects.all()
    return render(request,'gallery.html',{'gal':gal})
    


def contact(request):
    if request.method == 'POST':
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        number=request.POST.get('number','')
        message=request.POST.get('message','')
        contact=Contact(name=name,email=email,phone=number,message=message)
        contact.save()
        messages.info(request,'Detail sand')
    



def fac_Dashboard(request):
    
    return render(request,"fac_Dashboard.html",{'user':request.user})


def faculty(request):
    if request.method == 'POST':
        username =request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username, password=password)
        if user.is_staff:
            auth.login(request, user)
            return redirect("/fac_Dashboard")
        else:
            messages.info(request,'Invalid credentials')
            return render(request, 'faculty.html')
    else:
        return render(request, 'faculty.html')


def fac_reg(request):
    if request.method =='POST':
        name =request.POST['name']
        username =request.POST['username']
        password1 = request.POST['password1']
        password2 =request.POST['password2']
        email= request.POST['email']
        #aadhar = request.POST['aadhar']
        phone = request.POST['phone']
        #address = request.POST['address']
        #img= request.POST['img']
        
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'User name already exists')
                return redirect('fac_reg')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already exists')
                return redirect('fac_reg')

            else:
                user=User.objects.create_user(username=username,password=password1,email=email)
                user.is_staff=True
                user.save()
                reg=Faculty_Detail(user=user,phone=phone,name=name,)
                reg.save()
                msg=f'CPA Bakhira..\n Congratulation! You have successfully rgisterd \n username:{username}\n password:{password1}\n\n\n ThankYou!'
                url = "https://www.fast2sms.com/dev/bulk"
                payload = f"sender_id=FSTSMS&message={msg}&language=english&route=p&numbers={phone}"
                headers = {
                'authorization': "FXBN1L7qZclnhgtIxfTOrVSQpiesubyEUD9d8jYHaW5JCP6M0wu5crlOzbBUJXs2DvoQa0Pq63VCLGnd",
                'Content-Type': "application/x-www-form-urlencoded",
                'Cache-Control': "no-cache",
                }
                response = requests.request("POST", url, data=payload, headers=headers)
                print(response.text)
                
                print("Created ")
                messages.info(request,'Registration Successfully')
                return fac_Dashboard(request)
        else:
            messages.info(request,'Incorrect confirm password')
            return redirect('fac_reg')
            
    else:
         return render(request, 'fac_reg.html')


def stu_reg(request):
    if request.method =='POST':
        name =request.POST['name']
        username =request.POST['username']
        password1 = request.POST['password1']
        password2 =request.POST['password2']
        email=request.POST['email']
        phone = request.POST['phone']
        
        
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'User name already exists')
                return redirect('stu_reg')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already exists')
                return redirect('fac_reg')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email)
                user.save()
                reg=Student_detail(user=user,phone=phone,name=name,)
                reg.save()
                msg=f'CPA Bakhira..\n Congratulation! You have successfully rgisterd \n username:{username}\n password:{password1}\n\n\n ThankYou!'
                url = "https://www.fast2sms.com/dev/bulk"
                payload = f"sender_id=FSTSMS&message={msg}&language=english&route=p&numbers={phone}"
                headers = {
                'authorization': "FXBN1L7qZclnhgtIxfTOrVSQpiesubyEUD9d8jYHaW5JCP6M0wu5crlOzbBUJXs2DvoQa0Pq63VCLGnd",
                'Content-Type': "application/x-www-form-urlencoded",
                'Cache-Control': "no-cache",
                }
                response = requests.request("POST", url, data=payload, headers=headers)
                print(response.text)
                
                print("Created ")
                messages.info(request,'Registraion Successfully')
                
                return redirect("https://cpabakhira.pythonanywhere.com/admin/app1/student_detail/")
               
                

        else:
            messages.info(request,'Incorrect confirm password')
            return redirect('stu_reg')
            
    else:
         return render(request, 'stu_reg.html')


def stu_Dashboard(request):
    aca= Academy.objects.all()
    return render(request,"stu_dashboard.html",{"user":request.user,'aca':aca})

def edit_profile(request):
    context={}
    data=Faculty_Detail.objects.get(user_id=request.user.id)
    context['data']=data
    if request.method=='POST':
        name =request.POST['name']
        aadhar = request.POST['aadhar']
        phone = request.POST['phone']
        address = request.POST['address']
        img= request.POST['img']
        father= request.POST['father']
        data.name=name
        data.phone=phone
        data.aadhar=aadhar
        data.img=img
        data.father=father
        data.address=address
        data.save()
        messages.info(request,'successfully profile edited')
        return redirect("/fac_Dashboard")
    else:
        
        return render(request, 'edit_profile.html',{'user':request.user})

def student(request):
    if request.method == 'POST':
        username =request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username, password=password)
        if not user.is_staff:
              
                
            auth.login(request, user)
            return redirect("/stu_Dashboard")
            
        else:
            messages.info(request,'Invalid credentials')
            return render(request, 'student.html')
    else:
        return render(request, 'student.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


def render_pdf_view(request):
    
    template_path = 'print.html'
    context = {'user':request.user}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def checkout(request):
    
    if request.method=="POST":
        
        name = request.POST.get('name', '')
        amount = request.POST.get('amount', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '')
        state = request.POST.get('state', '')
        phone = request.POST.get('phone', '')
        
        #data.fee_status=amount
        #data.save()
        #return render(request, 'checkout.html', {'thank':thank, 'id': id})
        order_id=random.randint(5000,100000)
        param_dict = {

            'MID': 'DIY12386817555501617',
            'ORDER_ID': str(order_id),
            'TXN_AMOUNT': str(amount),
            'CUST_ID': email,
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL':'http://127.0.0.1:8000/payment/handlerequest',
        }
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)

    
        return  render(request, 'paytm.html', {'param_dict': param_dict})
    return render(request, 'checkout.html')


@csrf_exempt 
def handlerequest(request):
    # paytm will send you post request here
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
            return fee_status(request)
            
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
    return render(request, 'paymentstatus.html', {'response': response_dict})

def fee_status(request):
    context={}
    check=Student_detail.objects.filter(user_id=request.user.id)
    print(check)
    data=Student_detail.objects.get(user_id=request.user.id)
    context['data']=data
    data.fee_status=handlerequest.response_dict
    data.save()

