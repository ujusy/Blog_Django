from django.shortcuts import render, get_object_or_404,redirect
from django.utils import timezone
from blogapp.models import Blog
# Create your views here.

def home(request):
    blogs = Blog.objects #쿼리셋
    return render(request,'blogapp/home.html',{'blogs':blogs})

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk = blog_id) #몇 번 객체
    return render(request, 'blogapp/detail.html',{'details':details})

def new(request): #new.html을 띄우주는 함수
    return render(request, 'blogapp/new.html')

def create(request): #입력받은 내용을 데이터베이스에 넣어주는 함수
    blog = Blog() #블로그라는 class로 부터 blog 객체 생성
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_data = timezone.datetime.now()
    blog.save() #쿼리셋 메소드. 블로그라는 객체에 위와 같이 넣어준 상태를 database에 저장해라 라는 메소드이다. 
    return redirect('/blog/'+str(blog.id))      #객체.delete()는 데이터  베이스에서 삭제하라는 뜻
    
#redirect (URL) : 위에 다 처리 후 URL에 다 넘기세요. URL은 항상 str형 이므로 blog.id를 str형으로 변환
#render: request가 들어오면 html을 띄우는데 사전형 데이터를 담아서 띄워라. 
#둘의 차이는 인자에 따라서 어떤 상황에 따라 사용할지에 따라 사용하면 된다.  render은 html상에서 data를 담아서 처리하고 싶을때 사용 