from flask import Flask, jsonify, request, render_template
app = Flask(__name__)

from execrequest import ExecRequest

@app.route('/', methods=['GET', 'POST'])
def home():
    # POST request
    if request.method == 'POST':
        print('POST request received')
        request_data = request.get_json()
        req = ExecRequest(request_data)

        # for debugging
        #  print(req.run_tmp_file())

        return req.run_tmp_file(), 200

    # GET request
    else:
        message = {'some_key':'some_val'}
        return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True)
