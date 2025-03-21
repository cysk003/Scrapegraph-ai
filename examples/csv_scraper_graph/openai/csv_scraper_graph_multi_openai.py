"""
Basic example of scraping pipeline using CSVScraperMultiGraph from CSV documents
"""

import os

from dotenv import load_dotenv

from scrapegraphai.graphs import CSVScraperMultiGraph
from scrapegraphai.utils import prettify_exec_info

load_dotenv()
# ************************************************
# Read the CSV file
# ************************************************

FILE_NAME = "inputs/username.csv"
curr_dir = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(curr_dir, FILE_NAME)

with open(file_path, "r") as file:
    text = file.read()

# ************************************************
# Define the configuration for the graph
# ************************************************
openai_key = os.getenv("OPENAI_APIKEY")

graph_config = {
    "llm": {
        "api_key": openai_key,
        "model": "openai/gpt-4o",
    },
}

# ************************************************
# Create the CSVScraperMultiGraph instance and run it
# ************************************************

csv_scraper_graph = CSVScraperMultiGraph(
    prompt="List me all the last names",
    source=[str(text), str(text)],
    config=graph_config,
)

result = csv_scraper_graph.run()
print(result)

# ************************************************
# Get graph execution info
# ************************************************

graph_exec_info = csv_scraper_graph.get_execution_info()
print(prettify_exec_info(graph_exec_info))
