from flask import Flask, jsonify
app = Flask(__name__)

def fib(num):
    if num == 1:
        return 1
    if num <= 0:
        return 0
    return fib(num-1) + fib(num-2)


@app.route('/hi/<num>')
def hi(name=None):
  result = fib(num)
  return jsonify({
        "result": result,
  })

if __name__ == '__main__':
    app.run(host="0.0.0.0")
