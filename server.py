# -*- coding: utf-8 -*-

import os
from flask import Flask, jsonify, request
from RandomImage import get_random_image
from Configs import Configs


app = Flask(__name__)


# pretty print Slack error message
def print_error_to_slack():
    return_txt = 'Nothing to see here!'

    return {
        'response_type': 'in_channel',
        'text': return_txt,
    }


def print_error():
    return {
        'text': 'Nothing to see here!'
    }


@app.route("/")
def default():
    configs = Configs()

    channel = request.args.get('channel_id')
    print 'Channel: ' + str(channel)

    # if has slack channels on configs, validates slack channel id
    flag = True
    if len(configs.get_slack_channels()) > 0:
        flag = False
        for slack_channel in configs.get_slack_channels():
            if slack_channel == channel:
                flag = True
                break

    if not flag:
        print 'Not a valid slack channel!'
        if configs.get_print_to_slack():
            return jsonify(print_error_to_slack())
        else:
            return jsonify(print_error()), 401

    url = get_random_image(configs)

    if len(url) == 0:
        if configs.get_print_to_slack():
            return jsonify(print_error_to_slack())
        else:
            return jsonify(print_error()), 404

    if configs.get_print_to_slack():
        slack_resp = {
            'response_type': 'in_channel',
            'text': '<' + url + '>',
            'unfurl_links': 'true',
        }
        return jsonify(slack_resp)
    else:
        return jsonify({
            'url': url
        })


@app.route('/status')
def status():
    return jsonify({'success': True}), 200, {'ContentType': 'application/json'}


if __name__ == "__main__":
    CONFIGS = Configs()

    PORT = int(os.environ.get('PORT', CONFIGS.get_server_port()))
    app.run(host='0.0.0.0', port=PORT)
