from dotenv import load_dotenv
from booklib.main import create_app

load_dotenv()
app = create_app()

if __name__ == "main":
    app.run(host="0.0.0.0", port="5000")
