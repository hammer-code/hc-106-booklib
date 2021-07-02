from booklib import app
from dotenv import load_dotenv

load_dotenv()

if __name__ == 'main':
  app.run(host='0.0.0.0', port='5000')