"""Helper functions for the site"""

from datetime import datetime

def make_post(title, content):
    """Makes a post in the _posts file"""
    time = datetime.now()
    print(time)
    date = time.strftime("%Y-%m-%d")
    filename = date + "-post.md"
    filepath = "docs/_posts/" + filename
    file_str = "---\n"
    file_str += "layout: post\n"
    file_str += f'title:  "{title}"\n'
    file_str += f"date:   {date} 12:00:00 -0400\n"
    file_str += "categories: jekyll update\n"
    file_str += "---\n\n"
    file_str += content
    f = open(filepath, "w")
    f.write(file_str)
    f.close()