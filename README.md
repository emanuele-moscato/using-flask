# Example Python APIs using Flask

## Requirements
This project assumes conda environments are used to manage packages.

- Flask (`conda install flask`)
- Daiquiri (`pip install daiquiri`)
- Gunicorn (`conda install gunicorn`)

## Running the Flask app
Navigate to where the `app.py` script is and execute
```
python app.py
```

## Running the Flask app through Gunicorn
Once Gunicorn is installed, navigate to where the `app.py` script is and execute
```
gunicorn [-b <HOST>] [--reload] <MODULE>:<SERVER>
```
where `<MODULE>` is the name of the script without the extension (`app`) and `<SERVER>` is the name of the Flask server object (in this case also `app`). The `-b <HOST>` (binding) option is there to specify the IP address and port to expose, if we want to expose our app on `localhost:8000` we'll have to write `127.0.0.1:8000`. The `--reload` option is almost equivalent to a Flask server's debug mode, with the only difference that the app is reloaded only when the main module is modified (to see the changes in one of the other files, e.g. the HTML templates rendered by the app, you have to save the `app.py` file again, even if no changes were made).

The default port used by Gunicorn is already 8000 so we can just have
```
gunicorn app:app
```

When serving the app through Gunicorn, `app.run()` is not executed (`__name__=='__main__'` evaluates to `False`), so the options we specify there, such as the port binding and the debugging option, are not valid. Therefore, the app will be exposed on the port specified with the `-b` option (or 8000 if not specified) and the app won't be executed in debug mode (changes in the code will not be reflected in the browser). To launch the app in debug mode, add the `--reload` option (as it is, no value needed).
