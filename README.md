# Blog_Django

------

**장고로 블로그, 사진첩 기능 구현**

-----

### Project

-----

##### Built With

>+ Python Django
>+ HTML 

##### Getting Started

>+ 가상환경 설치 및 시작
>
>  ```python
>  python3 -m venv myvenv
>  
>  source myvenv/bin/activate. #mac기준
>  ```

>+ 장고 설치
>
>  ```python
>  pip install django
>  ```

---------

Using

장고의 파일 관리

>1. static file : 서버에 저장된 그대로를 서비스해 주는 파일 - 외부와 통신 x
>2. Dynamic file : 서버의 데이터들이 어느정도 가공된 다음 서비스되는 파일 - 외부와 통신 o

정적파일?

>종류
>
>>1. 프로젝트 입장에서 이미 무엇인지 아는 파일 -> 개발할 때 미리 준비해둔 파일 ="static" :미리 준비해둔 사진 띄우기
>>2.  웹 서비스 이용자들이 업로드 하는 파일 ="media" : 사진 업로드 

Static 파일의 처리 과정 

>1. Static 파일들의 위치 찾기
>2. static 파일들을 한 곳에 모으기 

static 파일 모아주기

<img width="453" alt="image-20200516023134016" src="https://user-images.githubusercontent.com/49120090/82084436-41fef200-9726-11ea-94cf-307be1dc962f.png">

Media

>Django와 외부의 통신망 = URL
>
>외부와 통신. -> settings.py안에 업로드된 파일저장할 디렉토리 경로뿐 아니라 외부와 통신할 수있는 경로 지정
>
>1. media파일의 어느 URL을 타고 - MEDIA_URL
>2. 어디로 모을 것인지 - MEDIA_ROOT

>[방법]
>
>1. Settings.py에서 media 설정(디렉토리,URL 설정)
>
>2. Url.py 설정
>
>   >```from django.conf import settings```
>   >
>   >```from django.conf.urls.static import static```
>   >
>   >이렇게 두 개 import 시켜주어야 한다. 
>
>   >```python
>   >urlpatterns = [
>   >    path('admin/', admin.site.urls),
>   >    path('',blogapp.views.home, name="home"),
>   >    path('blog/<int:blog_id>',blogapp.views.detail,name="details"),
>   >    path('blog/new/',blogapp.views.new, name="new"),
>   >    path('blog/create',blogapp.views.create, name ="create"),
>   >    path('portfolio/',portfolio.views.portfolio, name="portfolio"),
>   >
>   >
>   >] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>   >```
>   >
>   >
>
>3. models.py에서 업로드 될 데이터 class 정의
>
>4. DB에 내 말을 들어줘 -migrate
>
>5. admin.py -> admin.site.register()
>
>6. "모든 객체 내용을 보여줘" -> 함수 정의 -> views.py
>
>7. HTML 뜨우기

<img width="448" alt="image-20200516023043746" src="https://user-images.githubusercontent.com/49120090/82084470-4c20f080-9726-11ea-8c2d-1d2e6d38c843.png">

: 이미지를 데이터베이스에 넣고 싶을 때 pip install pillow 설치. 

