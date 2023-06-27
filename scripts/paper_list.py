"""
Convenience script to generate the list of papers in workshop sessions.
"""
import os
import csv
import argparse
from collections import defaultdict

POSTER_SESSIONS_HUMAN_READABLE = {
    "IP2" : "In-Person Poster Session 2",
    "IP1" : "In-Person Poster Session 1",
    "V1" : "Virtual Poster Session 1",
    "V2" : "Virtual Poster Session 2",
}
POSTER_SESSIONS_ORDERED = ["Virtual Poster Session 1", "Virtual Poster Session 2", "In-Person Poster Session 1", "In-Person Poster Session 2",]

parser = argparse.ArgumentParser()
parser.add_argument(
    "--papers", type=str, help="CSV file with papers.",
)

def read_papers_csv(args):
    papersdict = defaultdict(list)
    with open(args.papers) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            session = POSTER_SESSIONS_HUMAN_READABLE[row["Assignment"]]
            title = row["Title"]
            authors = row["Authors"]
            submission_type = row["Submission Type"]
            oral = True if "Oral" in row["Oral"] else False
            papersdict[session].append({
                "title" : title,
                "authors" : authors,
                "submission_type" : submission_type,
                "oral" : oral
            })
    return papersdict

def format_submission_type(paper):
    if paper['oral']:
        return f'<span style="color:#DD3333;font-weight:700">[Oral, {paper["submission_type"]}]</span>'
    else:
        return f'<span>[{paper["submission_type"]}]</span>'

def output_papers_formatted(papers_dict):
    html = ""
    for poster_session in POSTER_SESSIONS_ORDERED:
        papers_sorted = sorted(papers_dict[poster_session], key = lambda x: x['title'])

        html += f"<h3>{poster_session}</h3>"
        html += '\n<ul class="paper-list">'
        for paper in papers_sorted:
            html += "\n<li>\n"
            # Paper title
            html += '<span class="paper-title">' + format_submission_type(paper) + paper['title'] + '</span><br>\n'

            html += f'<span class="paper-authors">{paper["authors"]}</span><br>\n'
            html += "\n</li>\n"
        html += "</ul>\n\n"
    print(html)

def main():
    args = parser.parse_args()
    papers_dict = read_papers_csv(args)
    output_papers_formatted(papers_dict)

if __name__ == "__main__":
    main()