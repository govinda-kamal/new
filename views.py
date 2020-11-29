from django.shortcuts import render
from django.http import HttpResponse   #4t import HttpResponse  and then see at botton for futhr=ur steps
from .models import Post
# Create your views here.
def Bloghome(request) :
    allpost=Post.objects.all()
    context={"allpost":allpost}
    return render(request,"blog/bloghome.html",context)

    # return HttpResponse("this is home")      when we return Httpresponse then whatever the content we want to dispaly , we pass as a argument and when we return rnder then it take genrally 3 argument request, file.html, dictionary
    #  similarly do for home app

def blogpost(request,slug) :
    post=Post.objects.filter(slug=slug)[0]   #getting the title of the post which have the slug==slug(Argument)
    print(post)
    context={"post":post}
    return render(request,"blog/blogpost.html",context)
# def blogpoststr(request,sl) :
#     return render(request,"blog/blogpoststr.html")

    # return HttpResponse(f"this is blogpost of blog {sl}")   the argumnent which we use <str:sl> then here also use sl
#  def blogpost(request) :
#     allpost=Post.objects.all()
#     context={"allpost":allpost}
#     return render(request,"blog/blogpost.html")









    #now 5th step is to add bootstrap and html ,css ,js files to our website 
    # to do it 1st we make templates and static file in outermost dictionary
    # now all the html file which is required we will make in templates and call it in the corresponing app
    # now django wil search the template and it will not found by him so we have to go to setting and write the name of folder where our html files are located
    # now to if there are no. of html files then it will create a problem therefore make no. of new folder = no. of apps 
    # now in template there are no. of html files and in each file if we want to add same content then we can make a basic.html to inherit its content in othe r files