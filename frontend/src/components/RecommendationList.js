import React from 'react';
import ProductCard from './ProductCard';
import '../styles/RecommendationList.css';

const RecommendationList = ({ recommendations, onProductSelect }) => {
  return (
    <div className="recommendation-list">
      <h2>Recommended Products</h2>
      <div className="recommendations-container">
        {recommendations.length === 0 ? (
          <p>No recommendations found. Try a different search.</p>
        ) : (
          recommendations.map((product) => (
            <ProductCard
              key={product.id}
              product={product}
              onClick={() => onProductSelect(product.id)}
            />
          ))
        )}
      </div>
    </div>
  );
};

export default RecommendationList;
