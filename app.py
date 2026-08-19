from flask import Flask, render_template_string

app = Flask(__name__)

PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Date and Time</title>

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            background: radial-gradient(circle, #241200 0%, #080808 45%, #000000 100%);
            color: #ff8c00;
            font-family: Arial, sans-serif;
        }

        .clock-card {
            width: 90%;
            max-width: 750px;
            padding: 55px 30px;
            text-align: center;
            background: rgba(10, 10, 10, 0.9);
            border: 2px solid #ff8c00;
            border-radius: 25px;
            box-shadow:
                0 0 20px rgba(255, 140, 0, 0.5),
                0 0 60px rgba(255, 140, 0, 0.2);
        }

        h1 {
            margin-bottom: 30px;
            font-size: 24px;
            letter-spacing: 6px;
            text-transform: uppercase;
        }

        #time {
            font-size: clamp(45px, 10vw, 90px);
            font-weight: bold;
            letter-spacing: 4px;
            text-shadow: 0 0 15px #ff8c00;
        }

        #date {
            margin-top: 25px;
            font-size: clamp(18px, 4vw, 30px);
            color: #ffc266;
            letter-spacing: 2px;
        }

        .footer {
            margin-top: 35px;
            color: #8a5a20;
            font-size: 14px;
        }
    </style>
</head>

<body>
    <div class="clock-card">
        <h1>Current Date & Time</h1>

        <div id="time">00:00:00</div>
        <div id="date">Loading...</div>

        <div class="footer">Powered by Python and Docker</div>
    </div>

    <script>
        function updateClock() {
            const now = new Date();

            const time = now.toLocaleTimeString("en-IN", {
                hour: "2-digit",
                minute: "2-digit",
                second: "2-digit",
                hour12: true
            });

            const date = now.toLocaleDateString("en-IN", {
                weekday: "long",
                day: "2-digit",
                month: "long",
                year: "numeric"
            });

            document.getElementById("time").textContent = time;
            document.getElementById("date").textContent = date;
        }

        updateClock();
        setInterval(updateClock, 1000);
    </script>
</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(PAGE)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
