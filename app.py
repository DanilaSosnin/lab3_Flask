from flask import Flask, render_template, url_for, redirect, request
from data import currency_dict


app = Flask(__name__)


@app.route('/')
@app.route('/en')
def index():
    return render_template('en.html', currencies=currency_dict, valid=False, total=(0,0,0,0))


@app.route('/ru')
def index_ru():
    return render_template('ru.html', currencies=currency_dict, valid=False, total=(0,0,0,0))


@app.route('/convert', methods=['POST', 'GET'])
def convert():
    if request.method == 'POST':
        isValid = True
        value = request.form['value']
        total = 0.0
        basec = request.form['bc']
        finalc = request.form['fc']
        try:
            value = float(value.replace(',', '.'))
            isValid = True
            for key in currency_dict.keys():
                if key == basec:
                    total = value * currency_dict[key]
                    break
            for key in currency_dict.keys():
                if key == finalc:
                    total = total / currency_dict[key]
                    break
        except:
            isValid = False
        if request.form['lang'] == 'RU':
            if total >= 0.1:
                return render_template('ru.html', currencies=currency_dict, valid=isValid, total=(basec, finalc, value, float("{0:.2f}".format(total))))
            else:
                return render_template('ru.html', currencies=currency_dict, valid=isValid,
                                       total=(basec, finalc, value, float("{0:.8f}".format(total))))
        else:
            if total >= 0.1:
                return render_template('en.html', currencies=currency_dict, valid=isValid, total=(basec, finalc, value, float("{0:.2f}".format(total))))
            else:
                return render_template('ru.html', currencies=currency_dict, valid=isValid,
                                       total=(basec, finalc, value, float("{0:.8f}".format(total))))
    else:
        if request.form['lang'] == 'RU':
            return render_template('ru.html')
        else:
            return render_template('en.html')


if __name__ == '__main__':
    app.run(debug=True)
