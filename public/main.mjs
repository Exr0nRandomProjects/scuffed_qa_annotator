const leaderboard_list = document.getElementById('leaderboard');
function update_leaderboard() {
    fetch('/api/v1/leaderboard')
    .then(res => res.json())
        .then(names => {
            const n = Object.entries(names);
            n.sort((a, b) => b[1] - a[1]);
            while (leaderboard_list.firstChild)
                leaderboard_list.removeChild(leaderboard_list.lastChild);
            for (let [name, score] of n) {
                const elem = document.createElement('li');  // TODO: constantly reflowwing 
                elem.innerHTML = `${name}: ${score}`;
                if (name === username) elem.setAttributeNS(null, 'style', 'color: white;');
                leaderboard_list.appendChild(elem);
            }
        });
}
setInterval(update_leaderboard, 1000);

let username = null;
if (localStorage.getItem('name')) 
    username = localStorage.getItem('name');
else
    Promise.all([
        fetch('https://random-word-form.herokuapp.com/random/adjective').then(x => x.json()),
        fetch('https://random-word-form.herokuapp.com/random/noun').then(x => x.json())
    ]).then(([[a], [n]]) => {
        username = prompt('Please enter your display name:', a + ' ' + n);
        localStorage.setItem('name', username);
    });

const DOM = {
    question: document.getElementById('display-question'),
    output: document.getElementById('display-output'),
    answers: document.getElementById('display-answer'),
    context: document.getElementById('display-context'),
}
let current_id = null;

function populate_questions() {
    fetch('/api/v1/next_item')
        .then(res => res.json())
        .then(x => {
            for (let [k, v] of Object.entries(x)) {
                if (['question', 'output', 'context', 'answers'].includes(k))
                    DOM[k].innerHTML = v;
            }
            current_id = x.id;
        }).catch(console.error);
}

function clicked(e) {
    fetch('/api/v1/submit_item', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            id: current_id,
            value: parseInt(e.target.dataset.value),
            username: username
        })
    });
    populate_questions();
}

const buttons = document.getElementById('controls').children;
for (let elem of buttons) {
    elem.addEventListener('mouseup', clicked);
}

populate_questions();
