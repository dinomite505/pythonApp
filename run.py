# imports form a Python module
from app import create_app

# to check if the script is run directly or being imported as a module into another script
if __name__ == "__main__":
    app = create_app()
    # when set to 'True' enables debugging mode
    app.run(debug=True)
