# Study.com Scraper API using Flask

This project is a Flask web application that provides an API for scraping content from study.com. It utilizes BeautifulSoup for parsing HTML and serves the scraped content through API endpoints.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

- Python 3.x
- pip (Python package manager)

### Installing

1. Clone the repository:

```
git clone https://github.com/your_username/your_repository.git
```

2. Install dependencies:

```
pip install -r requirements.txt
```

### Running the Application

1. Navigate to the project directory:

```
cd your_repository
```

2. Run the Flask application:

```
python app.py
```

By default, the application will be available at `http://localhost:5000`.

## Usage

To use the API, make a GET request to the following URL:

```
https://your_domain.com/apii?url=(study_com_url)
```

Replace `(study_com_url)` with the actual URL of the study.com page you want to scrape content from.

## Built With

- Flask - Web framework for Python
- BeautifulSoup - Python library for pulling data out of HTML and XML files

## Authors

- [Your Name](https://github.com/your_username) - Initial work

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
