# Man's not bot

A tool to guess whether a username looks like a bot on Twitch.tv.

Use machine learning / classification, train with usernames found in known good channels (https://cancerino.info)

Disclaimer: this code is still a shell, nothing is implemented yet (see [TODO.md](TODO.md))


## Install

Requires [pipenv](https://docs.pipenv.org/)

```
git clone https://github.com/Benzhaomin/mansnotbot.git
cd mansnotbot
pipenv install
```

## Tests

```
pipenv install --dev
pipenv run quality && pipenv run tests && pipenv check
```