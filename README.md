# API Documentation

## Overview
This API provides endpoints for managing users, tokens, and products in an e-commerce backend.

## Authentication
All endpoints, except for registration and login, require authentication via Bearer tokens.

## Endpoints

### User Endpoints

#### Register a New User
- **URL:** `/users/register/`
- **Method:** `POST`
- **Permissions:** [AllowAny](file:///Users/datran/learn_devs/fullstack/ecommerce/api/views/token_view.py#7%2C57-7%2C57)
- **Request Body:**
  ```json
  {
    "username": "string",
    "email": "string",
    "password": "string"
  }
  ```
- **Response:**
  ```json
  {
    "id": "uuid",
    "username": "string",
    "email": "string",
    "created_at": "datetime",
    "updated_at": "datetime"
  }
  ```

#### Login
- **URL:** `/users/login/`
- **Method:** `POST`
- **Permissions:** `AllowAny`
- **Request Body:**
  ```json
  {
    "username": "string",
    "password": "string"
  }
  ```
- **Response:**
  ```json
  {
    "user": {
      "id": "uuid",
      "username": "string",
      "email": "string",
      "last_login": "datetime"
    },
    "access": "string"
  }
  ```

#### Get Current User
- **URL:** `/users/me/`
- **Method:** `GET`
- **Permissions:** `IsAuthenticated`
- **Response:**
  ```json
  {
    "id": "uuid",
    "username": "string",
    "email": "string",
    "last_login": "datetime"
  }
  ```

#### Logout
- **URL:** `/users/logout/`
- **Method:** `POST`
- **Permissions:** `IsAuthenticated`
- **Response:**
  ```json
  {
    "message": "Logout successfully"
  }
  ```

#### Change Password
- **URL:** `/users/password/reset/`
- **Method:** `POST`
- **Permissions:** `IsAuthenticated`
- **Request Body:**
  ```json
  {
    "oldPassword": "string",
    "newPassword": "string"
  }
  ```
- **Response:**
  ```json
  {
    "message": "Password changed successfully"
  }
  ```

### Token Endpoints

#### Create Access Token
- **URL:** `/token/access/`
- **Method:** `POST`
- **Permissions:** `AllowAny`
- **Request Body:**
  ```json
  {
    "username": "string",
    "password": "string"
  }
  ```
- **Response:**
  ```json
  {
    "access": "string"
  }
  ```

### Product Endpoints

#### Create New Product
- **URL:** `/products/create/`
- **Method:** `POST`
- **Permissions:** `IsAuthenticated`
- **Request Body:**
  ```json
  {
    "product_name": "string",
    "product_description": "string",
    "product_thumbnail": "string",
    "product_price": "float",
    "product_quantity": "int",
    "product_category": "string",
    "attributes": "json",
    "product_rating": "decimal",
    "product_variations": "json",
    "is_draft": "boolean",
    "is_published": "boolean"
  }
  ```
- **Response:**
  ```json
  {
    "id": "uuid",
    "product_name": "string",
    "product_description": "string",
    "product_thumbnail": "string",
    "product_price": "float",
    "product_quantity": "int",
    "product_category": "string",
    "attributes": "json",
    "product_rating": "decimal",
    "product_variations": "json",
    "is_draft": "boolean",
    "is_published": "boolean",
    "created_at": "datetime",
    "updated_at": "datetime"
  }
  ```

#### Get All Draft Products
- **URL:** `/products/draft/`
- **Method:** `GET`
- **Permissions:** `IsAuthenticated`
- **Query Parameters:**
  - `limit`: `int` (default: 10)
  - `page`: `int` (default: 1)
- **Response:**
  ```json
  [
    {
      "id": "uuid",
      "product_name": "string",
      "product_description": "string",
      "product_thumbnail": "string",
      "product_price": "float",
      "product_quantity": "int",
      "product_category": "string",
      "attributes": "json",
      "product_rating": "decimal",
      "product_variations": "json",
      "is_draft": "boolean",
      "is_published": "boolean",
      "created_at": "datetime",
      "updated_at": "datetime"
    }
  ]
  ```

#### Get All Published Products
- **URL:** `/products/published/`
- **Method:** `GET`
- **Permissions:** `IsAuthenticated`
- **Query Parameters:**
  - `limit`: `int` (default: 10)
  - `page`: `int` (default: 1)
- **Response:**
  ```json
  [
    {
      "id": "uuid",
      "product_name": "string",
      "product_description": "string",
      "product_thumbnail": "string",
      "product_price": "float",
      "product_quantity": "int",
      "product_category": "string",
      "attributes": "json",
      "product_rating": "decimal",
      "product_variations": "json",
      "is_draft": "boolean",
      "is_published": "boolean",
      "created_at": "datetime",
      "updated_at": "datetime"
    }
  ]
  ```

#### Draft a Product
- **URL:** `/products/draft/<uuid:product_id>/`
- **Method:** `POST`
- **Permissions:** `IsAuthenticated`
- **Response:**
  ```json
  {
    "id": "uuid",
    "product_name": "string",
    "product_description": "string",
    "product_thumbnail": "string",
    "product_price": "float",
    "product_quantity": "int",
    "product_category": "string",
    "attributes": "json",
    "product_rating": "decimal",
    "product_variations": "json",
    "is_draft": "boolean",
    "is_published": "boolean",
    "created_at": "datetime",
    "updated_at": "datetime"
  }
  ```

#### Publish a Product
- **URL:** `/products/published/<uuid:product_id>/`
- **Method:** `POST`
- **Permissions:** `IsAuthenticated`
- **Response:**
  ```json
  {
    "id": "uuid",
    "product_name": "string",
    "product_description": "string",
    "product_thumbnail": "string",
    "product_price": "float",
    "product_quantity": "int",
    "product_category": "string",
    "attributes": "json",
    "product_rating": "decimal",
    "product_variations": "json",
    "is_draft": "boolean",
    "is_published": "boolean",
    "created_at": "datetime",
    "updated_at": "datetime"
  }
  ```

#### Search Products
- **URL:** `/products/search/`
- **Method:** `POST`
- **Permissions:** `AllowAny`
- **Request Body:**
  ```json
  {
    "keyword": "string"
  }
  ```
- **Query Parameters:**
  - `limit`: `int` (default: 10)
  - `page`: `int` (default: 1)
- **Response:**
  ```json
  [
    {
      "id": "uuid",
      "product_name": "string",
      "product_description": "string",
      "product_thumbnail": "string",
      "product_price": "float",
      "product_quantity": "int",
      "product_category": "string",
      "attributes": "json",
      "product_rating": "decimal",
      "product_variations": "json",
      "is_draft": "boolean",
      "is_published": "boolean",
      "created_at": "datetime",
      "updated_at": "datetime"
    }
  ]
  ```

## Error Handling
Errors are returned in the following format:
```json
{
  "detail": "string"
}
```

- **400 Bad Request:** Invalid input or request.
- **404 Not Found:** Resource not found.
- **401 Unauthorized:** Authentication required or failed.

## Logging
All API activities are logged with the following format:
```plaintext
[LEVEL] [TIMESTAMP] [MODULE] [PROCESS_ID] [THREAD_ID] MESSAGE
```

## License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
