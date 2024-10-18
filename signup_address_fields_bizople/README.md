--> Install signup_address_fields_bizople
Module Name:
Signup Address Fields

-------------
Description:
The Signup Address Fields module enhances the Odoo signup process by adding additional fields related to the user's address, such as city, street, zip code, VAT number, and state. This ensures that users provide more detailed information during account creation. Additionally, the module supports the selection of the country and state during the signup process, improving the user experience for businesses requiring precise address information from their customers.  

------------- 
Copyright and License:
-*- coding: utf-8 -*-
Developed by Bizople Solutions Pvt. Ltd.
See LICENSE file for full copyright and licensing details.

-------------
Features:
- Extended Signup Form: Adds additional fields to the signup form including:
City, Street, ZIP Code, VAT Number, Country, State

- VAT Validation Based on Company Type: Depending on whether the user is signing up as a person or a company, the VAT field will either be required or not.

- Country Dropdowns: Provides users with the ability to select their country from pre-existing options, ensuring that valid and recognized regions are selected.

- Automatic Email Notifications: Sends a confirmation email to the user upon successful signup, informing them that their account has been created.

---------			
Usage:
1. Selecting Signup Fields:
- The module captures the following fields during the signup process: Login (email), Name, VAT (optional for personal accounts), City, Street, ZIP Code, Country, Password and password confirmation.

2. How to Use the Signup Form:
- A user fills out the signup form by providing their login, name, address details, and password. The form also validates that the password and confirmation password match.
- If the user selects "company" as their company type, they must also provide their VAT number.

3. Country Selection:
- Upon reaching the signup form, users can select their country from dropdown lists populated with valid options from Odoo’s res.country models.
Handling Signup Token:

4. Signup Error Handling:
- If any error occurs during signup (such as a password mismatch or an already registered email), the module displays an appropriate error message to the user.