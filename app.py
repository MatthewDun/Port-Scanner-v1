from flask import Flask, request, render_template, jsonify
from Port_scanner import scan_ports

app = Flask(__name__)

@app.route("/")
def home():
        return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit():
        data = request.get_json()
        Ip = data.get("Ipaddress")
        ports = scan_ports(Ip)

        return jsonify({"open_ports": ports})



if __name__ == "__main__":
        app.run(debug=True)