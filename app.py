from flask import Flask, request, send_from_directory

app = Flask(__name__)

# Home Page

@app.route('/')

def home():

    return send_from_directory('.', 'index.html')


# Index Page

@app.route('/index.html')

def index():

    return send_from_directory('.', 'index.html')


# Designs Page

@app.route('/designs.html')

def designs():

    return send_from_directory('.', 'designs.html')


# Upload Page

@app.route('/upload.html')

def upload():

    return send_from_directory('.', 'upload.html')


# Contact Page

@app.route('/contact.html')

def contact_page():

    return send_from_directory('.', 'contact.html')


# Contact Form Backend

@app.route('/contact', methods=['POST'])

def contact():

    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    print("Name:", name)
    print("Email:", email)
    print("Message:", message)

    return '''
    <script>
    alert("Message Sent Successfully");
    window.history.back();
    </script>
    '''


if __name__ == '__main__':

    app.run(debug=True)