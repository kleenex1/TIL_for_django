# 숨어있는 IP와 PORT

* 로컬에서 개발할때 Terminal에서 `python manage.py runserver`라는 명령어를 통해 개발서버를 실행해서 사용하지만 사실은 runserver 뒤에 IP와 PORT 인자가 숨어있다. 따로 적어주지 않는다면 `127.0.0.1`(내컴퓨터 IP) 이라는 IP와 `8000`번 포트를 사용해서 서버가 실행된다.
* IP : Internet Protocol의 약자로 네트워크 상에서 다른컴퓨터와 내컴퓨터를 구별하는 일종의 주소
* Port : IP로 찾은 컴퓨터 내부에서 실행되고 있는 프로그램이나 서비스를 구분하는 값, IP를 이용해 컴퓨터를 찾고 그 안에서 포트를 가지고 프로그램을 찾는다.

```python
django-admin runserver {ip:port}
python manage.py runserver {ip:port}
```