import React from 'react';
import '../styles/ProductCard.css';

const ProductCard = ({ product, onClick }) => {
  return (
    <div className="product-card" onClick={onClick}>
      <div className="product-image">
        {/* Placeholder for product image */}
        <div className="image-placeholder">
          <span>{product.name.charAt(0)}</span>
        </div>
      </div>
      <div className="product-info">
        <h3>{product.name}</h3>
        <p className="product-description">{product.description}</p>
        <div className="product-meta">
          <p className="product-price">${product.price.toFixed(2)}</p>
          <div className="product-effects">
            {product.effects.map((effect, index) => (
              <span key={index} className="effect-tag">
                {effect}
              </span>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

export default ProductCard;
