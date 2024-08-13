
# Loan Approval Prediction Model

This is a loan approval prediction model. Application gets input from html form and uses model prediction and print them into user interface.

## 1.Method: Run on Docker without building

* Download project: git clone https://github.com/ahmetkilinctr/Loan-Approval-Model.git <br />
cd flask-iris-classification 

### Step 1: Run docker

docker run --rm -d -p 8080:8080 ahbekadabra/loan_app:2024-08

### Step 2: Open browser and run app

http://localhost:8080

## 2.Method: Build docker image and container
### Step 1: Get image

docker pull ahbekadabra/loan_app:2024-08

### Step 2: Create container

docker run -p 8080:8080 -d ahbekadabra/loan_app:2024-08

### Step 3: Open browser and run app 

http://localhost:8080

## App Screenshots

### Input Form
![Ekran Resmi 2024-08-13 21 43 32](https://github.com/user-attachments/assets/989e551d-30d2-4d4c-a933-67dcf0373fe3)

### Result Page
![Ekran Resmi 2024-08-13 21 50 16](https://github.com/user-attachments/assets/72fdb55b-e5b8-42cc-8cc1-78785fb6c176)

