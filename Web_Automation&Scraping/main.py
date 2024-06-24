from playwright.sync_api import sync_playwright
import bs4

def store_scraped_txt_data(data, mode):
        with open("scraped_data.txt", mode) as txt_file:
            txt_file.write(data)

def store_scraped_html(file_name, data):
     with open(f"{file_name}", "w") as html_file:
        html_file.write(data)

def html_parsing(tag):
    page_html = page.inner_html(tag)
    soup = bs4.BeautifulSoup(page_html, "lxml")
    return soup


with sync_playwright() as p:
    #launching browser and web-site page
    browser = p.firefox.launch(headless=False, slow_mo=100)
    page = browser.new_page()
    page.goto("https://www.celtx.com/")

    #login in and entering the web-site
    page.get_by_role("link", name="Login").click()
    page.wait_for_url("https://www.celtx.com/a/ux/logon")
    page.wait_for_timeout(5000)
    page.get_by_role("textbox", name="email").fill("egoroff2206@gmail.com")
    page.get_by_role("textbox", name="password").fill("Denisko2004")
    page.get_by_role("button", name="Log In").click()
    page.get_by_role("link", name="Profile").click()

    #parsing and storing html
    soup = html_parsing("id=cxContent")
    html = soup.prettify()
    store_scraped_html("profile_scraped_data.html", html)

    #scraping text data and storing into a txt file
    profile_block_content = soup.find("div", {"class": "profile-block-content"}).get_text(" ")
    store_scraped_txt_data(f"Profile block content: {profile_block_content}", "w")

    #following the next page
    page.get_by_title("Projects", exact=True).click()
    page.wait_for_timeout(2000)

    #parsing and storing html
    soup = html_parsing("id=scroll-container")
    html = soup.prettify()
    store_scraped_html("projects_scraped_data.html", html)

    #scraping text data and storing into a txt file
    project_list_item = soup.find("div", {"class":"projectlistitem-details"}).get_text(" ")
    store_scraped_txt_data(f"\nProject name and details: {project_list_item}", "a")

    #following the next page
    page.get_by_title("Management", exact=True).click()
    page.wait_for_timeout(2000)

    #parsing and storing html
    soup = html_parsing("id=nonfilelist-container")
    html = soup.prettify()
    store_scraped_html("management_scraped_data.html", html)
    
    #scraping text data and storing into a txt file
    member_since = soup.find("div", {"class": "creating-since"}).get_text(" ")
    store_scraped_txt_data(f"\n{member_since}\n", "a")

    #scraping headings from every page and storing into txt file
    for page_num in range(1, 10):
        page.goto(f"https://blog.celtx.com/category/scriptwriting/page/{page_num}/")
        soup = html_parsing("body")
        data = soup.find_all("h2", class_="penci-entry-title entry-title grid-title")
        for heading in data:
            refined_data = f"\n{heading.get_text()}\n"
            store_scraped_txt_data(refined_data, "a")
         
    #page.wait_for_timeout(1000)
    browser.close()