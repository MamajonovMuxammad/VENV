from flask import Flask, render_template, request
import segno
from io import BytesIO
import base64

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    qr_data = None
    if request.method == 'POST':
        data = request.form.get('data')
        qr = segno.make(data)
        buffer = BytesIO()
        qr.save(buffer, kind='png', scale=10)
        qr_data = base64.b64encode(buffer.getvalue()).decode()

    return '''
        <form method="POST">
            <input type="text" name="data" placeholder="Введите вашу ссылку здесь">
            <input type="submit" value="Сгенерировать QR-код">
        </form>
        ''' + (f'<img src="data:image/png;base64,{qr_data}">' if qr_data else '')

if __name__ == '__main__':
    app.run(debug=True)
