from flask import Flask, render_template, request, jsonify
import sensors
import pump_control
import image_processing

app = Flask(__name__)

# Dashboard Route
@app.route("/")
def dashboard():
    sensor_data = {
        "temperature": sensors.get_temperature(),
        "pH": sensors.get_ph(),
        "tds": sensors.get_tds(),
        "humidity": sensors.get_humidity(),
        "water_level": sensors.get_water_level(),
    }
    return render_template("dashboard.html", data=sensor_data)

# Individual Sensor Routes
@app.route("/temperature")
def temperature():
    data = sensors.get_temperature_log()
    return render_template("temperature.html", data=data)

@app.route("/ph")
def ph():
    data = sensors.get_ph_log()
    return render_template("ph.html", data=data)

@app.route("/tds")
def tds():
    data = sensors.get_tds_log()
    return render_template("tds.html", data=data)

@app.route("/humidity")
def humidity():
    data = sensors.get_humidity_log()
    return render_template("humidity.html", data=data)

@app.route("/water-level")
def water_level():
    data = sensors.get_water_level_log()
    return render_template("water-level.html", data=data)

# Water Pump Control
@app.route("/pumps", methods=["GET", "POST"])
def pumps():
    if request.method == "POST":
        action = request.json.get("action")
        if action == "start":
            pump_control.start_pump()
        elif action == "stop":
            pump_control.stop_pump()
        return jsonify({"status": "success", "action": action})
    return render_template("pumps.html")

# Image Processing Route
@app.route("/image-processing")
def image_processing_page():
    result = image_processing.process_plant_image("data/images/sample.jpg")
    return render_template("image_processing.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
