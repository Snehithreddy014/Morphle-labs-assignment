from flask import Flask
import os
import time
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Snehith Siddharth"
    username = os.getenv('USER', 'default_user')  # Fallback if getlogin() fails
    server_time_ist = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time() + 19800))  # IST is UTC+5:30

    # Try to get the top command output
    try:
        top_output = subprocess.getoutput('top -b -n 1')
    except Exception as e:
        top_output = f"Error retrieving top output: {str(e)}"

    # Prepare the HTML response
    html = f"""
    <h1>System Info</h1>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {server_time_ist}</p>
    <h2>Top Output:</h2>
    <pre>{top_output}</pre>
    """
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
