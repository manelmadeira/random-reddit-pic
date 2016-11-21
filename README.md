# Random Reddit Image API

Get random image from configured Reddit channels powered by MongoDB and Python Flask.

You can see a live version of Print to Slack without a Slack channels restriction [here](https://manuelmadeira.com/random-pic).

# Requirements

MongoDB installed.

# Instalation

`pip install -r requirements.txt``

To run

`python server.py``

# Configuration

Theres a `config.json` file with sample configuration file.

| Field                | Description                            | Required |
| -------------------- | -------------------------------------- | -------- |
| server_port          | Flash Server port                      | No       |
| db.name              | DB Name                                | Yes      |
| db.connection_string | MongoDB Connection                     | Yes      |
| db.url_collection    | Collection to save used urls           | Yes      |
| print_to_slack       | If true, will respond in Slack format  | No       |
| slack_channels       | List of restricted Slack channels ID's | No       |
| categories           | Name of Reddits channels to get images | Yes       |