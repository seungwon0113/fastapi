http -> TCP 연결 위에서 텍스트를 정해진 규칙대로 주고 받는 것 입니다.


HTTP/1.1 200 OK
content-length: 25
content-type: application/json
date: Wed, 30 Oct 2024 02:15:00 GMT
server: uvicorn

{
    "message": "Hello World"
}

<yaml>
message:
    "Hello World"


http response 를 구성하는 요소
첫줄:
    -http version
    -status code (숫자)
    -status code 에 상응하는 문자

(첫 줄과 헤더 줄 사이에는 개행을 "한번" 한다)
(헤더 하나당 개행을 한 번씩 한다.)
request header랑 reponse header가 있다.
request, response 에 둘 다 쓸 수 있는 header도 있다.
response header 는 response에 대한 메타 데이터다
헤더 줄 :
 -> 지금까지 써 본 header..?

header -> User-Agent ex) chrome... ex) 휴대폰으로 할수 없습니다. 데스크탑을 이용해주세요.

1. http 는 문자열을 주고받는다.
2. 그 문자열은 이미지일 수도 있고 (binary) yaml 일 수도 있고, json 일 수도 있고, html 일 수도 있다.
3. body가 무엇인지는 "Content-Type" header가 설명한다.


aerich init -t app.configs.database_settings.TORTOISE_ORM
1. migrate 생성이 된다
2. aerich init-db

Diagram
1. mermaid 를 사용하면 코드를 다이어그램으로 바꿀 수 있다.
2. sequence diagram 을 그릴때는 꼭 autonumber를 활성화 한다.
3. autonumber 를 활성화 하면 모든 화살표에 번호가 자동으로 붙습니다.
4. 화살표 번호를 가지고 개발자들끼리 소통하기가 편리
5. '>>' 꺽쇠를 두번 쓰면 화살표 방향이 보이고, 한 번 쓰면 안 보인다.
6. '-' 한 번 쓰면 실선, 2번 쓰면 점선
7. 실선 = 요청, 점선 = 응답이 관례적 이다.

직렬 요청(응답에 의존할 때)과 병렬 요청
1. 기존 djnago (sync 방식)에서는 쿼리를 하면, 그 쿼리의 결과 돌아올때 까지 서버는 **기다린다.**
2. 기다린다는 것은 곧, 시간을 낭비 한다는 것을 의미 한다.
3. 게시글과 그 게시글의 댓글을 쿼리하는 상황을 가정해보면, django는 두개의 쿼리를 "직렬"로 실행하고 2번 기다린다.
4. 만약에, 게시글과 댓글을 병렬로 쿼리할 수 있다면 대기시간을 줄일 수 있다.(더 효율적이다.)

sync 방식의 문제점
1. latency : 지연 -> 어떤 작업을 수행하는데 걸리는 시간
2. cpu의 latency 는 cycle 로 측정
3. cpu "클럭"(clock) 이 높을 수록 좋다.
4. cpu 1 clock -> 1 cycle
5. L1,L2 -> 3 cycle(엄청 빠름), 14 cycle(빠름) : 빠른 연산
6. disk, network -> 41,000,000(느림), 240,000,000(엄청 느림) : 느린 연산
7. network 호출을 하고, 그 응답이 돌아올때 까지 그냥 기다리는 것은 **매우 비효율적**
8. 기존의 query set -> "Article.objects.get()"은 샌프란시스코에서 도쿄까지 다녀오는 것과 같다.
9. IO = Input, Ouput

병렬요청은 언제 가능할까?
1. 모든 직렬요청을 병렬요청으로 바꿀 수 있는 건 아니다.
2. 직전 응답에 의존하는 경우가 그 예다.

Breadcrumbs
1. 빵조각 -> 헨젤과 그레텔 -> 길찾기 

Structure View
1. pycharm 에서 `Command + 7` 을 누르면 structure view 를 볼 수 있다.
2. structure view 에서는 클래스가 가진 모든 멤버 변수와 메소드가 일목요연하게 정리되어서 보여진다.

diff view 와 edit view (정확한 명칭 아닐 수 있음)
1. commit panel 에서 파일을 클릭하면 기본적으로 diff view 에서 열린다.
2. diff view 의 왼쪽은 수정 전의 파일, 오른쪽은 수정 후의 파일이다.
3. "추가된 라인"은 diff view 에서 초록색
4. "삭제된 라인"은 diff view 에서 파란색
5. diff view 가운데의 '>>' 버튼을 누르면 변경사항을 롤백

poetry lock 의 hash
1. lock 파일이 변경될 때 마다 content-hash 도 같이 바뀐다.
2. content-hash 가 바뀌지 않았다 -> 변경 종속성이 없다.(추가되거나 삭제되지 않았다.)
3. content-hash 가 버뀌었다. -> 새로 poetry install 을 해야한다.
4. github action(CI) 할 때 종속성을 캐싱한다. 캐싱 시 이 hash 를 사용한다.

round trip 및 테스트 tip
1. 한번 요청하고 돌아오는 과정을 round trip 이라 한다.
2. 병렬 요청이 가능한 경우 asyncio.gather() 를 사용해서 network round trip 횟수를 줄인다.
3. http 응답을 json() 으로 변환하기 전에 반드스 200 status_code가 왔는지 "먼저" 검증한다.
    - 500 의 경우에는 반드시 json 으로 응답이 온다는 보장이 없다. nginx 의 default 500 응답은 json이 아니다.
4. 순서가 명시 되어 있지 않은 (보장되어 있지 않은) 경우라면 테스트도 순서에 의존하면 안된다.
    - 순서에 의존하지 않고 검증하는 방법: In 연산 사용하기, 순서 없는 자료구조 사용하기 set()
    - dict 는 순서가 있을까? python 에서 dict 는 순서가 있다. (3.6 버전 부터)

shell 종류
1. sh : 가장 기본 쉘
2. bash : ubuntu 의 기본 쉘
3. zsh : mac 의 기본 쉘

Test Isolation
1. Django 와 Tortoise 가 공통적으로 가지고 있는 특징 (TestCase 를 사용할 때)
2. Test 가 시작되면 새로운 데이터베이스를 생성합니다.
3. 모든 테스트는 새로운 데이터베이스 안에서 이루어진다.
4. 이것을 테스트 공간의 "격리"(isolation)라고 한다.
5. 격리 장점 : 기존 데이터 영향을 받지 않는다.
    - 기존 데이터의 영향을 받는 경우 : 이미 id 가 "comment1" 인 comment 가 존재한다면, 테스트시 Integrityerror 가 발생 (dup)
    - 테스트가 끝나면 모든 데이터를 삭제 한다.

gather 의 특징
1. 시작하자마자 모든 코루틴을 concurrent 하게 실행합니다.
2. 가장 마지막 코루틴 까지 완료될때 까지 block 합니다.
3. 인자로 받은 순서대로 그 결과를 반환합니다.

as_completed 의 특징
1. 시작하자마자 모든 코루틴을 concurrent 하게 실행합니다.
2. gather 와 다르게 for 로 반복할 수 있다.
3. 코루틴이 완료 될때 마다 실행 흐름을 돌려 받습니다. (for 내부를 실행 할 수 있습니다.)
4. 들어온 순서대로 실행되는 것이 아니라, 완료된 순서 대로 실행한다.

변수 이름이 _(언더바 로 시작하는 경우)
1. private : 외부에서 직접 접근 하지 마라 -> _ 언더바 하나
2. public 
3. __언더바 둘, _언더바 하나 차이도 있다.

event loop 의 디테일
1. 이전까지 event loop 는 black box
2. 