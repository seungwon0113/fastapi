from tortoise import fields


class BaseModel:
    id = fields.CharField(pk=True, max_length=40)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)
