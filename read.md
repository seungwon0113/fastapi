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

스크래치 파일 만드는 단축키
commend + shift + n
현재 line 을 duplicate : commend + D

제너레이터
1. 제너레이터는 "일시정지가 가능한 함수"
2. 함수안에 yield 가 포함되는 순간 함수는 제너레이터로 변한다.
3. 함수는 호출을 하면 그 내부의 코드가 바로 실행되지만, 제너레이터는 그렇지 않다.
    - 대신 제너레이터 객체 반환된다.
4. 제너레이터 객체를 실행하는 방법
    - for 문을 사용하는 방법
    - 내장 함수 next() 를 사용하는 방법
      - next() 는 yield 를 다시 만나기 전까지 제너레이터를 실행한 후에
      - yield 를 만났다면 함수를 다시 일시정지 하고 빠져 나온다.
      - 내장 함수 next() 는 제너레이터 객체의 __next__()
5. 제너레이터는 2번 회전(반복) 할 수 없다.
    - 전부 소진된 iterator 에 다시 한번 next() 를 호출하면
      (소진되었다 -> 마지막 yield 까지 실행 되었다.) StopIteration 에러가 발생
    - for 문은 반복을 계속 하다가 StopIteration 에러가 발생하면 for문을 빠져 나온다.
    - generator 는 함수가 실행되고 있는 환경을 그대로 저장한 상태로 함수를 "일시정지" 시킵니다.
    - 따라서 일시정지 할 때 함수의 local 변수도 그대로 저장되어 있으며, 
    - 다시 함수를 실행할 때 local 변수를 그대로 사용할 수 있습니다.

deque 자료구조란?
1. double ended queue
2. double ended -> 끝이 양쪽이 있다.
3. 원랴 queue 는 입구와 출구가 정해져 있다.
4. 양쪽 끝을 전부 입구와 출구로 쓸수 있다.
5. python 에서 일반적인 queue 를 사용할 때 deque 를 쓴다.(heapq 모듈에 필요한 기능이 없는 경우)

deque 룰렛 구현의 불편함
1. rullet() 함수 외부에 과거 당첨 금액을 저장해두어야 한다는 불편함

Debug 중 실행 흐름의 컨트롤
1. Resume Program: 다음 중단점 까지 계속 실행
2. Step Over: 한 줄 실행
3. Step Into: 다음 실행하는 함수 내부로 들어간다.
4. Step Out: 함수 외부로 빠져 나온다.

쓰레드
1. 쓰레드를 추가하면 실행흐름이 하나 더 추가된다.

event loop internal
1. event loop 내부에는 deque 인 _ready 와 heop 인 scheduled 가 있다.
2. event loop 는 한번 run 할 때 마다 (_run_once 라는 함수가 실제로 내부에 있음) 다음을 수행한다.
    - scheduled 에 있는 코루틴 중에서 지금 실행 가능한 코루틴을 _ready deque 에 밀어 넣는다.
    - _ready 안의 모든 코루틴을 순차적으로 실행한다. (여기서 랜덤 없음! 순차 실행임)
    - _ready 안의 코루틴을 실행 했다면 실행흐름은 이벤트 루프에서 -> 코루틴으로 이동한다.
    - 코루틴 안에서 await 을 만나면 (실행 되고 있던 코루틴은 중지 되고) 다시 이벤트 루프로 실행흐름이 이동한다.

미래를 위해 남기는 말
- 여태까지 "코루틴" 이란 말을 쓰긴 했지만 엄밀히 말하면 Task 입니다. (Task 는 Future 의 sub class 입니다.)
- 사실은 gather() 를 호출하면 인자로 받은 모든 코루틴은 task 에 감싸진다.
- 실제로는 await 할 때 task 를 await 할 때만 실행흐름이 이벤트루프로 이동합니다. (그냥 일반 코루틴은 이벤트 루프로 실행 흐름이 전환하지 않는다.)

Swagger 문서 자동 생성
1. 클라이언트 개발자의와 협력할 때에 API Spec 문서는 선택이 아니라 필수 입니다.
2. swagger 문서 접근 방법 FastAPI 에서 default 경로는 "/docs" 입니다.
3. swagger tag 
    -API 가 많을 때 tag 를 사용해서 분류할 수 있다.
4. Http method 바꾸기
   - @router.<http method> 에서 method 를 바꾸면된다.
5. response spec 보여주기 (가장 중요!)
6. 스펙문서와 실제 코드의 실행결과는 "항상" 일치 해야한다.
    - 불일치 한다면, 문서를 읽는 사람이 문서를 불신하게 된다.
    - 이 문제를 최소화 하기 위해서 손으로 문서를 쓰지 않고, 코드로 문서를 생성한다.
7. 일치하게 만드는 방법
   - pydantic 의 base model 을 상속하는 dto class 를 만든다.
   - path operation function 을 등록 할때 response_model을 전달한다. (1번을 전달한다.)
   - path operation function 도 해당 dto 를 리턴한다.
8. 필수값과 비 필수값, Nullable
    - key 가 있을 수도 있고 없을 수도 있다. -> NotRequired
    - key 가 무조건 있긴 한데, null 일 수 있다. -> nullable (선호)
9. Schemas
   - sawgger 제일 하단에 모든 spec 이 모여 있다.

클라이언트 개발자와 협업 하는 방법
0. (백엔드 프론트 모두다) 모든 팀원들끼리 상의해서 spec 을 먼저 정한다.
1. Dto 와 path operation function 만 먼저 만든다
2. path operation function 은 dummy dto 를 리턴합니다. dto 안의 값은 임의의 값으로 채우세요
3. mypy 통과하는지 확인
4. 클라이언트 개발자는 스펙문서를 보고 개발을 시작하고, 백엔드 개발자도 클라이언트가 개발하는 동안 내부의 기능을 채워 넣습니다.

http 기본 구조
1. http 요청은 다음 요소로 구성된 단순 문자열이다.
    - http version (보통 1.1)
    - http verb (혹은 method) (예: GET(조회), POST(생성), PUT(수정), DELETE(삭제), PATCH(수정))

테스트 크기에 관하여
1. 지금까지 만든 테스트... (when 절이 다르다.)
   - 서비스의 테스트: 서비스는 단순 함수 (plain function). 호출하는 것 만으로 테스트 가능
   - 라우터의 테스트: url 을 거쳐서 실제로 API 를 호출하는 테스트.
2. coverage: 테스트 슈트를 수행하는 중에 1번 이라도 실행된 제품 코드 / 전체 제품 코드
3. 라우터 테스트의 커버리지가 높은 이유: 서비스 코드 + 라우터 코드 (분자)가 실행되기 때문에 

e2e 테스트와 unit test (같은 용어라도 상황에 따라 의미가 다를 수도 있음)
1. end to end 테스트: 직접 api 호출 하는 테스트
2. e2e 테스트를 선호하는 이유: "유저에 집중하면 나머지 것을은 따라온다"
   - "유저 입장에서는 공개되어있는 api 를 호출하는 것이 서버의 기능을 이용 할수 있는 유일한 방법"
   - 서버내의 클래스나 서버 안의 작은 함수를 직접 호출 할수 있는 방법은 없다.
   
3. e2e 의 단점: 살제로 테스트가 터졌을때 어디서 터진지 알기 어렵다.
   - e2e 테스트는 테스트가 커버하는 코드의 양이 많기 때문에 에러가 발생했을때 "용의선상"에 오르는 코드도 많다.
   - unit test 에 비해서 조사해야 하는 코드의 양이 많다. -> 고치는 시간이 오래걸린다.
   - 간헐적으로 실패하는 테스트가 생겼을 때, 원인 찾기가 상대적으로(unit 에 비해) 어렵다.

4. (간헐적 말고) 시한 폭탄 처럼 터지는 테스트
5. 시간을 멈추고 테스트 하고 싶은 요구사항도 종종 만난다.
6. 날짜와 관련된 연산을 해야되는데, 윤년을 끼고도 정상동작하는지 검증하고 싶다. 윤년의 2월로 날짜를 고정 해야한다.
   -https://github.com/spulec/freezegun : 이럴때 freezegun 이 빛을 발한다.
7. freeze_time 빼먹고 테스트를 만들면 "시한 폭탄 테스트" 가 만들어진다.

피드백 루프
1. 개발 시작 할때 마다. './test.sh' 전체 테스트를 수행한다.
2. 올바른 피드백 루프는, 빠르고 믿을 수 있고, 실패한 지점을 바로 알 수 있다.

단위 테스트
1. service 함수를 직접 호출한 것, (하나의 클래스, 하나의 메소드를 검증하는 테스트)
2. 단위테스트는 위의 "올바른 피드백 루프"의 조건을 만족한다.

테스트 피라미드
1. Unit > Integration > e2e : 작은 테스트의 개수가 많아야되고, 범위가 넓은 테스트는 적어야 한다.

현재 e2e 를 더 선호하게 된 이유
1. 구글링 테스팅 블로그에서 unit test 를 더 많이 작성하라 했음에도 불구하고 e2e 를 더 선호 하게된 이유
2. routor 에서 validation 을 한다고 했을 때, service 에는 validation 을 거친 데이터만 들어가게 된다.
   - 하지만 단위 테스트에서 routor 를 bypass 하고 service() 를 직접 호춯하는 경우에는 validation 을 실패하는 데이터도 넣을 수 있다.
   - 테스트를 작성하지 않은 다른 동료 개발자는 "잘못된 데이터" (given 절) 을 보고 혼란을 느끼게 된다.
   - 처음부터 routor 를 반드시 거치도록 개발을 했다면 잘못된 given 절을 가진 테스트를 만들 수 없다.

3. 가장 외부의 인터페이스 (api) 에 의존 하므로, 내부의 서비스나 모델에 변화가 있더라도 상대적으로 적게 변한다.(테스트 수정할 일이 적어진다.)

예제 validation
'''python 
      for stop_word in ("!", "#", "@", ":", ";"):
        if stop_word in article_id:
            raise HTTPException(
                status_code=400,
                detail=f"특수 문자는 허용되지 않습니다만, 특수문자{stop_word}가 들어있습니다.",
            )'''

property-based testing
1. https://hypothesis.readthedocs.io/en/latest/
2. property based 는 (엣지 케이스를 포함한) given 절을 우리를 대신해서 만들어 준다.
3. (일정한 규칙을 가지는) 무작위 입력을 테스트 대상에 넣고, 테스트한다.

왜 트랜젝션이 필요한가?
1. 일반적인 결제 프로세스
2. 사용자가 주문하고 결제를 완료 했다면 ...
   - 재고 1 감소
   - (보통 실제 금원 출금은 PG 에서 일어난다.) (PG 는 Payment Gateway, inicis, naver, kakao)
   - 결제 내역 insert

3. 만약 재고 1감수 후에 서버가 강제 종료 된다면? -> 재고만 감소
    - 이문제를 해결하려면
    - 로그를 전부 뒤진다
    - 실제 창고를 전부 뒤진다
    - 모두다 힘들고, 비용 (인건비 포함)이 많이 드는 작업

4. 트랜젝션을 사용한다면
   - 모든 요청이 전부 성공하거나, 아니면 그 중 하나라도 실패했다면 모든 요청이 마치 없없던 것처럼 만들 수 있다.
   - 원자성 (Atomicity)

여담 이니시스 쓰지말자
  - inicis -> 장애 나도 전화 안받음
  - PG 는 어디서 수익을 낼까? 수수료 -> 수수료를 내는 (이커머스)회사가 중요한 고객
  - PG 비상 연락망?
  - PG 계약을 맺었다면 함부로 결제수단을 비노출 시키면 안되는데..
  - 장애가 났다면 결제수단을 비노출 해야함.
  - KCP, naver, kakao, toss

트랜젝션 예제
USE oz_fastapi;
SELECT * FROM articles;
SELECT * FROM comments;

BEGIN; # 트랜젝션을 시작하겠다
INSERT INTO articles(id, author, title, body)
VALUES ('test_id', 'test_author', 'test_title', 'test_body');
# commit 되지않은 변경사항은, 다른 커넥션에게 보이지 않는다.
INSERT INTO comments(id, author, body, article_id)
VALUES ('test_comment_id','test_author','test_content','test_id')

ROLLBACK; # 트랜젝션을 취소시킨다. 지금까지의 변경사항을 없었던 것처럼 한다.

COMMIT; # 트랜젝션을 완료시킨다. 모든 변경사항을 실제로 데이터베이스에 적용한다.
# commit 이 성공한 이후에는 다른 커넥션에서도 변경사항이 보인다.

DELETE FROM articles WHERE  id = 'test_id';
DELETE FROM comments WHERE  id = 'test_comment_id';

- begin 에서 commit 까지가 하나의 트랜젝션

트랜젝션 격리 수준
1. 앞서 트랜젝션을 직접 해보았는데, 커밋되지 않은 변경 사항은 다른 커넥션에서는 보이지 않았다.
2. 이 behavior 는 격리 수준에 따라 다르다.
3. mysql innodb 는 4개의 격리 수준을 가지고 있다.

    - READ UNCOMMITED
    - READ COMMITED
    - REPETABLE READ
    - SERIALIZABLE

4. read uncommited 처럼 격리수준이 낮을 때에는 Phantom Read 와 같은 현상이 발생한다.
   - A, B 커넥션이 있고 B 커넥션에서 A 의 변경사항을 조회 했는데, A가 롤백해 버리는 경우 B는 갑자기 안보이게 된다.
5. 결론 -> 격리수준은 REPETABLE READ 이상으로 쓰자 (default)

트랜젝션의 관리
1. 트랜젝션이 너무 빈번하게 일어나면 -> disk io 가 많아짐 -> 부하가 커진다.
2. 트랜젝션이 너무 길어지면 -> dead lock 의 위험성이 증가한다.
    - 결론 : 트랜젝션을 적당한 시간에 끝나도록 하는게 좋다.

3. mysql 의 innodb 엔진을 사용하는 경우 -> 모든 쿼리는 트랜젝션 안에서 실행된다. (쿼리가 하나일 지라도)
4. django 의 default 설정은 auto commit 이다.
   - auto commit 은 각 쿼리를 쿼리가 실행되자마자 바로 커밋한다.
   - 단 transaction 이 활성화 되지 않을 경우에만 auto commit 한다.
   - django : https://docs.djangoproject.com/en/5.1/topics/db/transactions/
   - tortoise : https://tortoise.github.io/transactions.html

gunicorn 간단한 소개
1. https://gunicorn.org/
2. 

FastAPI 는 정말 빠른가? 증명
1. WSGI: Web Server Gateway Interface -> 웹서버랑(gunicorn) 파이선 프레임 워크(django, fastapi) 사이를 이어주는 인터페이스
   - async WSGI 를 ASGI 라고 한다. (uvicorn)
   - XSGI 양식을 지켜서 프에임워크를 만들어서 gunicorn, uvicorn 등이랑 소통이 가능하다.
2. UNIX: Linux 의 할아버지, unix 에서 돌아간다는 말은, window 에서 안돌아간다
3. pre-fork worker model: 
4. port 를 listen 한다는 의미 -> 내가 포트 8000을 사용하고 싶다. (내가 이 포트를 사용해서 요청을 받겠다.) 운영 체제에게 요청하는 말
   - 운영체제는 거절할 수도, 승낙할 수도 있다.
   - 다른 프로세스가 이미 해당 포트를 listen 하고 있을 경우 운영체제는 거절한다.
   - 만약에 쓰이고 있지 않다면 승낙하고, 포트 8000에 bind 된다.

5. fork 의 의미 -> bind 에 성공한 후에 master 프로세스는 스스로 복제해서 (이 복제를 fork 라고 한다.) worker process 를 생성한다.
   - 실제 요청을 받아들이고 응답을 만들어내는 것을 worker process 입니다.

6. master 가 하는 일: worker 가 알 수 없는 이유로 죽었을 때 새로 만듭니다. 혹은, 어떤 시그널을 받아서 의도적 재시작 합니다.