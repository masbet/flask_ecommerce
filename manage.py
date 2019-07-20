from flask_migrate import MigrateCommand
from app import migrate, app
from app.models import models
from flask_script import Manager

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__=='__main__':
    manager.run()