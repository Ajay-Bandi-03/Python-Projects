# import requests

import requests


def get_exchange_rate(base_currency, target_currency):
    """Fetches the exchange rate from base_currency to target_currency."""
    api_url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()

        if target_currency in data['rates']:
            return data['rates'][target_currency]
        else:
            print(f"Currency {target_currency} is not available.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None


def convert_currency(amount, base_currency, target_currency):
    """Converts the given amount from base_currency to target_currency."""
    rate = get_exchange_rate(base_currency, target_currency)
    if rate is not None:
        return amount * rate
    else:
        return None


if __name__ == "__main__":
    print("Currency Converter")
    base_currency = input("Enter the base currency (e.g., USD): ").upper()
    target_currency = input("Enter the target currency (e.g., EUR): ").upper()
    try:
        amount = float(input(f"Enter the amount in {base_currency}: "))
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        exit()

    converted_amount = convert_currency(amount, base_currency, target_currency)

    if converted_amount is not None:
        print(f"{amount:.2f} {base_currency} = {converted_amount:.2f} {target_currency}")
    else:
        print("Conversion failed. Please try again.")
