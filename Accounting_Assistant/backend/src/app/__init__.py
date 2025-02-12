from app import app

def main():
    appl = app.get_app()
    ##!!!ADDING STATIC FOLDER
    ## IMPORT FOR CSS AND OTHER STATIC FILES
    appl.static_folder = '/home/mehdi/Projects/finance/Accounting_Assistant/frontend/static'
    app.main()
