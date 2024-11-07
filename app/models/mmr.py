from modulefinder import Module

from tortoise import fields

from app.models.base_model import BaseModel


class Mmr(BaseModel, Module):
    user = fields.CharField(max_length=50)
    point = fields.IntField()

    class Meta:
        table = "mmr"
        ordering = ["-point"]
