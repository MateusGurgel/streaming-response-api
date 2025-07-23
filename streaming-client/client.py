from rich.console import Console
import requests
from rich.live import Live
from rich.text import Text

console = Console()

console.print("This is [bold green]your[/bold green] lorem ipsum streaming client!", style="bold")

stream_url = "http://localhost:8000/"
stream_text = ""

with requests.get("http://localhost:8000/", stream=True) as response:
    response.raise_for_status()
    with Live(stream_text, console=console, refresh_per_second=60) as live:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:

                stream_text += chunk.decode("utf-8")
                stylish_text = Text(stream_text)
                stylish_text.stylize("green")
                live.update(stylish_text)