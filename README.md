<!DOCTYPE html>
<html>

<body>

  <h1>Job Posts Web Scraper</h1>

  <h2>Overview</h2>

  <p>This Python script is a simple web scraper designed to extract job posts information from the <a
      href="https://www.brightermonday.co.ke/jobs">BrighterMonday Kenya</a> website. It utilizes the BeautifulSoup
    library for HTML parsing and the Requests library for making HTTP requests. The extracted information includes job
    position, company name, and job function.</p>

  <h2>Features</h2>

  <ul>
    <li>Scrapes job posts from BrighterMonday Kenya website.</li>
    <li>Saves job information in individual text files in the 'job posts' directory.</li>
    <li>Displays a desktop notification when the script finishes refreshing.</li>
  </ul>

  <h2>Prerequisites</h2>

  <ul>
    <li>Python 3.x</li>
    <li>Required Python libraries: <code>beautifulsoup4</code>, <code>requests</code>, <code>win10toast</code></li>
  </ul>

  <h2>Usage</h2>

  <ol>
    <li><strong>Install Dependencies:</strong></li>
    <pre><code>pip install beautifulsoup4 requests win10toast</code></pre>
    <li><strong>Run the Script:</strong></li>
    <pre><code>python script.py</code></pre>
    <p>The script will refresh job posts every 20 minutes and save the information in the 'job posts' directory.</p>
  </ol>

  <h2>Notes</h2>

  <ul>
    <li>Make sure to respect the website's terms of service and use the scraper responsibly.</li>
    <li>Customize the script as needed based on changes to the website structure.</li>
  </ul>

  <h2>Disclaimer</h2>

  <p>This script is for educational and personal use only. The developer is not responsible for any misuse of this
    script.</p>

</body>

</html>
