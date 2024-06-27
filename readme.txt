Esta es la ultima version donde se pueden eliminar y agregar usuarios

# SchoolApp


School Project
 
This README file will guide you through the steps needed to set up and run the project on your local machine.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your machine
- Git installed on your machine

## Installation

Follow these steps to get the project up and running:

### 1. Clone the Repository

First, clone the repository to your local machine using Git:

```bash
git clone https://github.com/current-project (is an example you if you get until this instance you have the project)
cd schoolapp
```

### 2. Set Up a Virtual Environment

Create a virtual environment named `schoolapp` to isolate the project dependencies:

inside DATA-ACCES-MANAGEMENT 
```bash
```

Activate the virtual environment:

- On Windows:

  ```bash
  schoolapp\Scripts\activate
  ```

- On macOS and Linux:

  ```bash
  source schoolapp/bin/activate
  ```

### 3. Install Dependencies

With the virtual environment activated, install the project dependencies listed in the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations
### REMEMBER PLEASE MIGRATIONS MUST BE APPLIED ONCE WE CHANGE SOMETHING ON MODELS

Run the following command to apply the database migrations:

```bash
python manage.py migrate
```

### 5. Run the Development Server

Start the development server to run the project locally:
If you are usimg mac take into account that if you run without
the venv you might have to use python3 instead of python

```bash
python manage.py runserver
```

You should see output indicating that the server is running:

```
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Open your web browser and navigate to `http://127.0.0.1:8000/` to view the project.

## Contributing

If you want to contribute to this project, please clone the repository and create a pull request and create a new branch.

Feel free to open issues to discuss potential improvements or report bugs.



---

Team feel free to customize this README file further if you think this is incomplete.