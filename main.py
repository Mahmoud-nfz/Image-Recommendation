from flask import Flask, request, jsonify
from src.load_dataframes import load_dataframes
from src.embeddings import get_embedding, load_model
from src.find_closest import find_closest_lines
from src.fetch_image import fetch_image
from colorama import Style, init, Fore

# Initialize colorama
init()


app = Flask(__name__)

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

    print(df.head())
    for i in closest_indices:
        try:
            fetch_image(df['image'][i])
            print(Fore.Green+"Success"+Style.RESET_ALL)
        except:
            print(Fore.RED+"Error"+Style.RESET_ALL)

    # return closest_indices as json object
    return jsonify(closest_indices.tolist()), 200
    # return 'File saved successfully', 200

if __name__ == '__main__':
    df, df_embds = load_dataframes()
    model = load_model()
    app.run(port=9090)
