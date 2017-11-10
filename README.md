# Man's not bot

A tool to guess whether a username looks like a bot on Twitch.tv.

Use machine learning / classification, train with usernames found in known good channels (https://cancerino.info)

Disclaimer: this code is still a shell, nothing is implemented yet (see [TODO.md](TODO.md))


## Install

```
git clone https://github.com/Benzhaomin/mansnotbot.git
cd mansnotbot
virtualenv3 venv
source venv/bin/activate
pip install -e .
```

## Tests

```
pip install -e .[dev]
nosetests
flake8 mansnotbot
```