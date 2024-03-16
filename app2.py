from flask import Flask, request, render_template_string, render_template
import requests

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@picocss/pico@1/css/pico.min.css">
    <title>Weather Website using API function</title>
</head>
<body>
    <nav class="container-fluid">
        <ul>
            <li><strong>Weather Website</strong></li>
        </ul>
        <ul>
            <li><a href="#about">About</a></li>
            <li><a href="#contact" role="button">Contact</a></li>
        </ul>
    </nav>
    <main class="container">
        <div class="grid">
            <section>
                <hgroup>
                    <h2>Weahter Website in Real Life</h2>
                    <h3>Overview</h3>
                </hgroup>
                <p>This page displays the use of a Weather API to fetch data and return the weather and temperature (in celsius obviously). This page also presents the API function in Python. Have Fun!</p>
                <form method="post">
                    <input type="text" id="cityName" name="cityName" placeholder="Enter a city name" required>
                    <button type="submit">Get Weather</button>
                </form>
                {% if weather %}
                <p><strong>Weather:</strong> {{ weather.description }}</p>
                <p><strong>Temperature:</strong> {{ temperature }} Celsius</p>
                {% endif %}
            <h3>API Function Code</h3>
                <pre><code>import requests;

API_KEY = "your_api_key"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data["main"]["temp"] - 273.15, 2)
    
    print("Weather: ", weather)
    print("Temperature: ", temperature, "celsius")
else:
    print("An error occurred")</code></pre>
            </section>
        </div>
    </main>

</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        city_name = request.form['cityName']
        API_KEY = "2d552cbeed96f31b2263ee15c529cb7d"
        BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
        request_url = f"{BASE_URL}?appid={API_KEY}&q={city_name}"
        response = requests.get(request_url)
        if response.status_code == 200:
            data = response.json()
            weather = {
                'description': data['weather'][0]['description'],
                'temperature': round(data["main"]["temp"] - 273.15, 2)
            }
            return render_template_string(HTML_TEMPLATE, weather=weather, temperature=weather['temperature'])
        else:
            print("An error occurred")
    return render_template_string(HTML_TEMPLATE, weather=None)
@app.route('/about')
def about():
    return render_template('about.html')
if __name__ == '__main__':
    app.run(debug=True)
