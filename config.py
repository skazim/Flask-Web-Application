import os 
basedir= os.path.abspath(os.path.dirname(__file__))
class Config(object):
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
  # SQLALCHEMY_DATABASE_URI takes location of database from SQLALCHEMY_DATABASE_URI config extension
  # this is fallback value of the env not available and falls basck to default
  # here configuring database named app.db which is in basedir
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'myapp.db')

  # signal the database about the change to be made, here false i.e we donot need
  SQLALCHEMY_TRACK_MODIFICATIONS= False

  MAIL_SERVER= os.environ.get('MAIL_SERVER')
  MAIL_PORT =int(os.environ.get('MAIL_POST') or 25)
  MAIL_USER_TLS = os.environ.get("MAIL_USER_TLS") is not None
  MAIL_USERNAME= os.environ.get('MAIL_USERNAME')
  MAIL_PASSWORD= os.environ.get('MAIL_PASSWORD')
  ADMINS = ['kazimmuhammad10@gmail.com']
