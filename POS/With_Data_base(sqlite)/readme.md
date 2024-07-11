# POS-v8.0

## Overview

The POS (Point of Sale) system is designed to streamline the sales process in retail environments. It helps manage inventory, process transactions, and generate sales reports. This POS system is implemented in Python and is easy to configure and extend.

## Key Features

- **Order Processing**: Handle customer orders and transactions seamlessly.
- **Database Integration**: Maintain persistent storage of data using SQLITE.
- **User Interface**: Simple and intuitive interface for ease of use.
- **Theme Change**: You can Use Light theme as well as Aesthetic dark Theme.
- **Modify Item**: You can change the Price of any Item again.
- **Generate Sales Report**: You can Generate Report of your Sales.

## Folder Structure

POS-v7.0/

├── START.pyw

├── class_item.py

├── class_order.py

├── class_cashier.py

├── data.py

├── database_handler_item.py

├── database_handler_order.py

├── database_handler_cashier.py

├── Items.db

├── Orders.db

├── Cashiers.py

├── program.pyw

├── report_generator.pyw



### File Descriptions

- **START.pyw**: The main entry point of the POS application.
- **class_item.py**: Contains the `Item` class which defines product attributes and methods.
- **class_order.py**: Contains the `Order` class to manage customer orders.
- **class_cashier.py**: Contains the `Cashier` class to manage Cashiers.
- **data.py**: Contains Program Settings.
- **database_handler_item.py**: Handles database operations such as read/write functions for Items.
- **database_handler_order.py**: Handles database operations such as read/write functions for Orders.
- **database_handler_cashier.py**: Handles database operations such as read/write functions for Cashiers.
- **Items.db**: Contains Item table that store all Items.
- **Orders.db**: Contains Order table that store all Orders.
- **Cashiers.db**: Contains Cashier table that store all Cashiers.
- **program.pyw**: GUI implementation for the POS system.
- **report_generator.pyw**: You can Generate Report of your Complete Sales or between a date range.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Maaz-319/Python/tree/POS-v8.0/POS
    ```
2. Navigate to the project directory:
    ```sh
    cd POS-v8.0
    ```
3. Install required dependencies:
    ```sh
    pip install -r readme.md
    ```

## Usage

1. Start the application:
    ```sh
    python START.pyw
    ```
2. Follow the on-screen instructions to navigate through the POS system.
3. Manage inventory, process orders, and view reports through the provided interface.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch:
    ```sh
    git checkout -b feature-branch
    ```
3. Commit your changes:
    ```sh
    git commit -m 'Add some feature'
    ```
4. Push to the branch:
    ```sh
    git push origin feature-branch
    ```
5. Open a pull request.

## Contact

For any questions or issues, please contact:

- **Maaz**: [GitHub Profile Maaz-319](https://github.com/Maaz-319)

## Screenshots

*Sign In*
![image](https://github.com/Maaz-319/Python/assets/83403349/34da8505-fcc5-4a4a-9466-9540c523540c)

*Apllication Preview*
![image](https://github.com/Maaz-319/Python/assets/83403349/0615041d-8676-4382-aa99-af75180a08fd)

*Dark Theme*
![image](https://github.com/Maaz-319/Python/assets/83403349/a299ba14-771a-45f5-aa9d-9c79d778709b)

*Order Placing*
![image](https://github.com/Maaz-319/Python/assets/83403349/04c15e9f-453e-4119-9f9c-ed7c8fa1f542)

*Add New Items*
![image](https://github.com/Maaz-319/Python/assets/83403349/20cc5f18-e903-4dd1-8ac4-15dd2b461533)

*Modifying Item*
![image](https://github.com/Maaz-319/Python/assets/83403349/eaee4c8a-eef7-4243-b2ff-9e1049986f41)

*Basic Error Handeling*
![image](https://github.com/Maaz-319/Python/assets/83403349/c2fe3f83-8554-4b08-9445-2721bd5ff298)

*Sales Report*
![image](https://github.com/Maaz-319/Python/assets/83403349/8a50017f-f09f-439b-a09c-54f79071aea0)

*[Video Preview](https://drive.google.com/file/d/1xuRiCs1ytBF1gjOfgYDgkjLyP-GTCiEC/view?usp=sharing)*
---
