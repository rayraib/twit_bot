#!/usr/bin/python3
import requests

def get_quote():
	url = "https://quotes.rest/qod?category=inspire"
	response = requests.get(url)
	text = response.json()["contents"]["quotes"][0]["quote"]
	return (text)
if __name__ == "__main__":
	get_quote()
