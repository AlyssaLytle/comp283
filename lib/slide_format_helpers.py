"""Functions to Modify A Slide Deck"""

THEME = "dracula"
AUTHOR = "Alyssa Byrnes"

def format(file_name):
    """Steps through slide deck and makes format modifications"""
    # Make str to store new slide deck
    slides: str = ""
    # Break file into slides
    old_slides = _make_slide_list(file_name)
    print(old_slides)
    # If slides have header, copy it over
    if _has_header(old_slides):
        slides += old_slides[0]
        old_slides.pop(0)
    else:
        # Otherwise, make a header
        slides += _make_header(file_name)
    # Make modification to the remaining slides
    for slide in old_slides:
        slides += _add_div(slide)
    # Write New Slides
    fname = "slides/" + file_name
    f = open(fname, "w")
    f.writelines(slides)
    f.close()
   

def _make_slide_list(file_name: str) -> list[str]:
    """Reads file fname and makes a list of slides"""
    # Read file
    fname = "slides/" + file_name
    f = open(fname, "r")
    lines = f.readlines()
    f.close()
    slides: list[str] = []
    curr_slide: str = ""
    for line in lines:
        if line[:3] == "## ":
            slides.append(curr_slide)
            curr_slide = line
        else:
            curr_slide += line
    return slides

def _make_header(file_name) -> str:
    """Returns YAML header for slide"""
    title = file_name.split("/")[-1]
    title = title[:-3]
    header = "---\n"
    header += f"title: {title}\n"
    header += f"theme: {THEME}\ncenter: false\ntransition: 'none'\n"
    header += f"contributors: {AUTHOR}\n---\n\n"
    return header

def _has_header(slide_list) -> bool:
    """Returns true if slide already has a YAML header"""
    line0 = slide_list[0]
    if "---" in line0:
        return True
    else:
        return False
    
def _has_div(slide: str) -> bool:
    """If a slide has a div box in it already, don't add any."""
    return ("div" in slide)
    
def _add_div(slide: str) -> bool:
    "Puts text of slide in div box"
    new_slide = ""
    slide_list = slide.split("\n")
    new_slide += slide_list[0] + "\n"
    if not _has_div(slide):
        div_str = '<div id="content">\n'
        new_slide += div_str
    for s in slide_list[1:]:
        new_slide += s + "\n"
    if not _has_div(slide):
        new_slide += "</div>\n\n\n"
    return new_slide
        
    