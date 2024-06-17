from flask import Flask, render_template, request, redirect, url_for
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)

def benford_law(data):
    first_digits = [int(str(x)[0]) for x in data if x > 0]
    digit_counts = np.bincount(first_digits)[1:]
    digit_frequencies = digit_counts / len(first_digits)
    return digit_frequencies

def generate_benford_plot(data):
    frequencies = benford_law(data)
    digits = np.arange(1, 10)
    plt.figure(figsize=(10, 6))
    plt.bar(digits, frequencies, tick_label=digits)
    plt.xlabel('Primer Dígito')
    plt.ylabel('Frecuencia')
    plt.title('Distribución de los Primeros Dígitos según la Ley de Benford')

    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    img_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    buf.close()

    return img_base64

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        numbers = request.form.get('numbers')
        numbers = [float(x) for x in numbers.split(',')]
        img_base64 = generate_benford_plot(numbers)
        return render_template('index.html', img_base64=img_base64)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
