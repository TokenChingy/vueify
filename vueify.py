from bs4 import BeautifulSoup


import glob
import os
import sys


def main(export_path):
    os.chdir(export_path)

    for html_file in glob.glob("**/*.html", recursive=True):
        # HTML
        html_file_handle = open(html_file, "r+")
        html_soup = BeautifulSoup(html_file_handle, "html.parser")
        html_body = html_soup.find("body")

        html_wrapper = html_soup.new_tag("div")

        for html_tag in reversed(html_body.contents):
            html_wrapper.insert(0, html_tag.extract())

        html_body.append(html_wrapper)

        [script.extract() for script in html_soup.findAll("script")]
        html_body.name = "template"
        html_file_handle.close()

        # CSS
        css_clean_name = html_file.split('\\')[-1].replace('.html', '.css')
        css_soup = None

        try:
            css_file_handle = open(f"./assets/css/{css_clean_name}", "r+")
            css_soup = BeautifulSoup(css_file_handle, "html.parser")
            css_file_handle.close()
        except:
            css_soup = BeautifulSoup("", "html.parser")

        # Vue
        vue_soup = []
        vue_style_tags = []

        try:
            vue_file_handle = open(f"{html_file.split('.')[0]}.vue", "r+")
            vue_soup = BeautifulSoup(vue_file_handle, "html.parser")
            vue_style_tags = vue_soup.findAll("style")
        except:
            vue_soup = BeautifulSoup("", "html.parser")

        if len(vue_soup) > 0:
            if len(vue_style_tags) > 0:
                style_wrapper = vue_soup.new_tag("style")

                for style in reversed(css_soup.contents):
                    style_wrapper.insert(0, style.extract())

                vue_style_tags[0].extract()
                vue_soup.append(style_wrapper)

            vue_template_tags = vue_soup.findAll("template")

            if len(vue_template_tags) > 0:
                vue_template_tags[0].replaceWith(html_body)
            else:
                vue_soup.insert(0, BeautifulSoup(
                    "<!-- HTML -->", "html.parser"))
                vue_soup.insert(1, html_body)

            vue_file_handle.close()
            vue_file_handle = open(f"{html_file.split('.')[0]}.vue", "w+")
            vue_file_handle.write(vue_soup.prettify(formatter="html5"))
            vue_file_handle.close()
        else:
            vue_file_handle = open(f"{html_file.split('.')[0]}.vue", "w+")
            vue_soup = BeautifulSoup(vue_file_handle, "html.parser")
            vue_soup.insert(0, BeautifulSoup("<!-- HTML -->", "html.parser"))
            vue_soup.insert(1, html_body)
            vue_soup.append(BeautifulSoup(
                "<!-- JS --><script>export default {}</script>", "html.parser"))
            vue_soup.append(BeautifulSoup(
                f"<!-- CSS --><style scoped>{css_soup.prettify(formatter=None)}</style>", "html.parser"))
            vue_file_handle.write(vue_soup.prettify(formatter="html5"))
            vue_file_handle.close()

        os.remove(html_file)

    return


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print(f"Usage: {sys.argv[0]} export_path")
