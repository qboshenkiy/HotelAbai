**README.md**

# My Django Project

This project is a Django-based web application with isolated virtual environment on Windows. It includes basic setup and configuration, as well as essential directories and applications for a smooth development experience.

## Project Setup


1. **Create a Virtual Environment**:
   Open the command prompt, navigate to your project directory, and create a virtual environment:
   ```sh
   python -m venv myenv
   ```

2. **Install Python and Django**:
   Ensure Python is installed on your system. Install Django using pip:
   ```sh
   pip install django
   ```

3. **Activate the Virtual Environment**:
   ```sh
   myenv\Scripts\activate
   ```

4. **Create Django Project**:
   Create a new Django project with `manage.py` in the root directory:
   ```sh
   django-admin startproject myproject .
   ```

5. **Create Necessary Directories**:
   Create directories for templates, static files, and media in the project root:
   ```
   templates/
   static/
   media/
   ```

6. **Create Django Application**:
   Create a new Django application named `post`:
   ```sh
   python manage.py startapp post
   ```

## Configuration and Initialization

1. **Configure Application**:
   Add the `post` application to `INSTALLED_APPS` in `myproject/settings.py`:
   ```python
   INSTALLED_APPS = [
       ...
       'post',
   ]
   ```

2. **Create Models**:
   - **Card**: A model to store card information with fields `title` and `content`.
   - **Post**: A model to store post information with fields `title` and `content`.

3. **URLs Setup**:
   Add URL routing for the `post` application in `myproject/urls.py` and create `post/urls.py` for application-specific routes.

4. **Admin Initialization**:
   Register the `Card` and `Post` models in `post/admin.py` for easy management through the admin interface.

5. **Create Views**:
   - **index**: A view function to display all cards and posts on the homepage.
   - **send_mail**: A view function to handle form data submission and send emails. It processes POST requests and sends an email, then displays a success message.

## Running the Project

1. **Apply Migrations**:
   Run the following command to apply migrations:
   ```sh
   python manage.py migrate
   ```

2. **Create a Superuser**:
   Create a superuser to access the Django admin interface:
   ```sh
   python manage.py createsuperuser
   ```

3. **Run the Development Server**:
   Start the development server:
   ```sh
   python manage.py runserver
   ```

4. **Access the Application**:
   Open a web browser and go to `http://127.0.0.1:8000/` to see your application in action.

