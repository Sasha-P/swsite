# STAR WARS Universe Character Explorer

Django based site for STAR WARS character exploration

## Requirements

Requirements for different environments located in `./requirements/` folder

0. base.txt - common to all environments
1. local.txt - for local (develop) environment
2. test.txt - for test/CI environment
3. staging.txt - for staging environment (if present)
4. production.txt - for production environment

## Configuration

Export environment variables:

1. export DJANGO_SETTINGS_MODULE='swsite.settings.`<environment>`'
2. export SECRET_KEY="`<your secret key>`"

## Rum migration and import fixture:

1. `./manage.py migrate`
2. `./manage.py migrate --database=log_db`
3. `./manage.py loaddata apps/swu/fixtures/f.json`

## Use

Export Characters to CSV file.

`./manage.py exportcsv <output_file_name.csv>`

## License

Read LICENSE.txt file

## DISCLAIMER

**ALL COPYRIGHTS BELONG TO THEIR RESPECTIVE OWNERS**