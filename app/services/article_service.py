import asyncio

from app.dtos.article_and_comment_response import (ArticleAndCommentsResponse,
                                                   CommentResponse)
from app.models.article import Article
from app.models.comment import Comment


async def service_get_article_and_comments(
    article_id: str,
) -> ArticleAndCommentsResponse:
    """

    await:
        - 비동기 호출을 한다. (async def 로 시작하는 함수를 호출한다.)
        - 이벤트 루프에게 이 함수를 호출해 달라고 등록한다.
        - 만약 db 호출이라면 결과가 완료되기 까지 기다리는 것을 의미 한다.

    이벤트 루프 : 여러가지 비동기 함수들을 실행해 주는 친구. (무한 루프)

    parallel 과 concurrent 차이:
        - 은행에 가서 통장도 만들고, 치킨집에서 치킨 포장도 하고, 마트에서 우유도 사야한다.
        - 총 3개의 task 존재.

        parallel 의 경우:
            - 사람 3명이 각각 역할 수행한다.
            - task 가 병렬로 실행

        concurrent 의 경우
            - 1명이 은행에 먼저가서 번호표 뽑고
            - 치킨집 가서 주문하고
            - 마트 가서 우유 사고
            - 치킨집 포장받고
            - 은행가서 통장만들고
            - 귀가

        - 더 적은 자원으로 여러 개의 task 를 수행할 수 있는것은 -> concurrent
        - 하지만 마트에서 뭔가 사고가 나서 우유를 사는데 지연이 되었다면 (마트에 갇혔다...?)
        - 치킨과 은행 task 도 함께 지연된다.


        - parallel 은 사람이 진짜 3명이기 때문에 마트에 갇히는 일이 발생해도 치킨과 은행은 영향을 받지 않는다.
        - 사람 -> cpu core 를 말합니다. (혹은 process 를 얘기한다고도 볼 수 있다.)
        - task 는 IO 요청을 말합니다. (데이터베이스 호출, http 호출)
        - 은행, 치킨집, 마트 등은 IO 요청을 받아들이는 주체입니다. (데이터베이스, 외부 서버)

    asyncio.gather():
        - 비동기 호출을 "Concurrent" 하게 진행하는 2가지 방법중 하나 입니다.
        - gather(), as_completed() 가 있다.
        - gather() 를 호출할 때는 다수의 코루틴을 전달합니다.
        - 모든 코루틴이 실행완료 됬을 때 까지 대기한 후, 다 되었다면 순서대로 반환합니다.
    """

    # 직렬
    # article = await Article.get_one_by_id(article_id)
    # comments = await Comment.get_all_by_article_id(article_id)

    article, comments = await asyncio.gather(
        Article.get_one_by_id(article_id), Comment.get_all_by_article_id(article_id)
    )

    return ArticleAndCommentsResponse(
        id=article_id,
        author=article.author,
        title=article.title,
        body=article.body,
        comments=tuple(
            CommentResponse(id=comment.id, author=comment.author, body=comment.body)
            for comment in comments
        ),
    )
