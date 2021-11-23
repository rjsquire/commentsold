# COMMENTSOLD Code test

## Python / django web products / inventory solution

### To run:
1. Create a python virtual environment to run the application (I used 3.8.2)
2. Install requirements: `pip install -r requirements.txt` (use dev-requirements.txt if you want the flake8 dev tool)
3. Change into the cs_code directory: `cd cs_code`
4. Run the server: `python manage.py runserver`
5. Navigate to `http://localhost:8000` in your browser

### To simplify testing, the system uses sqlite.  This allows the entire database to be included in this git repository, and removes the need to run migrations.  However, it does bring some performance penalty.


### Features:
* Authentication: Any of the users in the data can log into the system using the email address and password provided. I used the default hashing provided by django rather than implementing a new password validator
* Products: An authenticated user can browse their products, and see the associated inventory.
	* From the product list the user can choose to view product details, or edit the product.  
	* When editing, the user is returned to the product detail view upon save or cancel.
* Inventory: An authenticated user can view their entire inventory.
	*  The inventory system can be filtered by product_id, sku, or the quantity present.
	*  Because of the data model, the inventory system does not show products that are not represented in inventory at all.  It would be a minor change to display all products.