import bs4, requests, json, os, sys, re, html, argparse
from bs4 import BeautifulSoup

URL = "http://acse.pub.ro/people/academic-personnel/"
OUTPUT_FILENAME = "acse_prof_info.json"


def retrieve_details_page_teacher_data(profileLink):
    details_soup = BeautifulSoup(requests.get(profileLink).content, 'html.parser', from_encoding='utf-8')
    teacher_name = details_soup.find("h1", {"class": "entry-title"}).text
    academic_title = details_soup.find("span", {"class": "academic-title"}).text
    parent_div = details_soup.find("div", {"class": "single-entry-content"})
    p_list = parent_div.findChildren("p")

    mail = {}
    mail["name"] = teacher_name
    mail["title"] = academic_title
    mail["email"] = p_list[0].text.split(':')[1].replace(" dot ", ".").replace(" at ", "@")

    if len(p_list) >= 2:
        try:
            mail["office"] = p_list[1].text.split(':')[1]
        except:
            mail["office"] = ""
    else:
        mail["office"] = ""

    if len(p_list) >= 3:
        try:
            mail["interfon"] = p_list[2].text.split(':')[1]
        except:
            mail["interfon"] = ""
    else:
        mail["interfon"] = ""

    return mail


def retrieve_main_page_teacher_data(dom_element):
    # convert each li to a specific soup for simplicity
    teacher_soup = BeautifulSoup(str(dom_element.prettify()), 'html.parser')

    anchor_profile_link = teacher_soup.find('a')['href']
    image_profile_link = teacher_soup.find('a').find('img')['src']

    print(f"Processing: {anchor_profile_link} ...")

    teacher = retrieve_details_page_teacher_data(anchor_profile_link)
    teacher["profile_link"] = anchor_profile_link
    teacher["image_link"] = image_profile_link

    return teacher


def find_all_teacher_names_on_main_page(soup):
    people_uls = soup.find_all("ul", {"class": "people"})
    info = []
    for ul in people_uls:
        for li in ul.findAll('li'):
            info.append(retrieve_main_page_teacher_data(li))
            # break
        # break
    return info


def get_info():
    soup = BeautifulSoup(requests.get(URL).content, 'html5lib')

    print(soup.title.string)  # Academic personnel | ACSE Department

    return find_all_teacher_names_on_main_page(soup)

    # return [{'name': 'Mihai'}]


def write_json_info_to_file():
    print("Writing results to json file...")
    parser = argparse.ArgumentParser(description="Extract information about ACSE teachers.")
    parser.add_argument('--output', help=f'File to output to. Default: {OUTPUT_FILENAME}', default=OUTPUT_FILENAME)

    args = parser.parse_args()

    with open(args.output, 'w', encoding='utf-16') as f:
        f.write(json.dumps(get_info()))


if __name__ == '__main__':
    write_json_info_to_file()