import sys
import threading

from tests.webserver import app

import logging

log = logging.getLogger('werkzeug')
log.disabled = True

def flaskserver():
    app.run(host='127.0.0.1', port=5000, debug=False)


th = threading.Thread(target=flaskserver, args=(), daemon=True)
th.start()

sys.path.append("../pyourls3")
