const PORT = 3260;

// imports
const fs = require('fs');
const csv = require('fast-csv');

// vars
let users = require('./leaderboard.json');
let logger = fs.createWriteStream('output.log');
let to_check = []
let next_question_index = 0;

// setup

const data_contents = fs.readFileSync(__dirname + '/data.tsv', { encoding: 'utf8' });
to_check = data_contents.split('\n').map(l => l.split('	'))
    .map(([id, context, question, output, answers]) => ({
        id: id, context: context, question: question, output: output, answers: answers
    }));

// util
function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
}
function save_to_leaderboard(users) {
    fs.writeFile('leaderboard.json', JSON.stringify(users), e => { if (e) console.err(e); });
}

// express
const express = require('express');
const app = express();
app.use(express.json());
app.use('/static', express.static(__dirname + '/public'));

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/public/index.html');
});

app.get('/api/v1/next_item', (req, res) => {
    //res.json(to_check[Math.floor(Math.random() * to_check.length)]);
    res.json(to_check[next_question_index % to_check.length]);
    next_question_index += 1;
    if (next_question_index % to_check.length == 0)
        shuffleArray(to_check);
});

app.get('/api/v1/leaderboard', (req, res) => {
    res.json(users);
});

app.post('/api/v1/submit_item', (req, res) => {
    const user = req.body.username;
    if (!(user in users)) users[user] = 0;
    req.body.date = (new Date()).toISOString();
    console.log(req.body)
    logger.write(JSON.stringify(req.body) + '\n');
    users[user] += 1;
    save_to_leaderboard(users);
    res.end('ok');
});

app.listen(PORT, () => console.log(`serving on port ${PORT}`));

