# 회원가입정보 유효성 검사

![1](./uservalidators/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-11-10%20114957.png)

닉네임에 대한 validator는 validator 파일을 이용하여 추가해주었음. 

근데 비밀번호 validator는 class로 되어 있다. 비밀번호는 class로 해줘야한다. (대부분은 함수형으로 되어 있음.)<br>
![2](./uservalidators/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-11-10%20115018.png)<br>
> def validate : 회원가입 할때 
> def get_help_text : 어드민 페이지에서 비밀번호를 바꿀 때


settings에서 django 기본 validator를 지우고 커스텀한 validator를 사용한다.<br>
![3](./uservalidators/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-11-10%20115436.png)<br>

닉네임이 중복되면 비밀번호가 계속 초기화 되는데, 

![4](./uservalidators/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-11-10%20115447.png)<br>
이를 방지하기 위해서 `ACCOUNT_PASSWORD_INPUT_RENDER_VALUE`를 설정한다.<br>
![5](./uservalidators/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-11-10%20115455.png)<br>

![6](./uservalidators/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-11-10%20115504.png)