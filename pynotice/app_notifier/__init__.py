from os.path import join, dirname

root = dirname(__file__)
app_notifier = join(root, "app-notifier")
exe = join(join(app_notifier, "bin"), "notifier")
