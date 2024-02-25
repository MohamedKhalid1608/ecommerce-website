# Flask E-commerce API

This is a simple Flask-based backend API for a basic e-commerce platform. It demonstrates RESTful API development and database integration.

## Setup

1. Clone the repository

2. Navigate to the project directory

3. Install dependencies

4. Set up the database:
- Make sure you have MySQL installed and running.
- Create a MySQL database named karkhana.db.
- Update the database configuration in `config.py` if needed.

5. Run migrations to create the necessary tables
  
6. Start the Flask development server


## API Endpoints

- `GET /products`: Returns a list of all products.
- `GET /products/<id>`: Returns details of a specific product.
- `POST /cart`: Adds a product to the cart.
- `GET /cart`: Retrieves the cart items.
- `DELETE /cart/<id>`: Removes a specific item from the cart.

## Usage

- Use an API testing tool like Postman to interact with the API endpoints.
- Send requests to the appropriate endpoints with the required parameters.
- For example:
- To retrieve all products: `GET http://127.0.0.1:5000/products`
- To add a product to the cart: `POST http://127.0.0.1:5000/cart` with JSON payload containing product_id and quantity.

