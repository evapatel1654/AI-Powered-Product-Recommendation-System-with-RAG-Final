from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
from recommendation import RecommendationEngine
from rag_model import RAGModel

app = Flask(__name__)
CORS(app)

# Load data
def load_data(filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'data', filename)
    with open(file_path, 'r') as f:
        return json.load(f)

products = load_data('products.json')
ingredients = load_data('ingredients.json')
sales_data = load_data('sales.json')

# Initialize models
recommendation_engine = RecommendationEngine(products, sales_data)
rag_model = RAGModel(products, ingredients)

@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/api/product/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    
    # Augment product with RAG information
    augmented_product = rag_model.augment_product(product)
    return jsonify(augmented_product)

@app.route('/api/recommendations', methods=['GET'])
def get_recommendations():
    user_query = request.args.get('query', '')
    effect = request.args.get('effect', '')
    
    # Get recommendations
    recommendations = recommendation_engine.get_recommendations(user_query, effect)
    
    # Augment recommendations with RAG
    augmented_recommendations = []
    for rec in recommendations:
        augmented_rec = rag_model.augment_product(rec)
        augmented_recommendations.append(augmented_rec)
    
    return jsonify(augmented_recommendations)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
