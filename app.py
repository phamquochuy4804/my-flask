from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="vi">
    <head>
        <meta charset="UTF-8">
        <title>Lab 3 - Flask Render</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {
                background: linear-gradient(to right, #dfe9f3, #ffffff);
                font-family: 'Segoe UI', sans-serif;
            }
            .navbar {
                margin-bottom: 30px;
            }
            .card {
                background-color: #ffffffcc;
                padding: 30px;
                border-radius: 15px;
                box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            }
        </style>
    </head>
    <body>
        <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
            <div class="container-fluid">
                <a class="navbar-brand" href="#">🏠 Trang chủ</a>
                <div>
                    <ul class="navbar-nav me-auto mb-2 mb-lg-0 d-flex flex-row gap-3">
                        <li class="nav-item">
                            <a class="nav-link active" href="#">📄 Thông tin</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#">🔙 Trở về</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>

        <div class="container d-flex justify-content-center">
            <div class="card text-center w-75">
                <h1 class="text-success">👋 Chào mừng bạn đến với Lab 3!</h1>
                <p class="fs-5 mt-3">
                    Họ và tên: <strong>Phạm Quốc Huy</strong><br>
                    MSSV: <strong>22DH111305</strong><br><br>
                    Đây là trang web viết bằng <strong>Flask</strong>, triển khai trên <strong>Render</strong> bằng <strong>Python</strong>.<br>
                    Chúc bạn học tốt và làm bài thật vui vẻ!
                </p>
            </div>
        </div>
    </body>
    </html>
    """
