# Django 앱의 철학
* App은 하나의 기능 단위, 프로젝트는 여러개의 App을 가진다. 

> 요청과 응답
> Url → View → Template

# 장고의 MVT 패턴
![1](./reusable_app.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-09-24%20171135.jpg)

1. 클라이언트의 요청을 받으면 `settings.py`의 Root_URLCONF는 Django가 URL을 분석한다.
2. URL 분석 후 담당할 View를 결정한다.
3. View는 데이터 베이스 처리가 필요하면 모델을 통해 처리하고 그 결과를 반환받는다.
4. View는 로직 처리가 끝나면 Template을 사용하여 클라이언트에게 전송할 html 파일을 생성하고 html 파일을 클라이언트에게 보내 응답한다.

# Django Template & Render 
* 화면 구성은 Template에서 Rendering을 통해 HttpResponse 객체로 변환된다.
* render(request, httpresponse)

# MVT 
* Model
  * 데이터구조 생성
  * 데이터베이스와 소통
* Template
  * 웹 사이트 화면 구성 담당
  * 매번 바뀌는 동적인 화면 구성(Template language를 사용하면 세부내용을 동적으로 구성할 수 있다.)
* View
  * 웹사이트 로직을 담당
  * Model과 Template 사이를 연결

# MVT 코딩 순서
1. 프로젝트 뼈대 만들기 : 프로젝트 및 앱 개발에 필요한 디렉토리, 파일 생성
2. 모델 코딩하기 : 테이블 관련 사항 개발(`models.py`, `admin.py`)
3. URLconf : `urls.py` 
4. Template : templates/ 하위 폴더의 html파일
5. View : `views.py` 

