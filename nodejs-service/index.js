const express = require('express');
const axios = require('axios');
const cors = require('cors');
const app = express();
const port = 3001;

// Utiliser le middleware CORS
app.use(cors({ origin: 'http://localhost:3000' }));

// Middleware pour parser le JSON
app.use(express.json());

app.get('/elements', async (req, res) => {
  try {
    const response = await axios.get('http://python-service:5001/elements');
    res.json(response.data);
  } catch (error) {
    console.error('Error fetching elements:', error);
    res.status(500).send('Error fetching elements');
  }
});

app.post('/elements', (req, res) => {
  const { name } = req.body;
  console.log('Adding item:', name);
  axios.post('http://python-service:5001/elements', { name })
    .then(response => {
      console.log('Item added to Flask server:', response.data);
      res.send(response.data);
    })
    .catch(error => {
      console.error('Error adding item to Flask server:', error);
      res.status(500).send('Failed to add item');
    });
});

app.delete('/clear-items', (req, res) => {
  axios.delete('http://python-service:5001/clear-items')
    .then(response => {
      res.send(response.data);
    })
    .catch(error => {
      console.error('Error clearing items from Python server:', error);
      res.status(500).send('Failed to clear items');
    });
});

app.listen(port, () => {
  console.log(`Node.js service listening at http://localhost:${port}`);
});
