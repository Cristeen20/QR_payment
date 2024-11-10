from flask import Flask, render_template, redirect, url_for,request

##import stripe

app = Flask(__name__)

# Set up Stripe API key
#stripe.api_key = 'your-stripe-secret-key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pay', methods=['POST','GET'])
def pay():
    try:
        # Create a PaymentIntent to manage the payment
        amount = request.args.get('amount')
        order_id = request.args.get('orderId')
        customer_id = request.args.get('customer_id')


        # Redirect the user to the payment confirmation page
        return render_template('pay.html', amount=amount, order_id=order_id, customer_id=customer_id)

    except Exception as e:
        return str(e)

# Route to simulate payment success
@app.route('/payment-success', methods=['GET'])
def payment_success():
    # Generate a random token (for demonstration purposes)

    # Pass the generated token to the success page
    return render_template('payment_success.html')

# Route to generate a payment token
@app.route('/nft-token', methods=['POST','GET'])
def generate_token():
    # You could use a real payment API here to generate a token
    # For this example, we generate a random token

    
    return render_template('nft.html')

if __name__ == '__main__':
    app.run(debug=True)
