from flask import Flask, render_template
from datetime import datetime
import os  # нужно импортировать

app = Flask(__name__)


@app.route('/')
def home():
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Получаем список всех файлов в папке static/images
    images_directory = os.path.join(app.static_folder, 'images')
    images = []
    for filename in os.listdir(images_directory):
        if filename.endswith('.png') or filename.endswith('.jpg'):
            # Добавляем относительный путь
            images.append('images/' + filename)
    return render_template('index.html', current_time=current_time, images=images)


# остальные маршруты
@app.route('/blog/')
def blog():
    return render_template('blog.html')


@app.route('/contacts/')
def contacts():
    return render_template('contacts.html')


if __name__ == '__main__':
    app.run(debug=True)