from flask import Flask, request, send_from_directory
import os

if not os.path.exists("files"):
    os.mkdir("files")
    
app = Flask(__name__)

@app.route('/')
def list_files():
    files = os.listdir('files')
    html = """
    <h1>Файлы в облаке</h1><ul>
    <a href="/upload">загрузить файл</a>
    """
    for f in files:
        html += f'<li><a href="/download/{f}">{f}</a></li>'
    html += '</ul>'
    return html
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            file.save(f"files/{file.filename}")
            return "Файл загружен! <a href='/'>Назад</a>"
    return '''
        <form method="post" enctype="multipart/form-data">
            <input type="file" name="file">
            <button>Загрузить</button>
        </form>
    '''
@app.route("/download/<filename>")
def download(filename):
    return send_from_directory(f"files", filename)

if __name__ == '__main__':
    app.run(debug=True)
