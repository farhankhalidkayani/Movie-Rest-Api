
# Movie Data API

A RESTful API built with Django REST Framework to manage movie data, including details like name, duration, rating, genre, and image.

## Features

- CRUD operations for movies
- Filter movies by genre (Comedy and Action)
- Upload images for movies

## Getting Started

### Prerequisites

- Python 3.x
- Django 3.x or later
- Django REST Framework
- Pillow (for image handling)

### Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```bash
   pip install django djangorestframework pillow
   ```

4. Create and apply migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create a superuser to access the admin panel:

   ```bash
   python manage.py createsuperuser
   ```

6. Run the server:

   ```bash
   python manage.py runserver
   ```

### API Endpoints

- **Movies**
  - `GET /movies/` - List all movies
  - `POST /movies/` - Create a new movie
  - `GET /movies/{id}/` - Retrieve a specific movie
  - `PUT /movies/{id}/` - Update a specific movie
  - `DELETE /movies/{id}/` - Delete a specific movie

- **Comedy Movies**
  - `GET /comedy/` - List all comedy movies

- **Action Movies**
  - `GET /action/` - List all action movies

### Model

The main model for the API is `MovieData` which includes the following fields:

- `name`: The name of the movie (max length: 200)
- `duration`: The duration of the movie in hours (float)
- `rating`: The movie rating (float)
- `genre`: The genre of the movie (default: Comedy)
- `image`: An image associated with the movie (uploaded to `Images/` directory)

### Serializer

The `MovieSerializer` is used to validate and serialize the `MovieData` model.

### Views

The API includes the following viewsets:

- `MovieViewSet`: Handles CRUD operations for all movies.
- `ComedyViewSet`: Handles read operations for comedy movies only.
- `ActionViewSet`: Handles read operations for action movies only.

### Media Files

Make sure to configure the media files in your settings to handle image uploads correctly. Ensure that the `MEDIA_URL` and `MEDIA_ROOT` settings are properly set in your `settings.py`.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Acknowledgments

- Django and Django REST Framework for making API development easy and efficient.
- Pillow for handling image uploads.

