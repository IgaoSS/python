# pylint: disable=C0114,C0115,C0116,W0703,C0209,E0015,C0304,C0321
from src.main.server.server import app

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)