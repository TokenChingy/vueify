from bs4 import BeautifulSoup

import glob
import os
import sys


def main(export_path):
    os.chdir(export_path)

    for html_file in glob.glob("**/*.html", recursive=True):
        html_file_handle = open(html_file, "r+")
        html_soup = BeautifulSoup(html_file_handle, "html.parser")
        html_body = html_soup.find("body")
        html_body.name = "template"
        html_file_handle.close()

        try:
            vue_file_handle = open(f"{html_file.split('.')[0]}.vue", "r+")
            vue_soup = BeautifulSoup(vue_file_handle, "html.parser")
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
        except:
            vue_file_handle = open(f"{html_file.split('.')[0]}.vue", "w+")
            vue_soup = BeautifulSoup(vue_file_handle, "html.parser")
            vue_soup.insert(0, BeautifulSoup("<!-- HTML -->", "html.parser"))
            vue_soup.insert(1, html_body)
            vue_soup.append(BeautifulSoup(
                "<!-- JS --><script>export default {}</script>", "html.parser"))
            vue_soup.append(BeautifulSoup(
                "<!-- CSS --><style scoped></style>", "html.parser"))
            vue_file_handle.write(vue_soup.prettify(formatter="html5"))
            vue_file_handle.close()

        os.remove(html_file)

    return


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print(f"Usage: {sys.argv[0]} export_path")
