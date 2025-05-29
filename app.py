from flask import Flask, render_template, jsonify
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)

# Sample data (replace with your actual data from Tabell 1)
def get_pipeline_data():
    return {
        "time_periods": ["Month 1", "Month 2", "Month 3", "Month 4"],
        "pipeline_runs": [15, 28, 35, 42],
        "success_rate": [92, 94, 96, 95],
        "build_time": [8.5, 7.2, 6.8, 6.0]
    }

# Generate plot and return as base64 image
def generate_plot():
    data = get_pipeline_data()
    
    plt.figure(figsize=(10, 5))
    plt.bar(data["time_periods"], data["pipeline_runs"], color='blue', alpha=0.6, label='Pipeline Runs')
    
    plt.xlabel('Time Period')
    plt.ylabel('Number of Runs', color='blue')
    plt.twinx()
    plt.plot(data["time_periods"], data["success_rate"], color='green', marker='o', label='Success Rate (%)')
    plt.ylabel('Success Rate (%)', color='green')
    plt.twinx()
    plt.plot(data["time_periods"], data["build_time"], color='red', linestyle='--', marker='s', label='Build Time (min)')
    plt.ylabel('Build Time (min)', color='red')
    
    plt.title('Pipeline Metrics Dashboard')
    plt.legend(loc='upper left')
    
    # Save plot to a BytesIO buffer
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()
    
    return base64.b64encode(buffer.getvalue()).decode('utf-8')

@app.route('/')
def index():
    plot_data = generate_plot()
    return render_template('index.html', plot_data=plot_data)

@app.route('/api/data')
def api_data():
    return jsonify(get_pipeline_data())

if __name__ == '__main__':
    app.run(debug=True)