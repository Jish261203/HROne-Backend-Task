﻿# HROne-Backend-Task

## Overview
This project is a sample backend application for an e-commerce platform, built with FastAPI and MongoDB, as per the HROne Backend Intern Hiring Task requirements.

## Features
- **Create Product**: POST /products — Add a new product with name, price, and available sizes/quantities.
- **List Products**: GET /products — List products with optional filters (name, size), pagination, and assignment-compliant response structure.
- **Create Order**: POST /orders — Place an order for one or more products (user_id can be hardcoded).
- **List Orders**: GET /orders/{user_id} — List all orders for a user, with product details joined in each order item, and pagination.

## Tech Stack
- **Python 3.10+**
- **FastAPI** for API framework
- **MongoDB** (with Motor for async access)

## Project Structure
```
E-commerce backend/
  app/
    main.py            # FastAPI app entry point
    database.py        # MongoDB connection setup
    config.py          # Configuration (Mongo URI, DB name)
    models/            # Data serialization helpers
    schemas/           # Pydantic models for request/response
    routes/            # API route definitions
      products.py      # Product endpoints
      orders.py        # Order endpoints
```

## How to Run
1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
2. **Set up MongoDB**:
   - Use MongoDB Atlas M0 Free Plan or a local MongoDB instance.
   - Set your MongoDB URI and DB name in `app/config.py`.
3. **Run the server**:
   ```bash
   uvicorn app.main:app --reload
   ```
4. **API Docs**:
   - Visit [http://localhost:8000/docs](http://localhost:8000/docs) for interactive Swagger UI.

## Assignment Compliance
- All endpoints, request/response formats, and pagination match the assignment spec.
- Product list omits sizes in the response, as required.
- Order list includes product details for each item.
- MongoDB is used for all data storage.
- Code is clean, modular, and well-documented.

## Example Requests
- See the assignment PDF for example request/response bodies.

---
