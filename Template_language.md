# Template Language 


# 템플릿 변수 (Template Variable)

```html
{{ variable }}
```
템플릿 변수는 템플릿이 렌더될 때 해당 변수가 의미하는 값으로 변환된다. 
뷰(View)에서 가공한 데이터를 템플릿으로 넘겨주면 템플릿에서는 템플릿 변수를 사용해 넘겨받은 데이터에 접근할 수 있습니다.

## 템플릿 변수의 점(.) 연산자

템플릿 변수는 점(.)을 사용해서 변수 안쪽 속성에 접근할 수 있습니다.

```python
user = {"name" : "우재", "coffee" : True}
```

이와 같은 점(.) 연산자는 다음과 같은 `순서`로 변수의 안쪽 속성에 접근을 시도합니다.

1.  변수를 `사전형(dict)`으로 생각하고 점(.) 연산자로 Key값 조회
2.  변수를 `객체`로 생각하고 내부 속성값 조회 또는 함수 호출
3.  변수를 `리스트(list)`로 생각하고 점(.) 연산자로 Index 조회

# 템플릿 필터 (Template Filter)

```html
{{ variable|filter }}
```

템플릿 변수에 파이프(|)를 쓰고 템플릿 필터를 사용하면 템플릿 변수를 특정 형식으로 변환 할 수 있습니다.

```html
{{ variable|filter:args }}
```

일부 필터는 필터 뒤에 인자를 필요로 합니다. Django는 약 60개의 내장 템플릿 필터를 제공하며 개발자가 직접 필터를 정의해서 사용하는 것도 가능합니다. 아래는 몇 가지 내장 템플릿 필터입니다.

### **default**

참조하는 템플릿 변수가 비어 있거나 boolean형의 False일 경우 변환되는 값을 지정합니다.

```
{{ variable|default:"coffee" }} 
```
변수가 비어 있거나 False면 coffee 라는 텍스트로 대체.

### **capfirst**

맨 첫글자를 대문자로 바꿔 줍니다.

```
{{ variable|capfirst }}
```

### **random**

반복 가능한 템플릿 변수에 대해 무작위로 하나를 추출해 변환합니다.

```
{{ variable|random }}
```

만약 variable이 참조하는 값이 [ "a", "b", "c", "d" ] 인 리스트형이라면 템플릿 변수가 리스트 내의 하나의 원소로 대체 됩니다.

### **upper & lower**

템플릿 변수를 대문자(upper) 또는 소문자 (lower)로 변환합니다.

```
{{ variable | upper }} , {{ variable | lower }}
```

### **ljust & rjust**

주어진 길이 내에서 공백을 넣어 왼쪽 정렬(ljust) 또는 오른쪽 정렬(rjust)을 한 문자열로 변환합니다.

```
{{ variable|ljust:"length" }}, {{ variable|rjust:"length" }}
```

variable이 "TEST" 일 때 {{ variable|ljust:"10" }} 이라면 "TEST "이 됩니다. 
공백을 표시해서 보면 "TEST_ _ _ _"이런 형태인거죠.
마찬가지로 만약 {{ variable|rjust:"10" }} 이라면 " TEST"이 되겠죠?

`참고문서`
[https://docs.djangoproject.com/en/2.2/ref/templates/builtins/#ref-templates-builtins-filters](https://docs.djangoproject.com/en/2.2/ref/templates/builtins/#ref-templates-builtins-filters)

# 템플릿 태그 (Template Tag)

```html
{% tag %}
```

템플릿 태그는 템플릿을 작성할 때 반복문, 조건문 등의 로직을 사용해서 마치 프로그래밍을 하듯 템플릿을 작성할 수 있게 해줍니다. Django가 기본적으로 제공하는 태그가 있지만, 개발자가 직접 태그를 정의해서 사용할 수도 있습니다.

```html
{% tag %} ~ {% endtag %}
```

태그의 형태는 단독으로 사용하는 템플릿 태그와 여는 태그와 닫는 태그가 필요한 템플릿 태그가 있습니다. 아래는 몇 가지 기본 템플릿 태그입니다.

### **for**

```
{% for obj in values %} ~ {% endfor %}
```

반복 가능한 객체를 반복하며 템플릿을 작성 할 수 있습니다.

```html
{% for food in foods %} 
    <li> {{ food.name }} </li>
{% endfor %}
```

만약 목록을 역순으로 반복하고 싶다면 아래와 같이 사용 할 수 있습니다.

```html
{% for food in foods reversed %} 
    <li> {{ food.name }} </li>
{% endfor %}
```

반복 가능한 객체가 비어 있거나 존재하지 않을 때는 아래와 같이 사용 할 수 있습니다. 아래는 만약 foods라는 객체가 비어있다면 {% empty %} 구문이 실행됩니다.

```html
{% for food in foods %} 
    <li> {{ food.name }} </li>
{% empty %}
    <li> There is no food. </li>
{% endfor %}
```

### **if**

```
{% if value1 %} ~ {% elif value2 %} ~ {% else %} ~ {% endif %}
```
```html
{% if hungry %}
    <p> Let's eat! </p>
{% elif sleepy %}
        <p> You need some coffee. </p>
{% else %}
    <p> Go back to work. </p>
{% endif %}
```

### **with**

```
{% with value1=value2 %} ~ {% endwith %}
```

복잡한 변수가 있을 때 '별명'을 붙이기 위해 사용합니다. with 구문 내에서는 value1을 value2 대신 사용할 수 있습니다.

[https://docs.djangoproject.com/en/2.2/ref/templates/builtins/#ref-templates-builtins-tags](https://docs.djangoproject.com/en/2.2/ref/templates/builtins/#ref-templates-builtins-tags)

# 사용자 정의 필터와 태그
[https://docs.djangoproject.com/en/2.2/howto/custom-template-tags/](https://docs.djangoproject.com/en/2.2/howto/custom-template-tags/)