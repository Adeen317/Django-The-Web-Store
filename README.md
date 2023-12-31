# THE WEB STORE
Here are the steps to create a folder, set up a virtual environment, install Django, create a Django project, and run the development server:

1. **Create a Folder**: First, create a new directory for your Django project.

2. **Open Command Prompt in the Folder**: Now, navigate to the folder you just created in Command Prompt.

3. **Set Up a Virtual Environment**: In your Command Prompt, use the following command to create a virtual environment named 'my_env':
   
   ```
   python -m venv env
   ```

   Activate the virtual environment:
   
   ```
   env\Scripts\activate
   ```

4. **Install Django**: With the virtual environment activated, install Django using pip:

   ```
   pip install django
   ```

5. **Create a Django Project**: To start a new Django project, run the following command, replacing 'my_project' with your desired project name:

   ```
   django-admin startproject AAAIH
   ```

6. **Navigate to Your Project Folder**: Change to the project directory using the 'cd' command:

   ```
   cd AAAIH
   ```

7. **Run the Development Server**: Finally, start the Django development server:

   ```
   python manage.py runserver
   ```

   This will display a URL, typically `http://127.0.0.1:8000/`, in the command prompt.

8. **Access the Development Server**: Copy the URL displayed in the command prompt and paste it into your web browser to access your Django project.

These steps will help you create a clean development environment and get your Django project up and running professionally.


