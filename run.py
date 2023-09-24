# from app.__init__ import create_app
import app.exchanges.Binance.APIs.config
from app.exchanges.Binance.APIs import base

if __name__ == '__main__':
    # create_app().run(debug=True)
    base.ws.run_forever()
