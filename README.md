# node-icu-tokenizer

Node.js String Tokenizer using ICU's BreakIterator

See [http://userguide.icu-project.org/boundaryanalysis](http://userguide.icu-project.org/boundaryanalysis) for a rundown on how the BreakIterator works.

Install ICU first:

**OS X**
```
brew install icu4c
brew link icu4c --force
```

**Linux**

```
apt-get install libicu-dev
or 
yum install libicu-devel
```

**Manually**

```bash
curl -LO http://download.icu-project.org/files/icu4c/55.1/icu4c-55_1-src.tgz
tar xzvf icu4c-55_1-src.tgz
cd icu/source
chmod +x runConfigureICU configure install-sh
./runConfigureICU MacOSX
make
sudo make install
sudo cp -r common/unicode /usr/local/include/
```

Install the NPM module:

```
npm install node-icu-tokenizer
```

Call the tokenizer:

```
new Tokenizer().tokenize('pretty quiet out there eh?');
```

Receive an array of tokens with boundaries:
```
[ { token: 'pretty', bounds: { start: 0, end: 6 } },
  { token: 'quiet', bounds: { start: 7, end: 12 } },
  { token: 'out', bounds: { start: 13, end: 16 } },
  { token: 'there', bounds: { start: 17, end: 22 } },
  { token: 'eh', bounds: { start: 23, end: 25 } },
  { token: '?', bounds: { start: 25, end: 26 } } ]
```

### Tokenizer Options

**locale**
* An [ICU locale](http://userguide.icu-project.org/locale). Defaults to **en_US**

**ignoreWhitespaceTokens** 
* If true (default) whitespaces are ommitted as tokens. Otherwise they are treated as normal words.


## Acknowledgments

This module is based off of node-icu-wordsplit, which also uses the BreakIterator for tokenizing.
[https://github.com/chakrit/node-icu-wordsplit] (https://github.com/chakrit/node-icu-wordsplit)
