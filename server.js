const express = require('express');
const fs = require('fs');
const path = require('path');

const app = express();
const port = 5000;


app.use(express.static('templates'));

app.get('/api/faqs', (req, res) => {
    fs.readFile(path.join(__dirname, 'data', 'faqs.json'), 'utf8', (err, data) => {
        if (err) {
            res.status(500).send('Error reading theFAQs data');
            return;
        }
        res.json(JSON.parse(data));
    });
});


app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'templates', 'faqs.html'));
});


app.listen(port, () => {
    console.log(`Server listening at http://localhost:${port}`);
})