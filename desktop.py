import webview
from threading import Thread, Event
from my_app import app


stop_event = Event()

app_title = "Jijna Flowbite Desktop Demo"
host = "http://127.0.0.1"
port = 5000

def run():
    while not stop_event.is_set():
        app.run(debug=True, port=port, use_reloader=False, threaded=True)

if __name__ == '__main__':
    t = Thread(target=run)
    t.daemon = True # This ensures the thread will exist when the main program exits.
    t.start()

    webview.create_window(
        app_title,
        f"{host}:{port}",
        width=1600,
        height=1200,
        text_select=True,
        resizable=True,
        easy_drag=True
    )

    webview.start()

    stop_event.set() # signal the flask server to shutdown.