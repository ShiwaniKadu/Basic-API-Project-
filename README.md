# Company and Employee Management System

This is a Django-based REST API project for managing companies and their employees. The project utilizes Django Rest Framework (DRF) to create and manage API endpoints.

## Features

- **Company Management**: Create, read, update, and delete company records.
- **Employee Management**: Create, read, update, and delete employee records.
- **Custom Endpoint**: Retrieve employees of a specific company.

## Technologies Used

- Django
- Django Rest Framework (DRF)

## Getting Started

### Prerequisites

- Python 3.6+
- Django 3.2+
- Django Rest Framework 3.12+

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/your-repository.git
    cd your-repository
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run migrations to set up the database:
    ```bash
    python manage.py migrate
    ```

5. Create a superuser to access the Django admin:
    ```bash
    python manage.py createsuperuser
    ```

6. Start the development server:
    ```bash
    python manage.py runserver
    ```

### API Endpoints

#### Company Endpoints

- List all companies: `GET /companies/`
- Retrieve a specific company: `GET /companies/{id}/`
- Create a new company: `POST /companies/`
- Update an existing company: `PUT /companies/{id}/`
- Delete a company: `DELETE /companies/{id}/`
- List all employees of a company: `GET /companies/{id}/employees/`

#### Employee Endpoints

- List all employees: `GET /employees/`
- Retrieve a specific employee: `GET /employees/{id}/`
- Create a new employee: `POST /employees/`
- Update an existing employee: `PUT /employees/{id}/`
- Delete an employee: `DELETE /employees/{id}/`

### Example Request and Response

#### Get Employees of a Company

**Request:**
```bash
GET /companies/{company_id}/employees/

