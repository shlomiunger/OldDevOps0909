import requests

def write_names():
    my_file = open("names.txt", "w")
    for name in range(3):
        current_name = input("Name: ")
        my_file.write(current_name + "\n")
    my_file.close()


def greet_names():
    my_file = open("names.txt", "r")
    names = my_file.readlines()
    for name in names:
        print(f"Hello {name}")
    my_file.close()


def read_url():
    my_file = open("urls.txt", "r")
    urls = my_file.readlines()
    urls = [line[:-1] for line in urls]
    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"{url}, status: {response.status_code}")
    my_file.close()


# write_names()
#
# greet_names()

read_url()
