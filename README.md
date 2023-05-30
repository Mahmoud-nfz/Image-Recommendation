# Image Recommendation


## Utilization

- Make sure you have `pipenv` installed in your system.
- run `pipenv install` to install all the dependencies.
- run `pipenv shell` to activate the virtual environment.
- Make sure you have a kaggle api key and the kaggle.json file is placed in `~/.kaggle/` directory.
- run `python main.py` to run the program.
- send a `POST` request to `http://localhost:9090/upload` with the following body:

```json
{
    "image": "image"
}
```