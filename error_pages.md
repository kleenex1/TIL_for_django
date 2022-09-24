# 제공하지 않는 url에 접근했을 때
1. Http 404를 불러온다.
```python
from django.http import Http404
```

2. if else구문을 통해 raise 에러를 실행시킨다.
```python
raise Http404("잘못된 경로입니다!")
```
![1](./error_pages.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-09-24%20200636.jpg)

# 상태 코드(Status Code)

상태 코드(Status Code)는 클라이언트 요청에 대한 처리가 성공했는지 실패했는지에 대해 알려주는 코드로 앞자리에 따라 크게 5가지 카테고리로 분류됩니다. 아래는 각 분류별 몇 가지 상태 코드입니다.

## 1XX (정보 전달)

-   100 (진행, Continue)
    
    요청의 첫 부분을 받아서 다음 요청을 기다리고 있다는 것을 알려 줍니다. 이미 요청을 완료했다면 해당 응답을 무시할 수 있습니다.
    
-   101 (프로토콜 전환, Switching Protocol)
    
    클라이언트가 서버에게 프로토콜 전환을 요청했고 서버에서 프로토콜을 변경한다는 것을 나타냅니다.
    

## 2XX (성공)

-   200 (성공, OK)
    
    클라이언트의 요청이 성공적으로 처리되었다는 것을 의미하며 주로 요청한 페이지를 서버가 제공했다는 것을 알려줍니다.
    
-   201 (작성됨, Created)
    
    요청이 성공적으로 처리되어 새로운 리소스를 생성했다는 것을 의미합니다.
    
-   202 (허용됨, Accepted)
    
    서버가 성공적으로 요청을 받았지만 아직 처리 전인 상태를 나타냅니다.
    
-   203 (신뢰할 수 없는 정보, Non-Authoritative Information)
    
    서버가 성공적으로 요청을 처리했지만 요청에 포함된 정보가 다른 곳에서 수정된 정보라는 것을 나타냅니다.
    
-   204 (콘텐츠 없음, No Content)
    
    요청을 성공적으로 처리했지만 콘텐츠를 제공하지 않는다는 것을 의미합니다.
    
-   205 (콘텐츠 재설정, Reset Content)
    
    요청을 성공적으로 처리했고 콘텐츠를 제공하지 않으며 클라이언트가 문서 보기를 재설정할 것을 요구합니다.
    

## 3XX (리다이렉션)

-   300 (여러 개의 선택 항목, Multiple Choice)
    
    요청에 대해 서버가 여러 응답이 가능하며 하나를 선택해야 함을 나타냅니다.
    
-   301 (영구 이동, Moved Permanently)
    
    요청한 리소스가 새로운 위치로 영구 이동했음을 나타냅니다. 클라이언트는 자동적으로 새로운 위치로 전달됩니다.
    
-   302 (임시 이동, Found)
    
    요청한 리소스가 일시적으로 이동했음을 나타내며 향후 다시 해당 리소스를 요청할 때도 동일한 주소로 해야 한다는 것을 알려줍니다.
    
-   304 (수정되지 않음, Not Modified)
    
    마지막 요청 이후 요청한 리소스는 수정되지 않았다는 것을 알려주며 서버가 콘텐츠를 전달하지 않습니다. 클라이언트는 이전에 전달받은 결과를 계속해서 사용할 수 있습니다.
    

## 4XX (실패)

-   400 (잘못된 요청, Bad Request)
    
    클라이언트의 요청을 서버가 이해할 수 없다는 것을 의미합니다.
    
-   401 (권한 없음, Unauthorized)
    
    클라이언트가 해당 요청에 대한 응답을 받기 위해서는 추가적인 인증이 필요하다는 것을 나타냅니다.
    
-   402 (결제 필요, Payment Required)
    
    이 요청을 결제가 필요하다는 것을 의미하며 처음 이 응답 코드가 만들어질 당시에는 결제 시스템에 사용할 목적이었으나 현재는 사용되고 있지 않습니다.
    
-   403 (금지됨, Forbidden)
    
    클라이언트가 요청한 리소스에 접근할 권한이 없음을 의미합니다. 401과 다른 점은 서버는 해당 클라이언트에 대한 정보를 가지고 있다는 점입니다.
    
-   404 (찾을 수 없음, Not Found)
    
    클라이언트가 요청한 리소스를 서버가 찾을 수 없다는 것을 의미합니다.
    

## 5XX (서버 오류)

-   500 (내부 서버 오류, Internal Server Error)
    
    서버에서 오류가 발생하여 요청한 작업을 수행할 수 없다는 것을 의미합니다.
    
-   501 (구현되지 않음, Not Implemented)
    
    클라이언트가 요청한 방법을 서버에서 수행할 수 있는 기능이 없다는 것을 의미합니다.
    
-   502 (잘못된 게이트웨이, Bad Gateway)
    
    서버가 요청을 처리하는데 필요한 작업 중 게이트웨이로부터 잘못된 응답을 받았다는 것을 의미합니다.
    
-   503 (서비스를 사용할 수 없음, Service Unavailable)
    
    서버가 해당 요청을 처리할 준비가 되지 않았으며 일반적으로는 유지관리를 위해 작동이 중단되거나 과부하가 걸렸을 때를 나타내며 대개 일시적입니다.
    

더 많은 상태 코드에 대해 알고 싶다면 아래 링크를 참고하세요. [https://developer.mozilla.org/en-US/docs/Web/HTTP/Status](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)