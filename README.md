# CDB Calculator

This application calculates the evolution of a CDB and exposes an API and a web page using a chart, based on values extracted from a 
CSV file, containing the CDI historical series during certain interval.

`Sqlite` was used for the database, but it can be easily changed just by changing the connection settings in `settings.py` file.

## Demo
If you want to try a demo, go to 
https://cdb-calculator-app.herokuapp.com/tools/cdb

How to run
------------------------------
1. With Python 3.7 or earlier and Pipenv installed (or with pip and some virtual environment)
    - Run `pipenv install` to install the packages.
2. Run the application using the Pipenv created environment
    - `pipenv run python manage.py runserver 8000`
    - If you prefer, you can access directly, activating the pipenv shell before (`pipenv shell` and `python manage.py runserver 8000`)

Access the application
------------------------------
- Go to http://localhost:8000/tools/cdb in your browser to access the web tool
- Or use the API endpoint http://localhost:8000/api/fixed-incomes/cdb/calculate 
    - Use a GET request with JSON encode and the following body format:
        ```json
        {
            "investmentDate":"2016-11-14",
            "cdbRate": 103.5,
            "currentDate":"2016-12-26"
        }
        ```
    - The result is the CDB unit price list between the initial investment date and the current date


Scripts
-------------------
- If you need to reimport the database, use `./manage.py runscript import_cdi_prices`


Running the tests
------------------------------
- Run `./manage.py test fixed_incomes`


Ideas for improvements
------------------------------
- [x] ~~Asyncronous API fetch on the web page~~ 
- [x] ~~Separated Django settings environment for a safe deployment~~ 
- [ ] Fetch CDI values from some API from times to times and use some scheduler like `crontab` 
- [ ] Add other types of fixed income



