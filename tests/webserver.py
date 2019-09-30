import flask
import tests.sharevar

app = flask.Flask(__name__)


@app.route("/yourls-api.php", methods=["POST"])
def proc_cron():

    if "action" not in flask.request.form:
        if tests.sharevar.modifier == "badauth":
            response = flask.Response('{"message": "Invalid username or password","errorCode": 403,"callback": ""}',
                                      status=403)
        else:
            response = flask.Response('{"errorCode": 400,"message": "Unknown or missing "action" parameter"}',
                                      status=400)

        response.headers["content-type"] = "application/json"
        return response
    else:
        option = flask.request.form["action"]

    tests.sharevar.last_request = flask.request.form

    if option == "shorturl":
        if tests.sharevar.modifier == "garbledjson":
            response = flask.Response("this is not valid json")

        elif tests.sharevar.modifier == "urlerror":
            response = flask.Response('{"status": "error", "code": "error:url", "message": "message goes here"}')

        elif tests.sharevar.modifier == "othererror":
            response = flask.Response('{"status": "error", "code": "something", "message": "message goes here"}')

        else:
            response = flask.Response('{"url": {"keyword": "ozh","url": "http://ozh.org","title": "Ozh RICHARD \u00ab o'
                                      'zh.org","date": "2014-10-24 16:01:39","ip": "127.0.0.1"},"status": "success","me'
                                      'ssage": "http://ozh.org added to database","title": "Ozh RICHARD \u00ab ozh.org"'
                                      ',"shorturl": "http://sho.rt/1f","statusCode": 200}')  # this is just the example
            # response included with the YOURLS docs

        response.headers["content-type"] = "application/json"
        return response

    elif option == "expand":
        if tests.sharevar.modifier == "garbledjson":
            response = flask.Response("this is not valid json")

        elif tests.sharevar.modifier == "error":
            response = flask.Response('{"status": "error", "code": "something", "message": "error: message goes here"}')

        else:
            response = flask.Response('{"message": "success", "longurl": "https://www.example.com"}')

        response.headers["content-type"] = "application/json"
        return response

    elif option == "stats":
        if tests.sharevar.modifier == "garbledjson":
            response = flask.Response("this is not valid json")

        else:
            response = flask.Response('{"stats": {"total_links": "3","total_clicks": "2"},"statusCode": 200,"message":'
                                      ' "success"}')

        response.headers["content-type"] = "application/json"
        return response

    elif option == "url-stats":
        if tests.sharevar.modifier == "garbledjson":
            response = flask.Response("this is not valid json")

        elif tests.sharevar.modifier == "error":
            response = flask.Response('{"status": "error", "code": "something", "message": "error: message goes here"}')

        else:
            response = flask.Response('{"message": "success", "link": {"shorturl": "durdehurrhurr","url'
                                      '": "hurdedurrdurr","title": "title goes here","timestamp": "2019'
                                      '-09-19 19:10:42","ip": "xxx.xxx.xxx.xxx","clicks": "2"}}')

        response.headers["content-type"] = "application/json"
        return response

if __name__ == "__main__":
    app.run()