# AI-Powered Product Recommendation System with RAG

This project is a prototype recommendation system that utilizes Artificial Intelligence and Retrieval-Augmented Generation (RAG) to provide personalized product recommendations based on user preferences and queries.

## Overview

The system combines traditional recommendation algorithms with modern RAG technology to create context-aware product suggestions with enhanced descriptions. By leveraging semantic search and knowledge augmentation, it provides users with relevant product recommendations and detailed information that goes beyond basic product descriptions.

## Features

- **AI-Powered Recommendations**: Implements a hybrid recommendation algorithm that balances content similarity with popularity metrics
- **Context-Aware Responses**: Uses RAG to enhance product information with relevant details from a knowledge base
- **Effect-Based Filtering**: Allows users to filter recommendations by desired effects (e.g., "relaxation", "energy")
- **Interactive Interface**: Clean, responsive UI for querying and displaying personalized recommendations
- **Detailed Product View**: Shows augmented information retrieved through the RAG system

## How to Run the Prototype

### Prerequisites
- Python 3.8+ for backend
- Node.js 14+ for frontend
- 4GB+ RAM recommended for vector operations

### Backend Setup

1. Navigate to the backend directory:
   ```
   cd backend
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the Flask application:
   ```
   python app.py
   ```
   The backend will run on http://localhost:5000

### Frontend Setup

1. Navigate to the frontend directory:
   ```
   cd frontend
   ```

2. Install dependencies:
   ```
   npm install
   ```

3. Start the React application:
   ```
   npm start
   ```
   The frontend will run on http://localhost:3000

### Testing the System

1. Visit http://localhost:3000 in your browser
2. Enter a product query (e.g., "calming tea for evening")
3. Optionally select effect filters (e.g., "relaxation", "sleep")
4. View recommendations and click on products for detailed information

## Approach to Recommendation Algorithm

The recommendation system implements a hybrid approach combining content-based filtering with popularity metrics:

### 1. Vector Embeddings
- Product descriptions and attributes are converted to vector embeddings using Sentence Transformers
- User queries are similarly transformed into the same vector space
- This enables semantic understanding beyond simple keyword matching

### 2. Similarity Calculation
- Cosine similarity is calculated between the query vector and product vectors
- Products with higher similarity scores are considered more relevant to the query

### 3. Hybrid Scoring
- Final recommendation scores combine:
  - 70% semantic similarity (relevance to query)
  - 30% popularity metrics (based on historical sales data)
- This balance ensures recommendations are both relevant and popular

### 4. Effect Filtering
- Products are tagged with effects (e.g., "relaxation", "energy boost")
- User-selected filters are applied as a post-processing step
- Only products matching the selected effects are included in final recommendations

## RAG Implementation

The RAG system enhances product information through a retrieval-based approach:

### 1. Knowledge Base Creation
- A structured knowledge base is built from ingredient data and product information
- Each knowledge entry is encoded as a vector embedding using Sentence Transformers
- FAISS (Facebook AI Similarity Search) indexes these embeddings for efficient retrieval

### 2. Information Retrieval
- When a user selects a product, the system:
  - Extracts key terms from the product description
  - Converts these terms to vector embeddings
  - Retrieves the most relevant information from the knowledge base

### 3. Product Augmentation
- The retrieved information enriches the product display with:
  - Detailed ingredient properties and benefits
  - Suggested uses based on product attributes
  - Complementary product suggestions
  - Scientific context when available

### 4. Context-Aware Responses
- The system combines the original product information with retrieved knowledge
- This creates comprehensive, informative product descriptions that address potential user questions before they're asked

## Assumptions and Simplifications

To create a working prototype within scope, several assumptions and simplifications were made:

1. **Limited Dataset**: The prototype uses a small dataset of tea products rather than a comprehensive product catalog
2. **Retrieval Focus**: The RAG implementation focuses on retrieval rather than generation (no LLM for text generation)
3. **Local Deployment**: The system is designed for local development without cloud infrastructure considerations
4. **Single User Model**: No user profiles or personalization based on user history
5. **Static Knowledge Base**: The knowledge base is pre-built rather than dynamically updated
6. **Limited Categories**: The prototype focuses on a single product category rather than multiple product types
7. **English Language Only**: No multilingual support implemented
8. **Basic Security**: No authentication or authorization mechanisms
9. **Simplified Evaluation**: No A/B testing or detailed metrics for recommendation quality

## Potential Areas for Improvement

The prototype demonstrates core functionality but could be enhanced in several ways:

### 1. Advanced Personalization
- Implement user profiles and preference tracking
- Add collaborative filtering based on similar user behaviors
- Develop a feedback loop to improve recommendations based on user interactions

### 2. Enhanced RAG Capabilities
- Incorporate a language model for true generative capabilities
- Implement dynamic knowledge base updates from trusted sources
- Add capability to explain recommendations with natural language

### 3. Scalability Improvements
- Deploy with containerization (Docker) for consistent environments
- Implement database sharding for large product catalogs
- Add caching layers for frequently requested recommendations

### 4. User Experience Enhancements
- Add more filtering options (price range, specific ingredients)
- Implement visual similarity for product recommendations
- Add product comparison features

### 5. Evaluation Framework
- Implement A/B testing for different recommendation algorithms
- Add comprehensive analytics dashboard
- Develop metrics to measure recommendation relevance and diversity

### 6. Business Integration
- Add inventory awareness to avoid recommending out-of-stock items
- Implement seasonal adjustments to recommendation weights
- Develop promotions integration for featured products

## Technology Stack

- **Backend**: Python, Flask, Sentence Transformers, FAISS
- **Frontend**: React.js, Axios, Material-UI
- **Data Storage**: JSON files (could be extended to databases)
- **Vector Operations**: NumPy, SciPy
- **Testing**: Pytest, React Testing Library

## Conclusion

This prototype demonstrates a practical implementation of an AI-powered recommendation system with RAG capabilities. While simplified for demonstration purposes, it illustrates the core concepts and provides a foundation for more sophisticated implementations. The hybrid recommendation approach combined with knowledge augmentation offers a powerful way to enhance product discovery and information presentation.
