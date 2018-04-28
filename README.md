# slattie_consoleVid


To run: in command prompt, type
> pipenv --three

> pipenv shell

> pipenv install

> python3 application.py


Anything in 'firstWordList' will be recognized as being the first word of a
response. The application expects first word videos to be located in a specific
directory where < word > is the first word:

> src/vids/fw/< word >

Anything in 'specialWordList' will be recognized as being a special word
existing anywhere within a response. The application expects special word videos
to be located in a specific directory where < word > is the special word:

> src/vids/sw/< word >

The application expects non-special word videos to be located in a specific
directory:

> src/vids/sw/
