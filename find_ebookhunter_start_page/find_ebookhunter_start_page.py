import sys
import requests

EBOOK_HUNTER_BASE_URL = "https://ebook-hunter.org/Books/"

def main(argv: list):
    book_titles = []
    collect_book_title = True

    # Take book titles to look for
    while(collect_book_title):
        title = input("Enter a book title to look for. Press N/n if no more book titles need to be entered:\n")
        if title.strip() == "" and len(book_titles) == 0:
            print("Sorry but you have not entered even a single book title. Need at least 1 book title to start searching")
        else:
            if title.strip().lower() == "n":
                print("Gotchya. Here are the list of titles to look for so far")
                print(book_titles)
                collect_book_title = False
            else:
                book_titles.append(title)
    

    # Start searching
    current_page = 1
    while(True):
        current_page_url = EBOOK_HUNTER_BASE_URL + str(current_page)
        print("--------------------------------")
        print("Looking for "+book_titles[0]+" in "+current_page_url)

        response = requests.get(current_page_url)
        if response.status_code == 200:
            if book_titles[0] in response.text:
                print("Found "+book_titles[0]+" in "+current_page_url)
                print("Looking for the remaining titles in the same page")
                match_found = 1
                for i, title in enumerate(book_titles):
                    if i > 0:
                        if title in response.text:
                            print("Found "+title+" in "+current_page_url)
                            match_found += 1
                        else:
                            print("NOT Found "+title+" in "+current_page_url)
                print("Found "+str(match_found)+"/"+str(len(book_titles))+" matches")
                print("You can start from here")
                print("")
                print(current_page_url)
                break
            else:
                print("NOT Found "+book_titles[0]+" in "+current_page_url+". Will continue in the next page")
                current_page += 1
        else:
            print("Some error occured. Please check whether the site is up & running. Status Code: "+str(response.status_code)+", Response: "+response.text)


if __name__ == "__main__":
    main(sys.argv)
