# FTP-Selenium
News Scraper and Document Creator


News Scraper and Document Creator: Code Explanation    
: Overview

This system consists of three Python scripts that work together to scrape news from websites, create a Word document with the scraped content, and transfer the document to a server. The three main components are:
1. main1.py: This Python script is designed to scrape news from a website, create a document with the news content, and then send that document to a server.
2. server.py: This python script main purpose is to act like a digital mailbox. It allows the main script to create files and then safely store them on the computer.
3. utilitis.py:  This python script main purpose is creating reusable tools for web scraping tasks, which can be very helpful in various data collection

main1.py
Imports and Setup:

The script starts by importing necessary libraries:
selenium: For web scraping.
webdriver_manager: For managing the Chrome WebDriver.
 docx: For creating Word documents.
 socket: For network communication.
subprocess and threading: For running the server script.
argparse: For parsing command-line arguments.




:Command-line Argument Parsing
The script uses argparse to allow users to specify which news site to scrape
- site or --s: Required argument to choose the site ('y' for Ynet, 'm' for Mako, 'c' for CNN)

:Server Management
Two functions manage the server:
 1.run_server(): Starts the server script as a subprocess.
 A threading mechanism to run the server in the background..2

File Transfer:
The send_file(filename, file_path) function handles sending the created document to the server:
Establishes a socket connection to the server.
Sends the filename and file size.
. Transfers the file data

Web Scraping and Document Creation
The main part of the script:
1.Configures Chrome to run headless (without UI).
. 2.Initializes the WebDriver and navigates to the chosen news site
3.Uses functions from utilitis.py to scrape headings and paragraphs.
. 4.Creates a Word document with the scraped content
5.Saves the document temporarily.
6.Sends the document to the server.
7.Cleans up temporary files and closes the WebDriver.



Cleanup
The script terminates the server subprocess and joins the server thread at the end.

server.py

File Reception:
The receive_file(conn, save_path) function handles incoming files:
. 1.Receives the filename and file size
. 2.Creates the file in the specified save directory
. 3.Receives and writes the file data

Server Loop:
The main server loop:
. .Sets up a socket to listen for connections1
2.Accepts incoming connections.
. 3.Calls `receive_file()` for each connection
. 4.Closes the connection and waits for the next one

utilitis.py
This script contains two main functions:
:find_headings(driver, num_headings=3)
  Searches for heading tags (h1 to h6) in the webpage and 
. Returns the text of the first  num_headings  found

:find_paragraphs(driver, num_paragraphs=3)
Finds all paragraph tags in the webpage and
Returns the text of the first  num_paragraphs found.

Both functions use Selenium's WebDriver to interact with the webpage and extract content.

How It All Works Together

1. The user runs main1.py with a command-line argument specifying the news site.
. main1.py starts server.py in a separate thread.2
. main1.py uses Selenium to scrape the specified news site.3
. The scraped content is formatted into a Word document.4
. The document is sent to the server using a socket connection.5
. server.py receives the document and saves it in a specified directory.6
. main1.py cleans up resources and terminates the server.7

This system allows for automated news scraping and document creation, with the resulting file stored on a separate server process.








