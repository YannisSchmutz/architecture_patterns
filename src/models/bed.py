from tortoise import fields
from tortoise.models import Model

from tortoise.contrib.pydantic import pydantic_model_creator


class Bed(Model):
    id = fields.IntField(pk=True)

    # FK adds automatically the "_id" to the field
    room = fields.ForeignKeyField(
        "hostel.Room",
        related_name="beds",
        description="The Room this bed belongs to",
    )

    def __str__(self):
        return f"Bed_{self.id}"


Bed_pydantic = pydantic_model_creator(Bed)
