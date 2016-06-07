import os


def add_md(content):
    slide = "<section data-markdown>\n"
    slide += """<script type="text/template">\n"""
    slide += content + "\n"
    slide += "</script>\n"
    slide += "</section>\n"
    return slide

def add_html(content):
    slide = "<section>\n"
    slide += content + "\n"
    slide += "</section>\n"
    return slide


template_file = "index.html.template"
output_file = "index.html"

presentation_content = ""

for directory in sorted(os.listdir("content")):
    directory = os.path.join("content", directory)
    presentation_content += "\n<section>\n"
    # presentation_content += "\n<section data-markdown>\n"
    for slide in sorted(os.listdir(directory)):

        if slide.startswith("."):
            continue

        slide_file = os.path.join(directory, slide)

        with open(slide_file, 'r') as fd:
            slide_content = fd.read()
            if slide_file.endswith(".md"):
                presentation_content += add_md(slide_content)
            elif slide_file.endswith(".html"):
                presentation_content += add_html(slide_content)

    presentation_content += "</section>\n"

# print presentation_content
with open(template_file, 'r') as fd_template, \
     open(output_file, 'w') as fd_out:
    data = fd_template.read()
    data = data.replace("{{{TO_REPLACE}}}", presentation_content)
    fd_out.write(data)
