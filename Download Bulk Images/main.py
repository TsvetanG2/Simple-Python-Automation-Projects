import requests


def download_image(url, saved_folder):
    response = requests.get(url)
    if response.status_code == 200:
        images = response.json()

        for idx, image_url in enumerate(images):
            response_image = requests.get(image_url)

            if response_image.status_code == 200:
                with open(f"{saved_folder}/image_{idx}.jpg", "wb") as f:
                    f.write(response_image.content)


download_image(input("From which website would you like to perform bulk download of Images? "))
