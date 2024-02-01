from flask import *
import requests, dotenv, os, json, base64

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

def toDataURI(txt: str, type="text/plain"):
    # Text to base64
    txtToBase64 = base64.b64encode(txt.encode()).decode("utf-8")
    data_uri = f"data:{type};base64,{txtToBase64}"
    return data_uri

# Web Site

def getReadme(lang):
    readme_path = os.path.join(
        os.path.dirname(__file__).replace("src", ""), f"README.{lang}.md"
    )
    with open(readme_path, "r", encoding="utf-8") as file:
        if file.readable():
            return toDataURI(file.read())
        else:
            with open(readme_path.replace(f"README.{lang}.md", "404.md"), "r") as f404:
                return toDataURI(f404.read())


@app.route("/")
def master():
    return """
        <script>window.location.href = navigator.language.split("-")[0];</script>
    """

@app.route("/<lang>")
def master2(lang):
    return render_template("index.html", readme=getReadme(lang), lang=lang)

@app.errorhandler(404)
def not_found(err):
    return err



# API

@app.route("/api/<req>", methods=["GET", "POST"])
def api_req(req):
    if request.method == "POST":
        try:
            res = requests.post(
                f"{api}?id={req}&type=create",
                headers={
                    "Accept": "application/json",
                    "Content-Type": "application/json"
                },
                data=json.dumps(decomp(request.get_json())[1:])
            )
            return json.loads(res.content)
        except ValueError: return json.loads('{"error": 1}')
    if request.method == "PATCH":
        row = request.get_json()
        row = row[0]
        column = decomp(request.get_json()[1:])[1]
        try:
            res = requests.post(
                f"{api}?id={req}&type=update&row={row}&column={column}",
                headers={
                    "Accept": "application/json",
                    "Content-Type": "application/json"
                },
                data=json.dumps(decomp(request.get_json()[1:])[1:])
            )
            return json.loads(res.content)
        except ValueError: return json.loads('{"error": 1}')
    if request.method == "DELETE":
        dat = request.get_json()
        dat = dat[0]
        try:
            res = requests.post(
                f"{api}?id={req}&type=delete&row={dat}",
                headers={
                    "Accept": "application/json",
                    "Content-Type": "application/json"
                },
                data="empty"
            )
            return json.loads(res.content)
        except ValueError: return json.loads('{"error": 1}')
    res = requests.get(f"{api}?id={req}")
    try:
        return json.loads(res.content)
    except: pass
    return json.loads('{"error": 1}')

@app.route("/api/<req>/<param>", methods=["GET", "POST", "DELETE", "PATCH"])
def api_req_param(req, param):
    if request.method == "POST":
        if param == "insertsheet":
            pass
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
        row = request.get_json()
        row = row[0]
        column = decomp(request.get_json()[1:])[1]
        try:
            res = requests.post(
                f"{api}?id={req}&sheet={param}&type=update&row={row}&column={column}",
                headers={
                    "Accept": "application/json",
                    "Content-Type": "application/json"
                },
                data=json.dumps(decomp(request.get_json()[1:])[1:])
            )
            return json.loads(res.content)
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

