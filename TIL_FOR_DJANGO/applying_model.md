# 모델 적용하기

* 하드코딩은 지양되어야 한다.
![1](./applying_model.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-09-26%20194427.png)
* 이러한 데이터들은 앞에서 view에서 모두 넘겨주도록 만들고, index view는 모델에서 가져오도록 한다.

## 모델을 import 한다.
![2](./applying_model.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-09-26%20194640.png)

## index view를 수정한다.
![3](./applying_model.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-09-26%20195053.png)

## block안 내용을 바꿔준다.
![4](./applying_model.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-09-26%20195849.png)
* 데이터로 조회해서 받은 queryset은 리스트 처럼 사용할 수 있다.( `menus = [Menu, Menu.....]`)
* 그 쿼리셋은 Menus라는 키로 접근할 수 있다.
![5](./applying_model.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-09-26%20200520.png)
