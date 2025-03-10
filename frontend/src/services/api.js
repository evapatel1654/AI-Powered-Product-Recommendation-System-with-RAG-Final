import axios from 'axios';

const API_URL = 'http://localhost:5000/api';

// Fetch all products
export const fetchProducts = async () => {
  try {
    const response = await axios.get(`${API_URL}/products`);
    return response.data;
  } catch (error) {
    console.error('Error fetching products:', error);
    throw error;
  }
};

// Fetch product details by ID
export const fetchProductDetails = async (productId) => {
  try {
    const response = await axios.get(`${API_URL}/product/${productId}`);
    return response.data;
  } catch (error) {
    console.error(`Error fetching product ${productId}:`, error);
    throw error;
  }
};

// Fetch recommendations based on query and effect filter
export const fetchRecommendations = async (query = '', effect = '') => {
  try {
    const params = new URLSearchParams();
    if (query) params.append('query', query);
    if (effect) params.append('effect', effect);
    
    const response = await axios.get(`${API_URL}/recommendations`, { params });
    return response.data;
  } catch (error) {
    console.error('Error fetching recommendations:', error);
    throw error;
  }
};
