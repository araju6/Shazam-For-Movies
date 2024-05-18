<!DOCTYPE html>
<html lang="en">
    <div class="container">
        <h1>Shazam for Movies</h1>
        <p>Shazam for Movies is a Python-based tool that identifies movies based on a dialogue quote provided by the user. It leverages web scraping and Named Entity Recognition (NER) to guess the possible movie titles from the given quote.</p>
        <h2>Features</h2>
        <ul>
            <li><strong>Google Search Integration</strong>: Fetches search results related to the provided quote.</li>
            <li><strong>Web Scraping</strong>: Extracts and cleans text from search results using BeautifulSoup.</li>
            <li><strong>Named Entity Recognition</strong>: Uses spaCy to identify movie titles from the extracted text.</li>
            <li><strong>User-Friendly GUI</strong>: Built with customtkinter to provide an intuitive interface for entering quotes and displaying results.</li>
        </ul>
        <h2>Installation</h2>
        <h3>Prerequisites</h3>
        <ul>
            <li>Python 3.x</li>
            <li>pip (Python package installer)</li>
        </ul>
        <h3>Clone the Repository</h3>
        <pre><code>git clone https://github.com/araju6/Shazam-For-Movies.git
cd Shazam-For-Movies</code></pre>
        <h3>Install Required Packages</h3>
        <pre><code>pip install beautifulsoup4 googlesearch-python requests spacy customtkinter
python -m spacy download en_core_web_sm</code></pre>
        <h2>Usage</h2>
        <ol>
            <li><strong>Run the Application:</strong>
            <pre><code>python main.py</code></pre></li>
            <li><strong>Enter a Movie Quote:</strong> Type a movie dialogue in the input field and click "Submit".</li>
            <li><strong>View the Result:</strong> The most likely movie title will be displayed.</li>
        </ol>
        <h2>Code Overview</h2>
        <h3>Main Components</h3>
        <ul>
            <li><strong>main.py</strong>: The main script that initializes the GUI and handles user input.</li>
            <li><strong>movieGetter()</strong>: Function that performs the Google search, web scraping, and NER to identify movie titles.</li>
            <li><strong>printer()</strong>: Function that updates the GUI with the identified movie title.</li>
        </ul>
        <h3>GUI Framework</h3>
        <p>Built with customtkinter. Provides an input field for the movie quote and displays the identified movie title.</p>
