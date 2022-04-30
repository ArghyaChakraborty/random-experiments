import sys
import requests

EBOOK_HUNTER_BASE_URL = "https://ebook-hunter.org/Books/"
BOOK_TITLES = [
    "Embracing the Power of AI by Globant"
]

def main(argv: list):
    global BOOK_TITLES
    collect_book_title = False if len(argv) >= 2 and argv[1].lower() == "n" else True

    # Take book titles to look for
    while(collect_book_title):
        title = input("Enter a book title to look for. Press N/n if no more book titles need to be entered:\n")
        if title.strip() == "" and len(BOOK_TITLES) == 0:
            print("Sorry but you have not entered even a single book title. Need at least 1 book title to start searching")
        else:
            if title.strip().lower() == "n":
                collect_book_title = False
            else:
                BOOK_TITLES.append(title)

    print("Gotchya. Here are the list of titles to look for so far")
    print(BOOK_TITLES)

    # Start searching
    current_page = 1
    while(True):
        current_page_url = EBOOK_HUNTER_BASE_URL + str(current_page)
        print("--------------------------------")
        print("Looking for "+BOOK_TITLES[0]+" in "+current_page_url)

        response = requests.get(current_page_url)
        if response.status_code == 200:
            if BOOK_TITLES[0] in response.text:
                print("Found "+BOOK_TITLES[0]+" in "+current_page_url)
                print("Looking for the remaining titles in the same page")
                match_found = 1
                for i, title in enumerate(BOOK_TITLES):
                    if i > 0:
                        if title in response.text:
                            print("Found "+title+" in "+current_page_url)
                            match_found += 1
                        else:
                            print("NOT Found "+title+" in "+current_page_url)
                print("Found "+str(match_found)+"/"+str(len(BOOK_TITLES))+" matches")
                print("You can start from here")
                print("")
                print(current_page_url)
                break
            else:
                print("NOT Found "+BOOK_TITLES[0]+" in "+current_page_url+". Will continue in the next page")
                current_page += 1
        else:
            print("Some error occured. Please check whether the site is up & running. Status Code: "+str(response.status_code)+", Response: "+response.text)


if __name__ == "__main__":
    main(sys.argv)
