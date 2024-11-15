import requests
import webbrowser

# Design your own program using the API above, it should have the following features:
# ● 2pts) Provide the user a list of commands that they can execute, including the option to
# quit the program
# ● 2pts) Add a feature to download an image of a specific dog breed. The function should
# take one parameter, a string representing the dog breed.
# ● 2pts) Add a feature to download an image of a random dog breed
# ● 2pts) Add a function to open a picture of a specific dog breed in your web browser.
# ● 2pts) Write good comments, and organize your code as multiple functions.

def list_breeds():
    url = "https://dog.ceo/api/breeds/list/all"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        breeds = data['message']
        print('List of Dog Breeds: ')
        for breed, subbreeds in breeds.items():
            if subbreeds:
                print(f"{breed}: {', '.join(subbreeds)}")
            else:
                print(f"{breed}")
    else:
        print('Failed to retrieve dog breeds.')
        
def download_breed(breed):
    url = "https://dog.ceo/api/breed/" + breed + "/images/random" 
    # concatenation of the breed into the url to access specific breed
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        image_url = data['message']
        img_response = requests.get(image_url)
        if img_response.status_code == 200:
            image_name = image_url.split("/")[-1]
            with open(image_name, 'wb') as file:
                file.write(img_response.content)
                print('Image saved as {a}'.format(a=image_name))
        else:
            print('Failed to save image.')
    else:
        print('Failed to retrieve dog URL. Are you sure that is a breed?')
        
def download_random():
    import requests
    url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        image_url = data['message']
        img_response = requests.get(image_url)
        if img_response.status_code == 200:
            image_name = image_url.split("/")[-1]
            with open(image_name, 'wb') as file:
                file.write(img_response.content)
                print("Image saved as {a}".format(a=image_name))
        else:
            print("Failed to save image.")
    else:
        print("Failed to retrieve dog URL. Are you sure that is a breed?")

def web_browser(breed):
    url = "https://dog.ceo/api/breed/" + breed + "/images/random"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        image_url = data['message']
        webbrowser.open(image_url)
    else:
        print('Failed to open image in web browser.')


def main():
    while True:
        print("""Welcome to the dog land, the place to go if you really love dogs.
            1. list breeds of dogs
            2. download image of a specific breed
            3. download image of a random breed
            4. open a picture of a specific dog breed in your browser
            5. quit dog land
            """)
        user = input()
        
        if user == "1":
            list_breeds()
        elif user == "2":
            ask = input('What breed are you looking for?')
            ask.capitalize
            download_breed(ask)
        elif user == "3":
            download_random()
        elif user == "4":
            ask2 = input("What breed are you looking for?")
            ask2.capitalize
            web_browser(ask2)
        elif user == "5":
            print('Thank you for using dog land.')
            return
        # no else function because if the user doesn't input a choice, should just loop
        # and offer the choices again

main()