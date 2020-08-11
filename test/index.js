var Tokenizer = require("../index"),
    assert = require('assert');

(function () {
    var tokenizerInstance = new Tokenizer();

    var results = tokenizerInstance.tokenize('we are conducting a test', {locale: 'en_US'});
    
    assert.notEqual(results, null, 'tokenized results');
    assert.equal(5,results.length, 'number of tokens 5');

    // locale is optional
    results = tokenizerInstance.tokenize('how about an 👍or ✌️?');
    assert.notEqual(results, null, 'tokenized results');
    assert.equal(results.length, 7, 'number of tokens 7 -- 1');

    results = tokenizerInstance.tokenize('new emojis as well ✋🏽?', {locale: 'en_US'});
    assert.notEqual(results, null, 'tokenized results');
    assert.equal(results.length, 6, 'number of tokens 7 -- 2');

    results = tokenizerInstance.tokenize('', {locale: 'en_US'});
    assert.equal(results.length, 0, 'number of tokens 0');

    results = tokenizerInstance.tokenize('but i want the whitespaces too!', {ignoreWhitespaceTokens: false});
    assert.equal(results.length, 12, 'number of tokens 12');

    console.log("All tests passed! ☕  time?");
})();
