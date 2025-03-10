from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class RecommendationEngine:
    def __init__(self, products, sales_data):
        self.products = products
        self.sales_data = sales_data
        
        # Initialize sentence transformer model for semantic similarity
        self.model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
        
        # Pre-compute product embeddings
        self.product_embeddings = self._compute_product_embeddings()
        
        # Calculate popularity scores
        self.popularity_scores = self._calculate_popularity_scores()
    
    def _compute_product_embeddings(self):
        """Compute embeddings for all products"""
        texts = []
        for product in self.products:
            # Create a rich text representation of the product
            text = f"{product['name']} {product['description']} {' '.join(product['effects'])} {' '.join(product['ingredients'])}"
            texts.append(text)
        
        # Return embeddings
        return self.model.encode(texts)
    
    def _calculate_popularity_scores(self):
        """Calculate popularity scores based on sales data"""
        popularity = {}
        
        for product in self.products:
            product_id = product['id']
            # Default score based on product data
            score = product['sales_data']['units_sold'] / 100  # Normalize
            
            # Find detailed sales data if available
            sales_entry = next((s for s in self.sales_data if s['product_id'] == product_id), None)
            if sales_entry:
                # Calculate recent sales trend
                if 'daily_sales' in sales_entry and len(sales_entry['daily_sales']) > 0:
                    recent_sales = sum(day['units_sold'] for day in sales_entry['daily_sales'][-7:])
                    score += recent_sales / 10  # Give some weight to recent sales
            
            popularity[product_id] = min(score, 10)  # Cap at 10
        
        return popularity
    
    def get_recommendations(self, user_query, effect=None, top_n=5):
        """Get product recommendations based on user query and effect filter"""
        # If no query, return most popular products
        if not user_query and not effect:
            sorted_products = sorted(self.products, 
                                     key=lambda p: self.popularity_scores.get(p['id'], 0), 
                                     reverse=True)
            return sorted_products[:top_n]
        
        # Filter by effect if specified
        filtered_products = self.products
        product_indices = list(range(len(self.products)))
        
        if effect:
            filtered_products = []
            product_indices = []
            for i, product in enumerate(self.products):
                if effect.lower() in [e.lower() for e in product['effects']]:
                    filtered_products.append(product)
                    product_indices.append(i)
        
        # If no query but effect filter, sort by popularity
        if not user_query:
            sorted_products = sorted(filtered_products, 
                                     key=lambda p: self.popularity_scores.get(p['id'], 0), 
                                     reverse=True)
            return sorted_products[:top_n]
        
        # Encode user query
        query_embedding = self.model.encode([user_query])[0]
        
        # Get relevant product embeddings
        relevant_embeddings = self.product_embeddings[product_indices]
        
        # Calculate similarity scores
        similarity_scores = cosine_similarity([query_embedding], relevant_embeddings)[0]
        
        # Combine similarity with popularity for final score
        final_scores = []
        for i, product in enumerate(filtered_products):
            similarity = similarity_scores[i]
            popularity = self.popularity_scores.get(product['id'], 0) / 10  # Normalize to 0-1
            
            # Weight: 70% similarity, 30% popularity
            final_score = 0.7 * similarity + 0.3 * popularity
            final_scores.append((product, final_score))
        
        # Sort by final score and return top N
        sorted_recommendations = [item[0] for item in sorted(final_scores, key=lambda x: x[1], reverse=True)]
        return sorted_recommendations[:top_n]
