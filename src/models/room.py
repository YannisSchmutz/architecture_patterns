from tortoise import fields
from tortoise.models import Model

from tortoise.contrib.pydantic import pydantic_model_creator


class Room(Model):
    id = fields.IntField(pk=True)
    number = fields.IntField()
    floor = fields.IntField()

    def __str__(self):
        return f"Room #{self.number} at floor #{self.floor}"


Room_pydantic = pydantic_model_creator(Room)
