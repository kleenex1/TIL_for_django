# 템플릿 상속하는 방법
`{% block %}`
`{% extends %}`
<hr>

0. base.html이라는 파일을 새로 생성한다.
1. 기존의 index.html 에 있는 모든 코드를 복사하여 base.html이라는 곳에 붙여준다.
2. 이제 base.html이 부모 템플릿(뼈대)이 되고 index.html이 자식 템플릿이 된다.

![1](./template_inheritance.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-09-24%20184033.jpg)
![2](./template_inheritance.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-09-24%20184229.jpg)
* 변경되는 부분은 블럭으로 만들어주고, 그 외는 남겨두면 된다.


![3](./template_inheritance.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-09-24%20185323.jpg)
* 다음으로 자식 템플릿의 가장 최상단에`{% extends './base.html' %}` 이라고 부모 템플릿 을 지정한다.

* 만약, 자식템플릿에서 따로 구현해주지 않으면 부모 템플릿의 내용을 그대로 사용하게된다.