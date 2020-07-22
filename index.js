var icuBoundaries = require('bindings')('node-icu-tokenizer');

var Tokenizer = function () {
    this.defaultOptions = {
        locale: 'en_US',
        ignoreWhitespaceTokens: true
    };
};

Tokenizer.prototype.tokenize = function (text, options) {
    options = options || {};

    if (text == null || text == undefined) {
        throw Error('"text" argument is required.');
    }

    var locale = options.locale || this.defaultOptions.locale,
        ignoreWhitespace = options.ignoreWhitespaceTokens != undefined ? options.ignoreWhitespaceTokens :
            this.defaultOptions.ignoreWhitespaceTokens;

    if (typeof text != 'string') {
        text = "" + text;
    }

    var boundaries = icuBoundaries.getWordBoundaryPositions(text, locale) || [],
    tokens = [];
    boundaries.forEach(function (boundary) {
        var token = text.substring(boundary.start, boundary.end);
        if (!ignoreWhitespace || !/\s/.test(token)) {
            tokens.push({
                token: token,
                bounds: boundary
            });
        }
    });

    return tokens;
};

module.exports = Tokenizer;
