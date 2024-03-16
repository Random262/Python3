import subprocess
from flask import Flask, request

app = Flask(__name__)


def get_sys_uptime():
    result = subprocess.run(['uptime', '-p'], capture_output=True, text=True)
    uptime = result.stdout[3:]
    return uptime


@app.route('/uptime', methods=['GET'])
def sys_uptime():
    uptime = get_sys_uptime()
    return f"Current uptime is {uptime}"


if __name__ == '__main__':
    app.run(debug=True)
