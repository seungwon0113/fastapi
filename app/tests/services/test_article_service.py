from tortoise.contrib.test import TestCase

from app.models.article import Article
from app.services.article_service import service_get_article_and_comments

# Django 랑 똑같이 TestCase 를 import 한다.
# 단, django 가 아닌 tortoise orm 에서 가져온다.


class TestArticleService(TestCase):
    async def test_get_articles_and_comments(self) -> None:
        """
        := -> wallus operator (바타코끼리 연산자)
        """
        # Given
        # 테스트에 필요한 재료를 준비한다.
        article_id = "test_article"
        article = await Article.create(
            id=article_id, author="author", title="title", body="body"
        )

        # When
        article_and_comment = await service_get_article_and_comments(article_id)

        # then
        self.assertEqual(article_and_comment.id, article.id)
        self.assertEqual(article_and_comment.author, "author")
        self.assertEqual(article_and_comment.title, "title")
        self.assertEqual(article_and_comment.body, "body")
