# 관리자도구(Admin)

* shell을 이용했던 것들을 Admin을 이용하면 좀 더 쉽게 다룰 수 있다.

1. 관리자 계정 생성하기
```python
python manage.py createsuperuser
```
![1](./admin.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-09-25%20164238.png) <br>
2. 관리자 페이지 사용하기(관리자페이지에 추가했던 모델이 없다.)<br>
![2](./admin.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-09-25%20164438.png) <br>
3. 앱 안의 admin 파일에 들어가서 설정했던 Model을 import해준다.<br>
![3](./admin.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-09-25%20164537.png)<br>
4. 추가한 모델이 관리자 페이지가 생성되었다.<br>
![4](./admin.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-09-25%20164646.png)<br>
5. 모델을 눌러보면 추가한 데이터들을 볼 수 있다.<br>
![5](./admin.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-09-25%20164946.png)<br>
6. 데이터 추가 및 수정도 가능하다.<br>
![6](./admin.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-09-25%20165035.png)<br>
