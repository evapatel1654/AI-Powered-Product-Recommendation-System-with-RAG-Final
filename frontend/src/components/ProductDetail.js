import React from 'react';
import '../styles/ProductDetail.css';

const ProductDetail = ({ product, onBack }) => {
  const { augmented_data } = product;

  return (
    <div className="product-detail">
      <button onClick={onBack} className="back-button">← Back to recommendations</button>
      
      <div className="product-header">
        <div className="product-image-large">
          {/* Placeholder for product image */}
          <div className="image-placeholder-large">
            <span>{product.name.charAt(0)}</span>
          </div>
        </div>
        <div className="product-header-info">
          <h2>{product.name}</h2>
          <p className="product-price-large">${product.price.toFixed(2)}</p>
          <div className="product-effects-large">
            {product.effects.map((effect, index) => (
              <span key={index} className="effect-tag-large">
                {effect}
              </span>
            ))}
          </div>
        </div>
      </div>

      <div className="product-description-section">
        <h3>Description</h3>
        <p>{product.description}</p>
      </div>

      <div className="product-ingredients">
        <h3>Ingredients</h3>
        <ul className="ingredients-list">
          {product.ingredients.map((ingredient, index) => (
            <li key={index} className="ingredient-item">
              {ingredient}
            </li>
          ))}
        </ul>
      </div>

      {augmented_data && (
        <div className="augmented-data-section">
          <h3>Enhanced Information (RAG)</h3>
          
          {augmented_data.ingredient_details && augmented_data.ingredient_details.length > 0 && (
            <div className="ingredient-details">
              <h4>Ingredient Details</h4>
              {augmented_data.ingredient_details.map((detail, index) => (
                <div key={index} className="ingredient-detail-card">
                  <h5>{detail.name}</h5>
                  <p>{detail.details}</p>
                </div>
              ))}
            </div>
          )}

          {augmented_data.suggested_uses && augmented_data.suggested_uses.length > 0 && (
            <div className="suggested-uses">
              <h4>Suggested Uses</h4>
              <ul>
                {augmented_data.suggested_uses.map((use, index) => (
                  <li key={index}>{use}</li>
                ))}
              </ul>
            </div>
          )}

          {augmented_data.health_benefits && augmented_data.health_benefits.length > 0 && (
            <div className="health-benefits">
              <h4>Potential Health Benefits</h4>
              <ul>
                {augmented_data.health_benefits.map((benefit, index) => (
                  <li key={index}>{benefit}</li>
                ))}
              </ul>
            </div>
          )}
        </div>
      )}
    </div>
  );
};

export default ProductDetail;
