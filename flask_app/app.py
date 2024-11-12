from flask import Flask, render_template, request, send_file
import pandas as pd
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    df = pd.DataFrame({
        'Name': ['Anna', 'Boris', 'Victor'],
        'Result': [25, 30, 35],
        'City': ['Paris', 'Nancy', 'Riga']
    })

    uploaded_df = None
    stats = None

    try:
        if request.method == 'POST':
            print("Form submitted")

            if 'name' in request.form:
                name = request.form['name']
                print(f"Name entered: {name}")

            if 'file' in request.files:
                file = request.files['file']
                if file and file.filename.endswith('.csv'):
                    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
                    print(f"Saving uploaded file to {file_path}")
                    file.save(file_path)
                    uploaded_df = pd.read_csv(file_path)
                    print("File uploaded successfully")
                    stats = uploaded_df.describe().to_html()
                    print("Stats generated")
                else:
                    print("No valid CSV file uploaded")

    except Exception as e:
        print(f"Error: {e}")

    return render_template('index.html', name=name, df=df, uploaded_df=uploaded_df, stats=stats)

@app.route('/download_example')
def download_example():
    try:
        example_csv = "Name,Age,City\nAnna,25,Milan\nBoris,30,Roma\nVictor,35,Kazan\n"
        with open("example_data.csv", "w") as file:
            file.write(example_csv)
        print("Example CSV created")
        return send_file(
            'example_data.csv',
            download_name='example_data.csv',
            as_attachment=True
        )
    except Exception as e:
        print(f"Error in download_example: {e}")
        return "Error occurred while generating the download file", 500

if __name__ == '__main__':
    print("Starting Flask app")
    app.run(host="0.0.0.0",port=5000)

