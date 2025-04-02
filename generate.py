import make_logo

projects = {
    "scipp": {
        "prefix": "sci",
        "suffix": "pp",
        "footer": "",
        "color": "#0065ac",
    },
    "plopp": {
        "prefix": "plo",
        "suffix": "pp",
        "footer": "",
        "color": "#800080",
    },
    "chexus": {
        "prefix": "che",
        "suffix": "xus",
        "footer": "",
        "color": "#189ab4",
    },
    "scippneutron": {
        "prefix": "sci",
        "suffix": "pp",
        "footer": "neutron",
        "color": "#bdb2ff",
    },
    "scippnexus": {
        "prefix": "sci",
        "suffix": "pp",
        "footer": "nexus",
        "color": "#ff9d00",
    },
    "essreflectometry": {
        "prefix": "ess",
        "suffix": "",
        "footer": "reflectometry",
        "color": "#ff0000",
    },
}

for project, data in projects.items():
    make_logo.main(**data, output=f"{project}-logo.svg")
