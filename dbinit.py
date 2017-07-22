from models import db, Job

if __name__ == '__main__':
    db.connect()
    db.create_table(Job)
