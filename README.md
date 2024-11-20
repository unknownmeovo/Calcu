<h1>Simple Algebraic Calculator</h1>
    <p>
        A lightweight, feature-rich calculator for algebraic expressions and equations built with Python and Tkinter. 
        This project offers a dual approach:
    </p>
    <ul>
        <li>
            A <strong>lightweight remote version</strong> (<code>calcu_main.py</code>) that fetches the core code from the internet.
        </li>
        <li>
            A <strong>local customizable version</strong> (<code>calcu.py</code>) for offline use or code modifications.
        </li>
    </ul>
    <h2>Features</h2>
    <ul>
        <li>Solve algebraic expressions and equations.</li>
        <li>Preprocesses user input to handle implicit multiplications (e.g., <code>2x</code> → <code>2*x</code>).</li>
        <li>Supports symbolic variable definitions using the <code>sympy</code> library.</li>
        <li>Toggle between <strong>light mode</strong> and <strong>dark mode</strong> themes.</li>
        <li>Maintains a history of up to 10 calculations.</li>
        <li>Simple, user-friendly graphical interface built with Tkinter.</li>
    </ul>
    <h2>Bugs and Limitations</h2>
    <p>
        This project is still a work in progress and may contain bugs. Some known issues include:
    </p>
    <ul>
        <li>Unexpected behavior with certain edge-case algebraic inputs.</li>
        <li>Limited error handling for complex symbolic equations.</li>
    </ul>
    <p>
        Feel free to report any bugs or suggest improvements via the 
        <a href="https://github.com/unknownmeovo/Calcu/issues" target="_blank">Issues</a> page on GitHub.
    </p>
    <h2>Getting Started</h2>
    <h3>Prerequisites</h3>
    <p>Make sure you have Python 3 installed on your system. Additionally, install the required dependencies:</p>
    <pre>
<code>pip install sympy</code>
    </pre>
    <h3>Running the Calculator</h3>
    <h4>1. Lightweight Remote Version</h4>
    <p>
        If you prefer minimal local code and have internet access, run the following:
    </p>
    <pre>
<code>python3 calcu_main.py</code>
    </pre>
    <p>
        This script fetches the calculator logic from the internet, keeping your local setup clean and lightweight.
    </p>
    <h4>2. Local Customizable Version</h4>
    <p>For offline use or if you want to modify the code:</p>
    <pre>
<code>python3 calcu.py</code>
    </pre>
    <p>
        This script provides the full calculator interface and runs completely offline.
    </p>
    <h2>File Overview</h2>
    <ul>
        <li><code>calcu_main.py</code>: Lightweight version fetching the core code from the internet.</li>
        <li><code>calcu.py</code>: Full local version with the complete code for customization.</li>
    </ul>
    <h2>How It Works</h2>
    <ul>
        <li><strong>Expression Evaluation:</strong> Handles expressions like <code>2x + 3y - 4</code> or equations like <code>2x + 3y = 10</code>.</li>
        <li><strong>Preprocessing:</strong> Automatically adjusts user input for implicit multiplication.</li>
        <li><strong>History Management:</strong> Stores the last 10 calculations for reference.</li>
        <li><strong>Themes:</strong> Switch between light and dark modes for better usability.</li>
    </ul>
    <h2>License</h2>
    <p>
        This project is licensed under the 
        <a href="https://www.apache.org/licenses/LICENSE-2.0" target="_blank">Apache License 2.0</a>.
    </p>
    <h2>Contributing</h2>
    <p>Feel free to contribute! Fork this repository, make your changes, and open a pull request.</p>
    <h2>Author</h2>
    <p>Created by Hadi Raza.</p>
    <h2>Acknowledgements</h2>
    <ul>
        <li><a href="https://docs.python.org/3/library/tkinter.html" target="_blank">Tkinter Documentation</a></li>
        <li><a href="https://www.sympy.org/en/index.html" target="_blank">SymPy Library</a></li>
    </ul>
