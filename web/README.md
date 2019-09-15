# OPD Crimes Flask App

Flask web app to serve OPD crime data created during the data cleaning workshop.

## Install

```bash
pip install -r requirements.txt
```

## Running

`FLASK_APP` tells the Flask CLI where the app manager can be found in our code.

```bash
export FLASK_APP=crimes:app
export FLASK_ENV=development

flask run -p 8000
```

The site should now be available at [http://localhost:8000](http://localhost:8000).

## Endpoints

### `/`

Hello world index.

### `/admin`

Opens the database admin portal.

Normally this would be behind user authentication with a library like `flask-user`. Don't have an unauthenticated admin portal on a web app **EVER**.

### `/json`

Static JSON response.

You must include `"Authorization: 123abc"` in the headers to authenticate this request.

### `/hello` & `/hello/<name>`

Renders an HTML page with a generic greeting or one for the name in the URL. If your name has spaces, you must replace them with `%20` to make the URL valid.

Ex: `/hello/Jane%20Tell`

### `/crimes` & `/crimes/type/<category>`

Renders an HTML page with crime data.

Can filter with a URL parameter or the search form on the page.

### `/json/crimes` & `/json/crimes/type/<category>`

Like the previous endpoint but returns a JSON response.

### `/name`

Returns the length of a name in a POST payload.
