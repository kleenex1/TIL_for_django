# 비밀번호 관리기능 
## 비밀번호 초기화
![1](./password/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-11-10%20134035.png)<br>
## 비밀번호 변경
![2](./password/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-11-10%20134050.png)

장고에서 제공하는 템플릿이 비밀번호를 바껴도 화면이 바뀌는것이 없어서 view에서 커스터마이징하여 바꿔준다.
![3](./password/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-11-10%20134058.png)<br>
passwordchangview에도 get_success_url이 정의되어있다. 근데 또 상속받아서 자식클래스에서 정의해주는것을 오버라이딩이라고 하고 자식클래스에서 오버라이딩하면 자식클래스에서 정의한것이 사용된다.<br>
![4](./password/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-11-10%20134108.png)<br>
allauth.urls에도 password/change url이 있다 하지만 유저 커스텀한 것을 먼저 찾게 함으로써 커스텀한 페이지를 보여주게 한다. 