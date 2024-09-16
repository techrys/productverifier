# 🛡️ Product Authentication System

![Product Authentication Banner](https://via.placeholder.com/1200x300/3498db/FFFFFF?text=Product+Authentication+System)

## 🌟 Features

- **🔐 Product Verification**: Easily verify product authenticity using serial numbers
- **📱 Multi-Mode Scanning**: Support for manual entry, NFC scanning, and camera scanning
- **📝 Product Registration**: Allow users to register their verified products
- **🎨 Sleek UI**: Modern, responsive design using Tailwind CSS
- **⚡ Fast and Interactive**: Powered by Alpine.js for a smooth user experience
- **🚀 Scalable Backend**: Built with Python and Flask for easy expansion

## 🖥️ Tech Stack

- **Frontend**: HTML5, Tailwind CSS, Alpine.js
- **Backend**: Python, Flask, Flask-CORS
- **Icons**: FontAwesome

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- Node.js and npm (for Tailwind CSS)

### Backend Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/product-authentication-system.git
   cd product-authentication-system
   ```

2. Set up a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```
   pip install flask flask-cors
   ```

4. Run the Flask app:
   ```
   python app.py
   ```

### Frontend Setup

1. Open `index.html` in your preferred browser.

2. (Optional) If you want to modify Tailwind CSS:
   ```
   npm install
   npm run build-css
   ```

## 📸 Screenshots

[Verification Page](https://github.com/user-attachments/assets/3d1eca09-0aa4-40fb-aa97-17cd5a6f92f3)

## 🛠️ Configuration

- Update `PRODUCT_CODES_FILE` in `app.py` to point to your secure product codes file.
- Modify API endpoints in `index.html` if your backend is hosted at a different URL.

## 🔒 Security Considerations

- Use HTTPS in production
- Implement rate limiting
- Consider using a database for storing product codes
- Add authentication for admin operations
).

## 📜 License

Distributed under the Apache 2.0 See `LICENSE` for more information.


Project Link: []([https://github.com/yourusername/product-authentication-system](https://github.com/techrys/productverifier))

---

⭐️ Star this repo if you find it useful!
