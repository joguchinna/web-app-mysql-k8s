from flask import Flask, render_template, request, session

app = Flask(__name__)

# Temporarily setting a non-secure session (Not Recommended)
app.config['SESSION_TYPE'] = 'filesystem'
# Do not set a secret_key

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/set_session')
def set_session():
    session['user'] = 'John Doe'  # Store user info in the session
    return "Session set"

@app.route('/get_session')
def get_session():
    return f"Session value: {session.get('user')}"

if __name__ == '__main__':
    app.run(debug=True)
