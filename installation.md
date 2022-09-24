# Django 설치

## 1. 새로운 폴더를 만든다.
```python
mkdir [폴더이름]
```

## 2. 파이썬3인지 확인한다.  
```python
python --version
```
![1](./installation.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-09-24%20162941.jpg)

## 3. 가상환경 생성하기
```python
python -m venv [가상환경 작명해주기]
```
![2](./installation.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-09-24%20164531.jpg)

## 4.  가상환경 실행해주기
```python
source Scripts/activate
# 혹은
. Scripts/activate
```
![3](./installation.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-09-24%20164546.jpg)
* (venv) : 본인이 설정한 가상환경의 이름이 나타나면 가상환경이 실행된 상태.
* deactivate : 가상환경 종료 커맨드

## 5. 가상환경 내에서 Django 설치하기
```python
pip install django # 최신버전 설치
pip install djang==3.2.13 # 특정 버전 설치
```
![4](./installation.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-09-24%20164555.jpg)

## 6. Django 프로젝트 생성하기
```python
django-admin startproject [프로젝트이름] [설치경로] #설치경로 생략 혹은 .
```
![5](./installation.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-09-24%20164604.jpg)
## 7. Django 서버 실행 해보기
```python
python manage.py runserver
```
![6](./installation.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-09-24%20164852.jpg)
* 항상 파일내에 어떤 폴더/파일이 있는지 ls로 확인후 명령어를 입력해준다.

## 완료
![7](./installation.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-09-24%20164613.jpg)


