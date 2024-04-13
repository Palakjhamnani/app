from flask import Flask, render_template
import time

app = Flask(__name__)

@app.route('/')
def home():
    # Simulate a delay (e.g., 3 seconds) before rendering the main page
    time.sleep(3)
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
