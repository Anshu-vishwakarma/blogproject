from django.shortcuts import render
# from.models import product
from django.http import HttpResponse

# def addproduct(req):
#    if req.method=="GET": 
#       return render(req,"addpro.html")      
#    else:
#       ob=product()
#       ob.name=req.POST.get('name')
#       ob.size=req.POST.get('size')
#       if len(req.FILES)!=0:
#          ob.image=req.FILES['image']
#       ob.save()
#       return HttpResponse("done")

# def show(req):
#     rec=product.objects.all()
#     return render(req,'show.html',{'rec':rec})


from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
def login(request):
    from . models import BlogData
    blog=BlogData.objects.all().order_by('-id').values()
    search=request.POST.get("search")
    print(search)
    yourdata=BlogData.objects.filter(category=search).values()
    b=''
    c=''
    if yourdata.exists():
        b=yourdata
    else:
        c=2
    print(yourdata)
    return render(request,'index2.html',{"blog":blog,"yourdata":b,"c":c})
# def home(request):
#     return render(request,'home.html')
from django.shortcuts import render,redirect
from django.http import HttpResponse
@login_required
def home(req):
    from . models import BlogData
    blog=BlogData.objects.all().order_by('-id').values()
    print(blog)
    return render(req,"index.html",{"blog":blog})
def home2(req):
    from . models import BlogData
    blog=BlogData.objects.all().order_by('-id').values()
    print(blog)
    return render(req,"index.html",{"blog":blog})
def LogIn(req):  
    return render(req,"loginfile.html")
def SignUp(req):
    return render(req,"signupfile.html")
def Admin(req):
    from . models import Record
    from . models import BlogData
    data2=Record.objects.all()
    blogdata=BlogData.objects.all().order_by('-id')
    return render(req,"Admin.html" ,{"Record":data2,"blog":blogdata})
def Faculty(req):
    return render(req,"Faculty.html")
from cryptography.fernet import Fernet
import base64
import logging
import traceback
from django.conf import settings

def encrypt(pas): 
    try:       
        pas = str(pas)   
        cipher_pass = Fernet(settings.ENCRYPT_KEY)    
        encrypt_pass = cipher_pass.encrypt(pas.encode('ascii'))  
        encrypt_pass = base64.urlsafe_b64encode(encrypt_pass).decode("ascii")    
        return encrypt_pass  
    except Exception as e:    
        logging.getLogger("error_logger").error(traceback.format_exc())    
        return None
def decrypt(pas):  
    try:      
        pas = base64.urlsafe_b64decode(pas)    
        cipher_pass = Fernet(settings.ENCRYPT_KEY) 
        decod_pass = cipher_pass.decrypt(pas).decode("ascii")       
        return decod_pass  
    except Exception as e:    
        logging.getLogger("error_logger").error(traceback.format_exc())   
        return None
def checklogin(req):
    global email,role
    role=req.POST.get("role")
    print(role)
    if role=="User":
        from . models import Record
        from . models import BlogData
        Eemail=req.POST.get("email")
        Epassword=req.POST.get("password")
        data=Record.objects.all()
        data2=Record.objects.filter(email=Eemail).values()
        blogdata=BlogData.objects.all().order_by('-id')
        mypost=BlogData.objects.filter(email=req.POST.get("email")).order_by('-id')

        for i in data:
            print(decrypt(i.password))
            print(Eemail)
            if Epassword==decrypt(i.password) and Eemail==i.email and 'User'==i.role:
                return render(req,"Student.html",{"res":data2,"blog":blogdata,"mypost":mypost}) 
            elif Eemail==i.email and 'User'==i.role:
                msg='Wrong Password!!'
                return render(req,'loginfile.html',{"wrn":msg})
            elif Eemail==i.email and Epassword==decrypt(i.password):
                msg='Role Incorrect !!'
                return render(req,'loginfile.html',{"wrn":msg})
            

        
                #data=Record.objects.filter(role=role,email=email,decrypt(password)=Epassword).values()
        return redirect('/SignUp')    
    # elif role=="Faculty":
    #     email=req.POST.get("email")
    #     password=req.POST.get("password")
    #     from . models import Record
    #     data=Record.objects.filter(role=role,email=email,password=password).values()
    #     print(data)
    #     data2=Record.objects.filter(role=role,email=email).values()

    #     if data.exists():
    #         Record2=Record.objects.filter(role="Student").values()
    #         return render(req,"Faculty.html",{"Record":Record2})
    #     elif data2.exists():
    #         data='Wrong Password!!'
    #         return render(req,'loginfile.html')
    #     else:
    #         return redirect("/SignUp")
    elif role=="Admin":
        from . models import Record
        from . models import BlogData
        Eemail=req.POST.get("email")
        Epassword=req.POST.get("password")
        data=Record.objects.all()
        data2=Record.objects.all()
        blogdata=BlogData.objects.all().order_by('-id')
        for i in data:
            if Epassword==decrypt(i.password) and Eemail==i.email and "Admin"==i.role:
                return render(req,"Admin.html",{"Record":data2,"blog":blogdata}) 
            elif Eemail==i.email and "Admin"==i.role:
                msg='Wrong Password!!'
                return render(req,'loginfile.html',{"wrn":msg})
            elif Eemail==i.email and Epassword==decrypt(i.password):
                msg='Role Incorrect !!'
                return render(req,'loginfile.html',{"wrn":msg})   
            
                #data=Record.objects.filter(role=role,email=email,decrypt(password)=Epassword).values()
        return redirect('/SignUp')
    else:
        return redirect("/SignUp")
    


def savedata(req):
    from . models import Record
    email2=req.POST.get("email")
    role=req.POST.get("role")
    # print(role)
    data=Record.objects.filter(email=email2)
    if data.exists():
        from django.contrib.auth.hashers import make_password
        msg='Email already register plaese try other Email'
        name=req.POST.get("name")
        fname=req.POST.get("Fname")
        email=req.POST.get("email")
        password=req.POST.get("password")
      
     
        mobile=req.POST.get("mobile")
        dob=req.POST.get("dob")
        return render(req,'signupfile.html',{'a':msg,'name':name,'fname':fname,'email':email,'password':password,'dob':dob,'mobile':mobile})
    else:
        if role=="User":
            from . models import Record
            # from django.contrib.auth.hashers import make_password
            ob=Record() 
            ob.name=req.POST.get("name")
            ob.fname=req.POST.get("Fname")
            ob.email=req.POST.get("email")
            
            a=encrypt(req.POST.get("password"))
            print(a)
            recipient_list = req.POST.get("email") 
            #simple mail transfer protocal(smtp)
            send_mail(' Your Registration Successfull ','Now you can login','arrajashu@gmail.com',[recipient_list])
            ob.password=a
            ob.gender=req.POST.get("gender")
            ob.mobile=req.POST.get("mobile")
            ob.dob=req.POST.get("dob")
            ob.role=req.POST.get("role")
            ob.save()
            
            data='SignUp Successfully Now You Can LogIn!!'
            return render(req,'loginfile.html',{"wrn":data})
        # elif role=="Faculty":
        #     from . models import Record
        #     ob=Record()
        #     ob.name=req.POST.get("name")
        #     ob.fname=req.POST.get("Fname")
        #     ob.email=req.POST.get("email")
        #     ob.password=req.POST.get("password")
        #     ob.gender=req.POST.get("gender")
        #     ob.mobile=req.POST.get("mobile")
        #     ob.dob=req.POST.get("dob")
        #     ob.role=req.POST.get("role")
        #     ob.save()
        #     data='SignUp Successfully Now You Can LogIn!!'
        #     return render(req,'loginfile.html',{"wrn":data})
        elif role=="Admin":
            from . models import Record
            ob=Record()
            ob.name=req.POST.get("name")
            ob.fname=req.POST.get("Fname")
            ob.email=req.POST.get("email")
            ob.password=req.POST.get("password")
            ob.gender=req.POST.get("gender")
            ob.mobile=req.POST.get("mobile")
            ob.dob=req.POST.get("dob")
            ob.role=req.POST.get("role")
            ob.save()
            data='SignUp Successfully Now You Can LogIn!!'
            return render(req,'loginfile.html',{"wrn":data})
        else:
            return HttpResponse("Please choose a role...!!")
        

def writepost(req):
    return render(req,"write.html")
def post(req):
    from . models import BlogData
    from . models import Record
    email=req.POST.get("email")
    data3=Record.objects.filter(email=email).values()
    ob=BlogData()
    data2=BlogData.objects.filter(title=req.POST.get("titlename"),category=req.POST.get("category")).values()
    # print(req.POST.get("textdata"))
    print(data2)
    if (data2.exists()):
        msg="Your post Published"
        from . models import BlogData
        blog=BlogData.objects.all().order_by('-id')
        return render(req,"student.html",{"res":data3,"blog":blog,"msg":msg})
    else:
        import re
        # pattern = '<[^<]+?>'
        ob.title=req.POST.get("titlename")
        # outputString = re.sub(pattern, "", req.POST.get("textdata"))
        # ob.data=outputString
        ob.data=req.POST.get("textdata")
        # print(outputString)
        ob.name=req.POST.get("name")
        ob.email=req.POST.get("email")
        if len(req.FILES)!=0:
            ob.image=req.FILES['image']  
        ob.category=req.POST.get('category')
        import datetime
        current_time = datetime.datetime.now()
        ob.datetime=current_time
        print(req.POST.get('img'))
        ob.save()
        msg="Your post Published"
        from . models import BlogData
        blog=BlogData.objects.all().order_by('-id')
        print(blog)
        mypost=BlogData.objects.filter(email=req.POST.get("email")).values().order_by('-id')
        print(mypost)
        return render(req,"student.html",{"res":data3,"blog":blog,"msg":msg,"mypost":mypost})


def preview(req):
    email=req.GET.get('email')
    print(email)
    from . models import BlogData
    data=BlogData.objects.filter(email=email).values()
    if data.exists():
        return render(req,'preview.html',{"datas":data})
    else:
        from . models import Record
        Record2=Record.objects.filter(role="User").values()
            # Record3=Record.objects.filter(role="Faculty").values()
        return render(req,"Admin.html",{"Record":Record2})
def Del(req):
    id=req.GET.get('id')
    from . models import Record
    Record.objects.get(id=id).delete()
    Record2=Record.objects.filter(role="User").values()
    # Record3=Record.objects.filter(role="Faculty").values()
    return render(req,"Admin.html",{"Record":Record2})

def forgot(req):
    return render(req,'forgot.html')
             
def changepass(req):
    from . models import Record
    code2=req.POST.get("code")
    data=Record.objects.filter(email=code2).values()
    if data.exists():
        code=code2[:5]+'***@'+code2.split('@')[-1]
        otp2=req.POST.get("otp")
        otp=otp2.replace(' ','')
        # print(code)
        # print(otp)
        # print(otp2)
        recipient_list =req.POST.get("code")
        send_mail(' For the security of your property,do not disclose your verification  code to others!','Your blog otp'+'-"'+otp+'"','arrajashu@gmail.com',[recipient_list])
        return render(req,'forgot2.html',{"otp":otp,"code":code2,'codec':code})
    else:
        return redirect("/SignUp")
def otpvar(req):
    otp=req.POST.get('otp')
    reotp=req.POST.get('reotp')
    code=req.POST.get('code')
    code3=code[:5]+'***@'+code.split('@')[-1]

    # print(code)
    # print(reotp)
    # print(otp)
    if otp==reotp:
        from . models import Record
        print(code)
        data=Record.objects.filter(email=code).values()
        print(data)
        return render(req,'otpvar.html',{"data":data})
    msg="Invalid Code"
    return render(req,'forgot2.html',{"otp":otp,"code":code,'codec':code3,"msg":msg})

def passwordchange(req):
    from . models import Record
    code=req.POST.get('code')
    print(code)
    data=Record.objects.get(id=req.POST.get('code'))
    data.password=encrypt(req.POST.get("password"))
    data.save()
    recipient_list =req.POST.get('email')
    send_mail(' password changed successfully','login again!','arrajashu@gmail.com',[recipient_list])
    msg="password change successfully"
    return render(req,"Loginfile.html",{'wrn':msg})
    # print(data)
    # data=Record.objects.get(id=req.POST.get('code'))





def Deletepost(req):
    Eid=req.GET.get('id')
    print(id)
    Email=req.GET.get('gmail')
    print(Email)
    from . models import Record
    from . models import BlogData
    a=BlogData.objects.get(id=Eid)
    a.delete()
    a.save()
    
    data2=Record.objects.filter(email=Email).values()
    blogdata=BlogData.objects.all().order_by('-id')
    mypost=BlogData.objects.filter(email=req.POST.get("email")).order_by('-id')
    return render(req,"Student.html",{"res":data2,"blog":blogdata,"mypost":mypost})


def useredit(req):
    eid=req.POST.get('mid')
    print(eid)
    from . models import Record
    from . models import BlogData

    data2=Record.objects.filter(email=req.POST.get('email1')).values()
    blogdata=BlogData.objects.all().order_by('-id')
    mypost=BlogData.objects.filter(email=req.POST.get("email1")).order_by('-id')
    print(data2)
    print(blogdata)
    print(mypost)
    a=Record.objects.get(id=eid)
    print(req.POST.get('name1'))
    a.name=req.POST.get('name1')
    a.fname=req.POST.get('fname1')
    a.mobile=req.POST.get('mobile1')
    a.gender=req.POST.get('gender1')
    if len(req.FILES)!=0:
        a.pimage=req.FILES['pimage']  
    a.save()
    return render(req,"Student.html",{"res":data2,"blog":blogdata,"mypost":mypost}) 





def passchange(req):
    eid=req.POST.get('pid')
    from . models import Record
    a=Record.objects.get(id=eid)
    new=encrypt(req.POST.get('p1'))
    a.password=new
    a.save()
    return render(req,'loginfile.html')



def blogDelete(req):
    from . models import BlogData
    eid=req.POST.get('eid')
    print(eid)
    BlogData.objects.get(id=req.POST.get('eid')).delete()


    from . models import Record

    data2=Record.objects.filter(email=req.GET.get('email1')).values()
    blogdata=BlogData.objects.all().order_by('-id')
    mypost=BlogData.objects.filter(email=req.GET.get("email1")).order_by('-id')
    return render(req,"Student.html",{"res":data2,"blog":blogdata,"mypost":mypost}) 
def savemsg(req):
    from . models import savemsg
    a=savemsg()
    a.uname=req.POST.get('uname')
    a.uemail=req.POST.get('uemail')
    a.usub=req.POST.get('usub')
    a.umsg=req.POST.get('umsg')
    a.save()
    recipient_list =req.POST.get('uemail')
    send_mail(' message received','thanks for connecting us','arrajashu@gmail.com',[recipient_list])
    return redirect("/")

# from django.shortcuts import render
# from django.http import HttpResponse
# from. models import EmpLogin
# from home.encrypt_util import *
# def register(request):   
#     if request.method == 'POST':      
#         name = request.POST['name']       
#         email = request.POST['email']    
#         password = request.POST['password']      
#         print('Original Password:', request.POST['password'])    
#         encryptpass= encrypt(request.POST['password'])    
#         print('Encrypt Password:',encryptpass)    
#         decryptpass= decrypt(encryptpass)   
#         print('Decrypt Password:',decryptpass)     
#         data=EmpLogin(name=name, email=email, password=password)  
#         data.save()        
#         return HttpResponse('Done')   
                                        
#     else:    
#         return render(request, 'index.html')


# from cryptography.fernet import Fernet
# import base64
# import logging
# import traceback
# from django.conf import settingsdef
# def encrypt(pas): 
#     try:       
#         pas = str(pas)   
#         cipher_pass = Fernet(settings.ENCRYPT_KEY)    
#         encrypt_pass = cipher_pass.encrypt(pas.encode('ascii'))  
#         encrypt_pass = base64.urlsafe_b64encode(encrypt_pass).decode("ascii")    
#         return encrypt_pass  
#     except Exception as e:    
#         logging.getLogger("error_logger").error(traceback.format_exc())    
#         return None
# def decrypt(pas):  
#     try:      
#         pas = base64.urlsafe_b64decode(pas)    
#         cipher_pass = Fernet(settings.ENCRYPT_KEY) 
#         decod_pass = cipher_pass.decrypt(pas).decode("ascii")       
#         return decod_pass  
#     except Exception as e:    
#         logging.getLogger("error_logger").error(traceback.format_exc())   
#         return None

