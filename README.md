# URL Shortener

## Overview

This URL shortener is a web application built using the Django framework and the shortuuid library. It enables users to create shortened versions of long URLs, making them more convenient to share and manage. Additionally, the application provides statistics on the number of clicks for each short link.

## Features

- **Shorten URLs:** Users can input long URLs and receive corresponding short links.
- **Redirects:** Short links automatically redirect users to the original long URLs.


## Prerequisites

Ensure that your development environment has the necessary dependencies:

- **Python (>=3.6):** The programming language used for the project.
- **Django:** The web framework for building the application.
- **shortuuid:** A library for generating concise UUIDs.

You can install the required Python packages using:

```bash
pip install django shortuuid



Getting Started:

1. Clone the repository:

-> -> https://github.com/rj62127/URLShortener.git
-> -> cd urlshortener

2. Create and activate a virtual environment (optional but recommended):

-> -> python -m venv venv
-> -> source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. Install dependencies:

-> -> pip install -r requirements.txt

4. Apply migrations:

-> -> python manage.py migrate

5. Run the development server:

-> -> python manage.py runserver


    The URL shortener will be accessible at http://localhost:8000


Usage:

-> Open your browser and navigate to http://localhost:8000.
-> Shorten a URL by entering it into the provided form.
-> Copy the generated short link and share it.


Configuration:

-> You can customize the URL shortener by modifying the settings.py file in the 'shortener' app.



Acknowledgments:

-> Django
-> shortuuid





