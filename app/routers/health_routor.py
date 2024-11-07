from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/vi/health", tags=["헬스체크"])
"""
    dto : data transfer object
    데이터"만" 담고 있는 객체 입니다. (데이터를 변형도 한다면 dto 가 아님)
    (parsing 까지는 봐주는 경우가 있긴 함 .. e.g.)
"""


class OkResponse(BaseModel):
    ok: bool
    extra_msg: str | None = None


@router.post("", response_model=OkResponse)
async def health() -> OkResponse:
    return OkResponse(ok=True)
