const words = ["Cientista de Dados", "Professor", "pai da Helena"];
let i = 0;
let timer;

function typingEffect() {
    let word = words[i].split("");
    var loopTyping = function () {
        if (word.length > 0) {
            document.getElementById('word').innerHTML += word.shift();
        } else {
            setTimeout(deletingEffect, 1500); // Agora espera um segundo antes de começar a apagar
            return false;
        }
        timer = setTimeout(loopTyping, 40);
    };
    loopTyping();
}

function deletingEffect() {
    let word = words[i].split("");
    var loopDeleting = function () {
        if (word.length > 0) {
            word.pop();
            document.getElementById('word').innerHTML = word.join("");
        } else {
            setTimeout(typingEffect, 100); // Agora espera meio segundo antes de começar a escrever a próxima palavra
            if (words.length > (i + 1)) {
                i++;
            } else {
                i = 0;
            }
            return false;
        }
        timer = setTimeout(loopDeleting, 40);
    };
    loopDeleting();
}

typingEffect();
