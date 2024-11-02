import asyncio

from httpx import AsyncClient
from tortoise.contrib.test import TestCase

from app.models.article import Article
from app.models.comment import Comment
from main import app


class TestArticleRouter(TestCase):
    async def test_get_article_and_comment(self) -> None:
        # given
        article_id = "test_article"
        article = await Article.create(
            id=article_id, author="author", title="title", body="body"
        )
        await asyncio.gather(
            Comment.create(
                id="comment1", article=article, author="c1_author", body="c1_content"
            ),
            Comment.create(
                id="comment2", article=article, author="c2_author", body="c2_content"
            ),
        )

        # When
        # 기존에 동기 방식으로  http 요청을 할때는 requests 를 사용 했다면
        # 비동기 방식으로 httpx 요청을 하고 싶다면 httpx 를 사용한다.

        # httpx.AsyncClient(app=app) async client 에 app 을 전달하면
        # asgi app 에 바로 요청을 할 수 있는 client 가 생성된다.
        async with AsyncClient(app=app, base_url="http://test") as ac:

            # app 을 전달해서 AsyncClient 를 만들었기 때문에
            # url 의 scheme 이나 host 를 전달할 필요 없이 바로 경로만 적으면 된다.
            # url 은 어떻게 만들어 졌는가
            #       -> article_router.py 의 router 의 prefix + router.get() 의 경로
            response = await ac.get(
                url=f"/v1/articles/{article_id}",
                headers={"Accept": "application/json"},
            )

        # Then
        # status code 가 200 임을 먼저 검증했고, 그 다음에 json() 으로 변환한다.
        # 이 순서를 반드시 지키는게 좋다
        # http 는 json 을 주고받는 protocol 이 아니다.
        # http 는 "문자열" 주고 받는 protocol 입니다. (TCP 연결 위에서)

        # 에러 같은거..? json 으로 변환하려고 시도하면 decode 에러가 발생
        # Client - nginx -> uvicorn -> fastapi
        self.assertEqual(response.status_code, 200)
        response_body = response.json()
        self.assertEqual(response_body["id"], article_id)
        self.assertEqual(response_body["author"], "author")
        self.assertEqual(response_body["title"], "title")
        self.assertEqual(response_body["body"], "body")

        # 보장되지 않는 순서에 의존하는 경우
        # 간헐적으로 터지는 테스트가 만들어진다.
        # Ci 의 결과에 의해서 배포 여부가 결정 -> CI 가 간헐적으로 실패 -> 배포자가 CI 를 못 믿게 된다.
        self.assertEqual(len(response_body["comments"]), 2)
        self.assertEqual(response_body["comments"][0]["id"], "comment1")
        self.assertEqual(response_body["comments"][0]["author"], "c1_author")
        self.assertEqual(response_body["comments"][0]["body"], "c1_content")

        self.assertEqual(response_body["comments"][1]["id"], "comment2")
        self.assertEqual(response_body["comments"][1]["author"], "c2_author")
        self.assertEqual(response_body["comments"][1]["body"], "c2_content")

        # 그렇다면 순서와 상관없이 검증하려면? -> set()
        # 핵심은 : In 연산을 이용
        # set 안에 내가 원하는 id 가 있는지 assertIn 으로 검증
        id_set = {comment["id"] for comment in response_body["comments"]}
        self.assertIn("comment1", id_set)
        self.assertIn("comment2", id_set)

        # dict 를 쓰는 방법
        # comprehension 으로 dict 를 만든 후
        # dict 에서 원하는 comment 를 뽑아온 후
        # comment 안의 멤버(author 와 body)를 검증
        comment_dict = {comment["id"]: comment for comment in response_body["comments"]}
        result_comment1 = comment_dict["comment1"]
        self.assertEqual(result_comment1["author"], "c1_author")
        self.assertEqual(result_comment1["body"], "c1_content")

        result_comment2 = comment_dict["comment2"]
        self.assertEqual(result_comment2["author"], "c2_author")
        self.assertEqual(result_comment2["body"], "c2_content")
