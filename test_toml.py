import tomllib

text = """

[window]

title = "Exp Check"
geometry = "800x500+500+300"
ui_conf = {bg = "black", borderwidth = 5}
theme_conf = {bg = "black", fg = "white"}
grid_config = {}

"""
print(tomllib.loads(text))

