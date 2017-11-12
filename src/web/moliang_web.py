from enum import Enum

import flask
import pandas.io.json as pd_json

app = flask.Flask(__name__)


class StatsType(Enum):
    Overall = 0
    Weekly = 1
    Monthly = 2


@app.route('/')
def index():
    return flask.render_template("moliang_home.html")


@app.route('/databaseinfo')
def get_database_info():
    pass


@app.route('/overallstats')
@app.route('/weeklystats')
@app.route('/monthlystats')
def get_stats():
    pass


def flatten_json(json_list):
    flattened_list = list()
    for json_item in json_list:
        flattened_list.append(pd_json.json_normalize(json_item).to_json(orient='records'))
    return flask.jsonify(player_list=flattened_list)


if __name__ == '__main__':
    app.run(debug=False)
