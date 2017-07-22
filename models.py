from peewee import (SqliteDatabase, Model, CharField, DateTimeField,
                    IntegerField)
from settings import DB_FILE

db = SqliteDatabase(DB_FILE)


class Job(Model):
    job_id = CharField()
    title = CharField()
    description = CharField()
    budget = IntegerField()
    created = DateTimeField()

    class Meta:
        database = db

    def to_text(self):
        if self.budget:
            title = f'{self.title} ({self.budget}$)'
        else:
            title = self.title
        description = self.description
        created = self.created
        return f'*{title}*\n{description}\n_{created}_\n' + '-' * 10
