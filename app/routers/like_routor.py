from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/vi/like", tags=["좋아요"])
"""
    dto : data transfer object
    데이터"만" 담고 있는 객체 입니다. (데이터를 변형도 한다면 dto 가 아님)
    (parsing 까지는 봐주는 경우가 있긴 함 .. e.g.)
"""


class LikeRequset(BaseModel):
    id: int
    article_id: int


class LikeResponse(BaseModel):
    id: int
    article_id: int


@router.post("", response_model=LikeResponse)
async def do_lile(like_request: LikeRequset) -> LikeResponse:
    return LikeResponse(id=1, article_id=like_request.article_id)
