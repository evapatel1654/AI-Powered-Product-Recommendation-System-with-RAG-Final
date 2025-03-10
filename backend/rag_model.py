from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

class RAGModel:
    def __init__(self, products, ingredients):
        self.products = products
        self.ingredients = ingredients
        
        # Initialize sentence transformer model for embedding
        self.model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
        
        # Create knowledge base from ingredients
        self.knowledge_base = self._create_knowledge_base()
        
        # Build index for fast retrieval
        self.index, self.texts = self._build_index()
    
    def _create_knowledge_base(self):
        """Create a knowledge base with information about ingredients and their effects"""
        knowledge_base = []
        
        # Add ingredient information
        for ingredient in self.ingredients:
            text = f"Ingredient: {ingredient['name']}. Properties: {ingredient['properties']}. "
            text += f"Common effects: {', '.join(ingredient['common_effects'])}."
            knowledge_base.append({
                "text": text,
                "ingredient": ingredient['name']
            })
            
        return knowledge_base
    
    def _build_index(self):
        """Build a FAISS index for fast similarity search"""
        texts = [item["text"] for item in self.knowledge_base]
        embeddings = self.model.encode(texts, convert_to_numpy=True)
        
        # Normalize embeddings
        faiss.normalize_L2(embeddings)
        
        # Create index
        index = faiss.IndexFlatIP(embeddings.shape[1])
        index.add(embeddings)
        
        return index, texts
    
    def retrieve_relevant_information(self, query, k=3):
        """Retrieve relevant information from knowledge base given a query"""
        # Encode query
        query_embedding = self.model.encode([query], convert_to_numpy=True)
        faiss.normalize_L2(query_embedding)
        
        # Search for similar texts
        scores, indices = self.index.search(query_embedding, k)
        
        # Return results
        results = []
        for i, idx in enumerate(indices[0]):
            if idx < len(self.texts) and scores[0][i] > 0.5:  # Only include if similarity is high enough
                results.append(self.knowledge_base[idx])
        
        return results
    
    def augment_product(self, product):
        """Augment product information using the RAG system"""
        augmented_product = product.copy()
        
        # Create a query from product information
        query = f"{product['name']} {product['description']} {' '.join(product['effects'])}"
        
        # Add information about ingredients
        ingredient_info = []
        for ingredient in product.get('ingredients', []):
            # Retrieve information about this ingredient
            ingredient_query = f"Ingredient {ingredient} effects properties"
            relevant_info = self.retrieve_relevant_information(ingredient_query)
            
            # Find matching ingredient info
            matched_info = next((info for info in relevant_info 
                                if info.get('ingredient', '').lower() == ingredient.lower()), None)
            
            if matched_info:
                ingredient_info.append({
                    "name": ingredient,
                    "details": matched_info['text']
                })
        
        # Add augmented data
        augmented_product['augmented_data'] = {
            "ingredient_details": ingredient_info,
            "suggested_uses": self._generate_suggested_uses(product),
            "health_benefits": self._extract_health_benefits(product, ingredient_info)
        }
        
        return augmented_product
    
    def _generate_suggested_uses(self, product):
        """Generate suggested uses based on product type and effects"""
        suggested_uses = []
        
        if product['type'] == 'beverage':
            if 'relaxation' in product['effects']:
                suggested_uses.append("Enjoy before bedtime to promote relaxation and better sleep")
            if 'stress relief' in product['effects']:
                suggested_uses.append("Drink during stressful situations to help calm nerves")
        
        # Add more product types and suggestions as needed
        
        return suggested_uses
    
    def _extract_health_benefits(self, product, ingredient_info):
        """Extract potential health benefits based on ingredients"""
        benefits = []
        
        for info in ingredient_info:
            if 'relaxation' in info['details'].lower():
                benefits.append("May promote relaxation")
            if 'sleep' in info['details'].lower():
                benefits.append("May improve sleep quality")
            # Add more potential benefits
        
        return list(set(benefits))  # Remove duplicates
