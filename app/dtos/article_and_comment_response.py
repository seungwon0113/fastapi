from pydantic import BaseModel


class CommentResponse(BaseModel):
    """
    Response dto 를 생성
    Response dto 는 결과 json 에 어떤 값이 들어가지 결정
    댓글이 가지고 있는 많은 컬럼들 중에서
    - 댓글의 id
    - 댓글의 작성자
    - 댓글의 본문
    위 세개의 컬럼을 클라이언트에게 전달해 준다.

    fastapi는 Response dto 를 보고
    Response spec 을 자동으로 생성(자동으로 swagger가 만들어진다.)
    """

    id: str
    author: str
    body: str


class ArticleAndCommentsResponse(BaseModel):
    """
    게시글과 댓글을 모두 담는 dto 를 생성
    dto -> Data transfer objects -> 정보를 담고 있는 객체
    -> 정보를 수정한다면 dto 가 아니다. 담고만 있어야 dto 다.

    함수가 dict 를 리턴하도록 하지않는다.(99.9% 상황으로 dict 대신 dto 사용 가능)

    don't:
        return {"abc" : "def"}

    do:
        return MyDto(abc = "def")
    """

    id: str
    author: str
    title: str
    body: str

    # list 의 type annotation 을 작성할 때에는 list[CommentResponse] 이렇게 했을 테지만,
    # tuple 의 경우는 type annotation 이 "길이"도 지정한다.
    # 길이를 모르는 경우 아래와 같이 ',...' 을 사용한다.
    # 의미는, CommentResponse 가 담긴 튜플인데, 길이는 가변적 이다.
    # 리스트 말고 튜블을 쓰는 이유 : 튜플은 immutable(한 번 생성되고 나면, 변하지 않는다.)
    comments: tuple[CommentResponse, ...]
