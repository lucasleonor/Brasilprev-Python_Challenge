from python_challenge.setup_app import setup_app

app = setup_app()

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
