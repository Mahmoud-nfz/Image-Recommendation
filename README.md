# Image Recommendation

### Notebook : 
https://www.kaggle.com/code/mahmoud17/image-recommendation

## Utilization

- Make sure you have `pipenv` installed in your system.
- run `pipenv install` to install all the dependencies.
- run `pipenv run python3 main.py` to run the program inside the virtual environment.
- send a `POST` request to `http://localhost:9090/upload` with the following body:

```json
{
    "image": "image"
}
```
