function greeting(name) {
    console.log('Hello ' + name);
}

function processUserInput(callback) {
    var name = "Olamide";
    callback(name);
}

processUserInput(greeting);