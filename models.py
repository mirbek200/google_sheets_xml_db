from peewee import *

db = PostgresqlDatabase(
    'google sheets',
    host='localhost',
    port='5432',
    user='postgres',
    password='123'
)
db.connect()


class BaseModel(Model):
    class Meta:
        database = db


class Data(BaseModel):
    order_number = CharField()
    price_usd = CharField()
    date = CharField(null=True)
    price_ru = IntegerField()

    def __repr__(self):
        return self.title


# db.create_tables([Data])


db.close()
