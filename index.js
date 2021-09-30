const PORT = 3260;

// imports
const fs = require('fs');
const csv = require('fast-csv');

// vars
let users = {}
let logger = fs.createWriteStream('output.log');
let to_check = []

// setup
//fs.createReadStream(__dirname + '/data.csv')
//    .pipe(csv.parse({ headers: true, delimiter: '	' }))
//    .on('error', console.error)
//    .on('data', to_check.push)
//    .on('end', rows => console.log('processed rows:', rows, to_check));

const data_contents = fs.readFileSync(__dirname + '/data.tsv', { encoding: 'utf8' });
to_check = data_contents.split('\n').map(l => l.split('	'))
    .map(([id, context, question, output, answers]) => ({
        id: id, context: context, question: question, output: output, answers: answers
    }));

// express
const express = require('express');
const app = express();
app.use(express.json());
app.use('/static', express.static(__dirname + '/public'));

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/public/index.html');
});

app.get('/api/v1/next_item', (req, res) => {
    res.json(to_check[Math.floor(Math.random() * to_check.length)]);
    //return res.json({ id: 'bontehu', question: 'how long will it take me to code this?', output: 'seventy five years', answers: '75 years', context: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Maxime mollitia, molestiae quas vel sint commodi repudiandae consequuntur voluptatum laborum numquam blanditiis harum quisquam eius sed odit fugiat iusto fuga praesentium optio, eaque rerum! Provident similique accusantium nemo autem. Veritatis obcaecati tenetur iure eius earum ut molestias architecto voluptate aliquam nihil, eveniet aliquid culpa officia aut! Impedit sit sunt quaerat, odit, tenetur error, harum nesciunt ipsum debitis quas aliquid. Reprehenderit, quia. Quo neque error repudiandae fuga? Ipsa laudantium molestias eos sapiente officiis modi at sunt excepturi expedita sint? Sed quibusdam recusandae alias error harum maxime adipisci amet laborum.' });
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
    res.end('ok');
});

app.listen(PORT, () => console.log(`serving on port ${PORT}`));

