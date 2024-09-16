@app.route('/verify', methods=['POST'])
def verify_product():
    data = request.json
    product_code = data.get('product_code')
    
    if not product_code:
        return jsonify({'error': 'No product code provided'}), 400
    
    valid_codes = load_product_codes()
    
    if product_code in valid_codes:
        return jsonify({'verified': True, 'message': 'Product verified successfully!'})
    else:
        return jsonify({'verified': False, 'message': 'Invalid product code.'})

@app.route('/register', methods=['POST'])
def register_product():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    product_code = data.get('product_code')
    
    if not all([name, email, product_code]):
        return jsonify({'error': 'Missing required information'}), 400
    
    # In a real-world scenario, you'd save this information to a database
    # For this example, we'll just return a success message
    return jsonify({'success': True, 'message': 'Product registered successfully!'})

if __name__ == '__main__':
    app.run(debug=True)
