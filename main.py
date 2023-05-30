from flask import Flask, request, jsonify
from flask_cors import CORS
from src.load_dataframes import load_dataframes
from src.embeddings import get_embedding, load_model
from src.find_closest import find_closest_lines
# from src.fetch_image import fetch_image
from colorama import Style, init, Fore

# Initialize colorama
init()

app = Flask(__name__)
CORS(app)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file found', 400

    file = request.files['file']

    if file.filename == '':
        return 'No selected file', 400

    file.save("./public/uploads/"+file.filename)

    embedding = get_embedding(model, "./public/uploads/"+file.filename)
    print(embedding)

    closest_indices = find_closest_lines(df_embds, embedding, top_n=5)
    print(closest_indices)
    print(df['image'][closest_indices])

    imageNames = df['image'][closest_indices].tolist()
    print(imageNames)

    imageLinks = [
        images[images['filename'] == imageName]['link'].values[0] for imageName in imageNames
    ]

    # return closest_indices as json object
    return jsonify({"recommendations":imageLinks}), 200
    # return 'File saved successfully', 200

if __name__ == '__main__':
    df, df_embds, images = load_dataframes()
    model = load_model()
    app.run(port=9090)
