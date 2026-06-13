import subprocess, sys, os

chrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
html_file = sys.argv[1]
png_file = sys.argv[2]

subprocess.run([
    chrome, "--headless=new", "--disable-gpu", "--no-sandbox",
    f"--screenshot={png_file}", f"--window-size=1280,900",
    f"file://{os.path.abspath(html_file)}"
], check=True, timeout=15000)
print(f"Screenshot saved: {png_file}")
