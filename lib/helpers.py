"""Helper methods to generate webpage"""

from datetime import date

def _page_header(title) -> str:
    """REturns the header for a .md page"""
    page_str: str = "---\nlayout: default\n"
    page_str += f"title: {title}\n"
    page_str += "contributors: Alyssa Byrnes\n---\n\n"
    page_str += "# " + title + "\n\n"
    return page_str

def _link_dict_to_md(links: dict[str,str]) -> str:
    """Converts a dict of links to an md list"""
    link_str = ""
    for title in links:
        if len(links[title]) > 0:
            link_str += f"[{title}]({links[title]}), "
        else: #not a link
            link_str += f"{title}, "
    return link_str[:-2]

def lesson_page(title: str, topics: list[dict]):
    """Generate a page for a day's lessons"""
    # Make Page
    page_info: str = _page_header(title)
    location = "../docs/calendar/"
    page_title = title.lower()
    page_title = page_title.replace(",", "")
    page_title = page_title.replace(" ", "-") + ".md"
    for topic in topics:
        title = topic['title']
        links = _link_dict_to_md(topic['links'])
        page_info += f"* {title}: {links}\n"
    f = open(location + page_title, "w")
    f.writelines(page_info)
    f.close()
    print("Page made: " + "/calendar/" + page_title )

def update_calendar(page_title: str, date):
    """Update a date on the calendar""" 
    #TODO
    return 0