import React, { useState, useEffect } from 'react';
import Header from './components/Header';
import SearchBar from './components/SearchBar';
import RecommendationList from './components/RecommendationList';
import ProductDetail from './components/ProductDetail';
import { fetchProducts, fetchRecommendations, fetchProductDetails } from './services/api';
import './styles/App.css';

function App() {
  const [products, setProducts] = useState([]);
  const [recommendations, setRecommendations] = useState([]);
  const [selectedProduct, setSelectedProduct] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [effectFilter, setEffectFilter] = useState('');

  // Get all products on initial load
  useEffect(() => {
    const getProducts = async () => {
      try {
        const data = await fetchProducts();
        setProducts(data);
      } catch (err) {
        setError('Failed to load products');
        console.error(err);
      }
    };

    getProducts();
  }, []);

  // Handle search
  const handleSearch = async (query) => {
    setLoading(true);
    setError('');
    try {
      const data = await fetchRecommendations(query, effectFilter);
      setRecommendations(data);
      setSelectedProduct(null);
    } catch (err) {
      setError('Failed to get recommendations');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  // Handle effect filter change
  const handleEffectFilterChange = (effect) => {
    setEffectFilter(effect);
  };

  // Handle product selection
  const handleProductSelect = async (productId) => {
    setLoading(true);
    setError('');
    try {
      const data = await fetchProductDetails(productId);
      setSelectedProduct(data);
    } catch (err) {
      setError('Failed to get product details');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  // Get all unique effects from products for filter options
  const effectOptions = [...new Set(products.flatMap(product => product.effects))];

  return (
    <div className="app">
      <Header />
      <main className="container">
        <div className="search-section">
          <SearchBar 
            onSearch={handleSearch} 
            onEffectFilterChange={handleEffectFilterChange}
            effectOptions={effectOptions}
            selectedEffect={effectFilter}
          />
          
          {error && <div className="error">{error}</div>}
          
          {loading ? (
            <div className="loading">Loading...</div>
          ) : (
            <>
              {recommendations.length > 0 && !selectedProduct && (
                <RecommendationList 
                  recommendations={recommendations} 
                  onProductSelect={handleProductSelect}
                />
              )}
              
              {selectedProduct && (
                <ProductDetail 
                  product={selectedProduct} 
                  onBack={() => setSelectedProduct(null)}
                />
              )}
            </>
          )}
        </div>
      </main>
    </div>
  );
}

export default App;
