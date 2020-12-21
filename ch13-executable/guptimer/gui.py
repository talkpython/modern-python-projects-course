import tkinter as tk

from guptimer.helpers import check_url

# Dictionary to map statuses to color tags
COLORS = {
    2: "green",
    3: "yellow",
    4: "bright_red",
    5: "red",
}


def main():
    """Draw a GUI for checking URLs"""

    def check_urls():
        # Grab text from URLs box and split it
        urls_string = urls_box.get("1.0", tk.END)
        urls = urls_string.rstrip().split("\n")
        # Remove the "disabled" state from the response box, so we can edit it
        response_box.configure(state="normal")
        # Remove all current content
        response_box.delete("1.0", tk.END)
        for line, url in enumerate(urls, start=1):
            status_code = check_url(url)
            if status_code:
                # Write HTTP status next to each URL ...
                response_box.insert(tk.END, str(status_code) + "\n")
                # ... and colorize it
                fg_color = COLORS.get(status_code // 100, "magenta")
                response_box.tag_add(fg_color, f"{line}.0", f"{line}.9")
            else:
                response_box.insert(tk.END, "Wrong URL!\n")
                response_box.tag_add("magenta", f"{line}.0", f"{line}.9")
        # Disable the response box, so users can't edit it
        response_box.configure(state="disabled")

    # Create a new window
    window = tk.Tk()
    # Add gray background
    window.config(bg="#f6f6f6")

    # Add label in the first row
    tk.Label(window, text="URLs to check (one per line)").grid(row=0)

    # Add a text box where users can input URLs
    urls_box = tk.Text(window, height=20, width=50)
    urls_box.grid(row=1, column=0)

    # Add a "disabled" textbox where we display response codes
    response_box = tk.Text(
        window,
        height=20,
        width=10,
        state="disabled",
        bg="#f6f6f6"
    )
    response_box.grid(row=1, column=1)

    # Tags can be used to change text color in a text box
    response_box.tag_config("green", foreground="#9CCC65")
    response_box.tag_config("yellow", foreground="#FF9800")
    response_box.tag_config("bright_red", foreground="#EF5350")
    response_box.tag_config("red", foreground="#C62828")
    response_box.tag_config("magenta", foreground="#9C27B0")

    # Add a button and connect it to a check_urls function
    check_button = tk.Button(window, text="Check", command=check_urls)
    check_button.grid(row=2)

    # Start main event loop, so our program will respond to button clicks
    window.mainloop()


# Test URLs:
# http://httpstat.us/200
# http://httpstat.us/301
# http://httpstat.us/404
# http://httpstat.us/500

if __name__ == "__main__":
    main()
