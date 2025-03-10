import React, { useState } from 'react';
import '../styles/SearchBar.css';

const SearchBar = ({ onSearch, onEffectFilterChange, effectOptions, selectedEffect }) => {
  const [query, setQuery] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    onSearch(query);
  };

  return (
    <div className="search-bar">
      <form onSubmit={handleSubmit}>
        <div className="search-input-container">
          <input
            type="text"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="What are you looking for today? (e.g. relaxing tea, energy boost, etc.)"
            className="search-input"
          />
          <button type="submit" className="search-button">
            Search
          </button>
        </div>
        
        <div className="filter-container">
          <label htmlFor="effect-filter">Filter by effect:</label>
          <select
            id="effect-filter"
            value={selectedEffect}
            onChange={(e) => onEffectFilterChange(e.target.value)}
            className="effect-filter"
          >
            <option value="">All Effects</option>
            {effectOptions.map((effect, index) => (
              <option key={index} value={effect}>
                {effect}
              </option>
            ))}
          </select>
        </div>
      </form>
    </div>
  );
};

export default SearchBar;
