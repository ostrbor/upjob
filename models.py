from peewee import (SqliteDatabase, Model, CharField, DateTimeField,
                    IntegerField)

db = SqliteDatabase('jobs.db')


class Job(Model):
    job_id = CharField()
    title = CharField()

    description = CharField()
    budget = IntegerField()
    created = DateTimeField()

    class Meta:
        database = db

    def to_text(self):
        title = self.title
        description = self.description
        budget = self.budget + ' :dollar:'
        created = self.created
        return '*%s*\n%s\n%s\n_%s_\n' % (title, budget, description, created)
