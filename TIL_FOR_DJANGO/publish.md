# 배포하기

* 서버도 하나의 컴퓨터, 하지만 잘 꺼지지 않고 안정성이 높은 컴퓨터이다
* 서버로 사용할 컴퓨터를 일반사람들이 구축하고 관리하기 힘드니 업체가 서버를 제공하고 일반사람들은 해당 서버를 네트워크를 통해 사용하게 되는데 이를 클라우드 서비스라고 한다.
* 서버를 위한 클라우드 서비스는 2가지가 있다.(서비스를 어디까지 설정해서 사용할 수 있는가에 차이가 있다.)

## IaaS(Infrastructure as a Service)
* 서버 장비만 빌려서 사용하는 방식
* 서버 장비 + 운영체제만 제공
* 개발자가 필요한 프로그램을 직접 설치 및 설정
* 까다롭지만 필요한 최적의 환경 구성 가능
* AWS EC2

## PaaS(Platform as a Service)
* 서버 장비 + 운영체제 + 실행환경 제공
* 전체적인 실행환경이 갖춰져 있음
* 서버 구축보다 개발하는 프로젝트에 더 집중 가능
* AWS Elastic Beanstalk, Google App Engine, Heroku
* pythonanywhere : Python App에 특화된 서비스
