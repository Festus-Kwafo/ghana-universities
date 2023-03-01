# Universities in Ghana API Data
This is a web application built with FastAPI that scrapes data from https://www.4icu.org/ for universities in Ghana, and exposes them via API endpoints.

## Getting Started
To use the application, you need to have Python 3.6 or later installed on your machine. You can clone this repository or download the code as a zip file.

```bash
git clone https://github.com/Festus-Kwafo/ghana-universities.git
```

Install the required packages by running the following command in your terminal:

```bash
pip install -r requirements.txt
```
Next, start the application by running the following command:
```bash
main.py 
```

This will start the application on http://localhost:8080.

## API Endpoints
The application has the following API endpoints:

### `GET /universities`
Returns a list of all universities in Ghana.
#### Parameters
None.

#### Response
A JSON object with the following properties:

| Property    | Type   | Description                                                  |
|-------------|--------|--------------------------------------------------------------|
| name        | string | The name of the university.                                  |
| ranking     | string | The rank of the university in Ghana (according to 4icu.org). |
| website     | string | The website URL of the university.                           |
| logo        | string | The  URL of the university logo.                             |
| description | string | Row 3, Column 3                                              |
| acronym     | string | The nickname of the university                               |
| founded     | string | The year the university was founded                          |
| motto       | string | the motto of the university                                  |
| colors      | string | The colors of the university                                 |
| address     | string | The address of the university                                |
| tel         | string | The phonenumber of the university                            |
| fax         | string | The fax number of the university                             |
### `GET /universities/{rank}`
Returns information about the university with the rank in Ghana.
#### Parameters
| Property | Type   | Description                                                  |
|----------|--------|--------------------------------------------------------------|
| rank     | string | The rank of the university in Ghana (according to 4icu.org). |
#### Response
A JSON object with the following properties:

| Property    | Type   | Description                                                  |
|-------------|--------|--------------------------------------------------------------|
| name        | string | The name of the university.                                  |
| ranking     | string | The rank of the university in Ghana (according to 4icu.org). |
| website     | string | The website URL of the university.                           |
| logo        | string | The  URL of the university logo.                             |
| description | string | Row 3, Column 3                                              |
| acronym     | string | The nickname of the university                               |
| founded     | string | The year the university was founded                          |
| motto       | string | the motto of the university                                  |
| colors      | string | The colors of the university                                 |
| address     | string | The address of the university                                |
| tel         | string | The phonenumber of the university                            |
| fax         | string | The fax number of the university                             |
## Contributing
If you'd like to contribute to this project, feel free to submit a pull request!

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.