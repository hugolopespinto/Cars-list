import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';
import Navbar from './navbar';

function App() {
  const [showAddForm, setShowAddForm] = useState(false);
  const [items, setItems] = useState([]);
  const [newItemName, setNewItemName] = useState('');

  useEffect(() => {
    fetchItems();
  }, []);

  const fetchItems = () => {
    axios.get('http://localhost:3001/elements')
      .then(response => {
        setItems(response.data);
      })
      .catch(error => {
        console.error('There was an error fetching the items!', error);
      });
  };

  const handleAddItem = () => {
    axios.post('http://localhost:3001/elements', { name: newItemName })
      .then(response => {
        console.log('Item added successfully:', response.data);
        setNewItemName('');
        setShowAddForm(false);
        fetchItems();
      })
      .catch(error => {
        console.error('Error adding item:', error);
      });
  };

  const handleClearList = () => {
    axios.delete('http://localhost:3001/clear-items')
      .then(response => {
        console.log('Items cleared successfully:', response.data);
        fetchItems();
      })
      .catch(error => {
        console.error('Error clearing items:', error);
      });
  };

  return (
    <div className="App">
      <Navbar />
      <div className="button-container">
        <button onClick={() => setShowAddForm(true)}>Add a new car</button>
        <button onClick={handleClearList}>Clear the list</button>
      </div>

      {showAddForm && (
        <div className="modal">
          <div className="modal-content">
            <span className="close" onClick={() => setShowAddForm(false)}>&times;</span>
            <h2>Add a new car to the list</h2>
            <input
              type="text"
              value={newItemName}
              onChange={(e) => setNewItemName(e.target.value)}
              placeholder="Enter car name / model"
            />
            <button onClick={handleAddItem} disabled={newItemName.trim() === ''}>ADD</button>
          </div>
        </div>
      )}

      <div className="items-list">
        <h2 style={{ textAlign: 'center' }}>Items List</h2>
        <div style={{ display: 'flex', justifyContent: 'center' }}>
          <div style={{ maxWidth: '400px', textAlign: 'left' }}>
            {items.map((item, index) => (
              <div key={index} style={{ marginBottom: '10px' }}>{item.name}</div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
