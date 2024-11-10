from flask import Flask, render_template, request, send_file
import qrcode
import os

app = Flask(__name__)

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route to generate QR code
@app.route('/generate_qr', methods=['POST'])
def generate_qr():

    bill_details = {
    "order_id": "12345",
    "total_amount": "20",
    "customer_id":"11209890"
    }
    url= f"http://127.0.0.1:5000/pay?amount={bill_details['total_amount']}&orderId={bill_details['order_id']}&customer_id={bill_details['customer_id']}"
    

    qr = qrcode.make(url)

    # Save the QR code image
    qr_path = os.path.join('static', 'qr.png')
    qr.save(qr_path)

    return render_template('index.html', qr_image=qr_path,bill=bill_details)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True,port=8000)
