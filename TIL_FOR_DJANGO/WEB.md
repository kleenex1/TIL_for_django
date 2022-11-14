# Web 이란?
# 인터넷과 웹

## 인터넷
* Internet은 컴퓨터로 연결하여  TCP/IP(Transmission Control Protocol/Internet Protocol)라는 [통신 프로토콜](https://ko.wikipedia.org/wiki/%ED%86%B5%EC%8B%A0_%ED%94%84%EB%A1%9C%ED%86%A0%EC%BD%9C "통신 프로토콜")을 이용해 정보를 주고받는 [컴퓨터 네트워크](https://ko.wikipedia.org/wiki/%EC%BB%B4%ED%93%A8%ED%84%B0_%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC "컴퓨터 네트워크")이다.

## WWW란?
* World Wide Web의 약자로 인터넷에 연결된 컴퓨터를 이용해 사람들과 정보를 공유할 수 있는 공간. HTTP를 기반으로 HTML로 작성된 하이퍼 텍스트를 웹브라우저를 통해 읽을 수 있게 디었다. 인터넷과 동일하다고 볼 수 있지만 엄밀히는 인터넷보다는 작은 개념.

## HTTP와 HTTPS
* 정의
	* HyperText Transfer Protocol의 약자로 하이퍼 텍스트를 교환, 전송을 위한 통신 규약
		* 만약 컴퓨터 A와 컴퓨터 B가 사양도 다른 상황에서 두 컴퓨터를 통신으로 연결 하고 싶다면?에서 출발한 것으로 HTTP는 다양한 환경에서 여러 기기가 통신을 주고 받을 수 있게 만든 일종의 규칙.

* 구조
	* 클라이언트와 서버사이에 이뤄지는 `요청`과 `응답`으로 이뤄진다. 단순해 보이지만 우리가 이용하는 인터넷은 무수한 응답과 요청으로 이뤄진다. 홈페이지 주소를 입력할 때 쓰는 http는 http 프로토콜을 이용해 정보를 교환한다는 의미이다.

* HTTP와 get, post
	* http를 통해 클라이언트가 서버 측에 요청을 보낼 때 사용하는 방식이 크게 2가지다.(GET / POST)
	* `GET`
		* 일반적으로 get은 DB에서 자료를 가져와서 읽을 때 주로 사용한다.
	* `POST`
		* 서버의 DB 값이나 상태를 바꾸는 *쓰기*, *수정*을 할때 주로 사용한다.
	* 정리 
		* get방식은 동영상, 이미지, 텍스트를 읽어오는 등 서버에 저장된 데이터를 가져올때
		* post방식은 게시판에 글을 쓴다, 회원가입을 한다는 DB에 영향을 줄때
		* (get은 링크를 전달할때 용도로 쓸 수 있다면 post방식으로 자료를 읽어오면 자료의 링크가 전부 숨겨진다. 그러므로 링크로 타인에게 자료를 전달하려고해도 불가능해진다.)

* HTTP응답(response) 코드 [mdn링크](./https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
	* 100번대 : Informational responses
	* 200번대 : Successful responses
	* 300번대 : Redirection messages
	* 400번대 : Client error responses
	* 500번대 : Server error responses

* HTTPS
	* 보안이 강화된 HTTP
	* 일반적으로 SSL 또는 TSL 프로토콜을 이용해 데이터를 암호화한다. 


## HTTP의 특징
1. HTTP는 Stateless다.
	* HTTP 프로토콜은 현재 상태를 저장하지 않는다.
	* 클라이언트가 한 개의 요청을 하면 한 개의 응답을 할 뿐이다.
	* 하지만 쿠키, 세션 등을 이용하면 이러한 Stateless 상태를 극복할 수 있다.
2. HTTP는 확장이 가능하다.
	* HTTP는 헤더라는 부분을 추가함으로써 더욱 다양한 정보를 주고 받을 수 있다.
3. HTTP는 ASCII로 인코딩된 텍스트로 구성되어있다.
4. 메시지의 구성
	* 출발선, 헤더, 바디로 나뉜다. 

	### Request Header
	![request](./web.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-09-24%20162433.jpg)
	1. 출발선(Start Line)
		* 최상단 첫번째 줄. GET, POST, PUT 과 같은 HTTP메서드, URII, HTTP 버전
	2. 헤더(Headers)
		* Host : 클라이언트가 요청하는 호스트에 대한 정보
		* User-Agent : 클라이언트에 대한 각종 정보 운영체제, 브라우저 내용 등..
		* Accept : 클라이언트 측에서 원하는 데이터 타입
	3. 본문(Body)
		* 요청의 경우가 있을 수 있고 없을 수도 있다. 응답의 경우 요청에 대한 응답 데이터를 보내야해서 본문에 대부분 내용이 있으나 요청의 경우 본문이 존재하지 않는 경우도 있다.
	### Response Headers
	![response](./web.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-09-24%20162509.jpg)
	1. 출발선(Start Line)
		* 여기에는 응답코드가 있다. (Http Response Code) 2xx,3xx,4xx,5xx...
	2. 헤더(Headers)
		* 요청에 따른 응답에 대한 정보
		* Content-Type : 클라이언트에게 전송된 자료의 종류, 인코딩 방식
		* Date : 해당 메시지가 만들어진 날짜
	3. 본문(Body)
		* 요청할때는 없을 수도 있지만, 서버측이 응답할 땐 body가 거의 있다. 그래야 컴퓨터 사용자의 요청이 제대로 수행되어 결과물이 나온 것을 확인할 수 있기 때문이다.

