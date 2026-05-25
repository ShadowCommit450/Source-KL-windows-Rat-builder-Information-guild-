from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Source-KL Windows RAT Builder</title>

    <meta name="description" content="Source-KL Windows RAT Builder interface with payload configuration and remote management tools.">

    <meta name="keywords" content="Windows RAT Builder, Source-KL, payload builder, remote administration, Windows client manager, loader, command control">

    <style>
        body{
            background:#10131a;
            color:white;
            font-family:Arial;
            text-align:center;
            padding-top:100px;
        }

        h1{
            font-size:45px;
        }

        p{
            color:#cccccc;
            width:70%;
            margin:auto;
            line-height:1.8;
        }
    </style>
</head>
<body>

    <h1>Source-KL Windows RAT Builder</h1>

    <p>
        Windows payload generation and remote management platform with configurable
        modules, startup systems, encrypted communication handling, and runtime controls.
    </p>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=True)
