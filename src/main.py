from flask import *
import requests, dotenv, os, json, time

dotenv.load_dotenv(
    os.path.join(
        os.path.dirname(__file__), "..", ".env"
    )
)

api = "https://script.google.com/macros/s/" + dotenv.get_key(
    os.path.join(
        os.path.dirname(__file__), "..", ".env"
    ), "GOOGLE_APPS_SCRIPT_DEPLOYMENT_ID"
) + "/exec"

app = Flask(__name__)


def decomp(arr):
    if not arr:
        return []
    keys = list(arr[0].keys())
    res = [keys, *(list(obj.values()) for obj in arr)]
    return res


@app.route("/api/<req>", methods=["GET", "POST"])
def api_req(req):
    if request.method == "POST":
        res = requests.post(
            f"{api}?id={req}&type=create",
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json"
            },
            data=request.get_json()
        )
        return json.loads(res.content)
    if request.method == "PATCH":
        res = requests.post(
            f"{api}?id={req}&type=update&data={request.form}",
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json"
            },
            data=request.form
        )
    if request.method == "DELETE":
        res = requests.post(
            f"{api}?id={req}&type=delete&data={request.form}",
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json"
            },
            data=request.form
        )
    res = requests.get(f"{api}?id={req}")
    try:
        return json.loads(res.content)
    except: pass
    return json.loads('{"error": 1}')

@app.route("/api/<req>/<param>", methods=["GET", "POST", "DELETE", "PATCH"])
def api_req_param(req, param):
    if request.method == "POST":
        try:
            res = requests.post(
                f"{api}?id={req}&sheet={param}&type=create",
                headers={
                    "Accept": "application/json",
                    "Content-Type": "application/json"
                },
                data=json.dumps(decomp(request.get_json())[1:])
            )
            return json.loads(res.content)
        except ValueError: return json.loads('{"error": 1}')
    if request.method == "PATCH":
        try:
            res = requests.post(
                f"{api}?id={req}&sheet={param}&type=update",
                headers={
                    "Accept": "application/json",
                    "Content-Type": "application/json"
                },
                data=request.get_data()
            )
        except ValueError: return json.loads('{"error": 1}')
    if request.method == "DELETE":
        dat = request.get_json()
        dat = dat[0]
        try:
            res = requests.post(
                f"{api}?id={req}&sheet={param}&type=delete&row={dat}",
                headers={
                    "Accept": "application/json",
                    "Content-Type": "application/json"
                },
                data="empty"
            )
            return json.loads(res.content)
        except ValueError: return json.loads('{"error": 1}')
    res = requests.get(f"{api}?id={req}&sheet={param}")
    try:
        return json.loads(res.content)
    except: pass
    return json.loads('{"error": 1}')

if __name__ == "__main__":
    app.run(debug=True, port=2552)

