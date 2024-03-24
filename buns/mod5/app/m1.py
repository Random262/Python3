import os
import signal
from subprocess import Popen, PIPE
from flask import Flask


def start_server(port):
    global cou
    process = Popen(['lsof', '-ti', f':{port}'], stdout=PIPE)
    outs = process.communicate()[0]
    if outs:
        pids = [int(x) for x in outs.decode('utf-8').split('\n')]
        print(f'Killing process(es) with pid {pids}')
        for pid in pids:
            os.kill(pid, signal.SIGTERM)
        cou += len(pids)
        start_server(port)
    else:
        print(f'Starting server')
        app = Flask(__name__)

        @app.route('/')
        def hello():
            return f'Your server killed {cou} processes'

        app.run(port=port)


if __name__ == '__main__':
    cou = 0
    start_server(5000)
