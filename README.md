# Word frequency

## What is it?
A service (API) that provide, for a given text, the highest frequency word in this text, the frequency of the specified
word and a list of the most frequent words.

## Tech/framework

* Framework: ``Django``

## installation (via virtual env. If you want to use docker, please skip this step)

```
$ virtualenv .venv

$ source .venv/bin/activate

$ python -m pip install -r requirements.txt

$ python manage.py runserver 

$ (for test) : python manage.py test
```

## Commands

* Launch server : sudo docker-compose build && sudo docker-compose up
* Launch tests :  sudo docker-compose run api sh -c "python manage.py test"

## Utilisation

* The Highest frequency word a text : http://0.0.0.0:9000?action=calculate_highest_frequency&text=your_text
* Frequency for a word : http://0.0.0.0:9000?action=calculate_frequency_for_word&text=your_text&word=your_word
* Calculate most frequency words in a text : http://0.0.0.0:9000?action=calculate_most_frequent_words&text=your_text
* If you want test through a file, go to the file (in the root of the project) named input.py and give a value to the variables "text" and "word"

('your_text' and 'your_word' are the text and word that you want using)