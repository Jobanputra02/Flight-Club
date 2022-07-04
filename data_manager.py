import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/18bfe0916b078433bf7ec50ef0a373a4/pythonFlightDeals/prices"
SHEETY_USERS_ENDPOINT = "https://api.sheety.co/18bfe0916b078433bf7ec50ef0a373a4/pythonFlightDeals/users"


class DataManager:

    def __init__(self):
        self.customer_data = None
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "sheet1": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def new_user(self):
        print("Welcome to the Flight CLub!")
        print("First rule of Flight Club, you don't talk about flight club.")
        f_name = input("Please enter your first name : ")
        l_name = input("Please enter your last name : ")
        email = input("Please enter your email : ")
        email_again = input("Please enter your email again : ")

        if email == email_again:
            new_user = {
                "user": {
                    "firstName": f_name,
                    "lastName": l_name,
                    "email": email,
                }
            }
            requests.post(url=SHEETY_USERS_ENDPOINT, json=new_user)
            print("Congrats! Welcome to the fight club.")
        else:
            print("Please check your details and enter again.")

    def get_customer_emails(self):
        customers_endpoint = SHEETY_USERS_ENDPOINT
        response = requests.get(customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
