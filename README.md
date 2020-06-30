# Web-API
[![Build Status](https://api.travis-ci.org/RentadroneCL/Web-API.svg)](https://travis-ci.org/github/RentadroneCL/Web-API)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://www.mypy-lang.org)

[Rentadrone.cl](https://rentadronecl.github.io)

API specification for deploy the [detection models](https://github.com/RentadroneCL/model-definition/blob/master/README.md), this repository contains a performant, production-ready reference implementation.

## Documentation
See [https://rentadronecl.github.io/docs](https://rentadronecl.github.io/docs/detection-models) for tutorials and more guides.

## Developers
Help improve our software! We welcome contributions from everyone, whether to add new features, improve speed, fix existing bugs or add support. [Check our code of conduct](CODE_OF_CONDUCT.md), [the contributing guidelines](CONTRIBUTING.md) and how decisions are made.

## Requirements
Python 3.6+

## Quickstart
In the root project execute the following command to install all dependencies project

```
pip install -r requirements.txt
```

You will also need an ASGI server, for production such as <a href="http://www.uvicorn.org" class="external-link" target="_blank">Uvicorn</a> or <a href="https://gitlab.com/pgjones/hypercorn" class="external-link" target="_blank">Hypercorn</a>.

```bash
pip install uvicorn
```

## Configuration
### Configuration Files
All of the configuration files for the API  are stored in the `config` directory. Each option is documented, so feel free to look through the files and get familiar with the options available to you.

### Application Key
The next thing you should do after installing is set your application key to a random string.

Typically, this string should be 32 characters long. The key can be set in the `.env` environment file. If you have not copied the `.env.example` file to a new file named `.env`, you should do that now. If the application key is not set, your user sessions and other encrypted data will not be secure!

### Model Configuration
The model that we are going to deploy is for predicting photovoltaic fault. You can get the data [here](https://github.com/RentadroneCL/model-definition).

We start by loading the data and compiled models into the `storage/model` folder and the configuration files for each model in the `storage/config` folder and saving the names of the features that we want to use in our model.

### Example model configuration file
```js
{
  "model": {
    "min_input_size": 400,
    "max_input_size": 400,
    "anchors": [5,7, 10,14, 15, 15, 26,32, 45,119, 54,18, 94,59, 109,183, 200,21],
    "labels": ["1"],
    "backend": "full_yolo_backend.h5"
  }
}
```

After we have prepared the data and saved all necessary files it is time to start creating the API to serve our model from.

**NOTE:** There are several methods for saving a model, each with its own sets of pros and cons you may change in function of your necesities.

### Run it

Run the server with:

```bash
uvicorn run:app --reload
```

<details markdown="1">
<summary>About the command <code>uvicorn run:app --reload</code>...</summary>

The command `uvicorn run:app` refers to:

* `run`: the file `run.py` (the Python "module").
* `app`: the object imported inside of `run.py` with the line `from app import app`.
* `--reload`: make the server restart after code changes. Only do this for development.

</details>

You already created an API that:

* Receives HTTP requests in the _path_ `/prediction`.
* `/prediction` _path_ take `POST` <em>operations</em> (also known as HTTP _methods_).
* The _path_ parameter should be parse as `json` object.
* If the mimetype does not indicate JSON `application/json` this returns `None`.

### Example of an input data
```js
[
  {
    "id": 3,
    "url": "https://domain.com/storage/3/0074.jpg"
  },
  {
    "id": 6,
    "url": "https://domain.com/storage/6/0045.jpg"
  },
  {
    "id": 7,
    "url": "https://domain.com/storage/7/0055.jpg"
  },
  {
    "id": 8,
    "url": "https://domain.com/storage/8/0024.jpg"
  },
  {
    "id": 2,
    "url": "https://domain.com/storage/2/0078.jpg"
  },
  {
    "id": 5,
    "url": "https://domain.com/storage/5/0091.jpg"
  },
  {
    "id": 4,
    "url": "https://domain.com/storage/4/0089.jpg"
  }
]
```

### Viewing Results
```js
[
  {
    "id": 3,
    "url": "https://domain.com/storage/3/0074.jpg",
    "objects": []
  },
  {
    "id": 6,
    "url": "https://domain.com/storage/6/0045.jpg",
    "objects": [
      {
        "class": "1",
        "label": "Soiling Fault",
        "score": -1,
        "xmax": 98,
        "xmin": 86,
        "ymax": 100,
        "ymin": 100
      },
      {
        "class": "1",
        "label": "Soiling Fault",
        "score": -1,
        "xmax": 256,
        "xmin": 243,
        "ymax": 104,
        "ymin": 104
      },
      {
        "class": "4",
        "score": -1,
        "label": "Diode Fault",
        "xmax": 14,
        "xmin": 0,
        "ymax": 49,
        "ymin": 49
      },
      {
        "class": "4",
        "score": -1,
        "label": "Diode Fault",
        "xmax": 231,
        "xmin": 218,
        "ymax": 56,
        "ymin": 56
      },
      {
        "class": "4",
        "score": -1,
        "label": "Diode Fault",
        "xmax": 231,
        "xmin": 218,
        "ymax": 59,
        "ymin": 59
      }
    ]
  },
  {
    "id": 7,
    "url": "https://domain.com/storage/7/0055.jpg",
    "objects": []
  },
  {
    "id": 8,
    "url": "https://domain.com/storage/8/0024.jpg",
    "objects": []
  },
  {
    "id": 2,
    "url": "https://domain.com/storage/2/0078.jpg",
    "objects": [
      {
        "class": "4",
        "score": -1,
        "label": "Diode Fault",
        "xmax": 364,
        "xmin": 347,
        "ymax": 329,
        "ymin": 329
      },
      {
        "class": "4",
        "score": -1,
        "label": "Diode Fault",
        "xmax": 367,
        "xmin": 343,
        "ymax": 329,
        "ymin": 329
      },
      {
        "class": "4",
        "score": -1,
        "label": "Diode Fault",
        "xmax": 366,
        "xmin": 350,
        "ymax": 329,
        "ymin": 329
      },
      {
        "class": "4",
        "score": -1,
        "label": "Diode Fault",
        "xmax": 369,
        "xmin": 347,
        "ymax": 329,
        "ymin": 329
      },
      {
        "class": "4",
        "score": -1,
        "label": "Diode Fault",
        "xmax": 361,
        "xmin": 347,
        "ymax": 334,
        "ymin": 334
      },
      {
        "class": "4",
        "score": -1,
        "label": "Diode Fault",
        "xmax": 366,
        "xmin": 349,
        "ymax": 333,
        "ymin": 333
      },
      {
        "class": "4",
        "score": -1,
        "label": "Diode Fault",
        "xmax": 367,
        "xmin": 349,
        "ymax": 331,
        "ymin": 331
      }
    ]
  },
  {
    "id": 5,
    "url": "https://domain.com/storage/5/0091.jpg",
    "objects": []
  },
  {
    "id": 4,
    "url": "https://domain.com/storage/4/0089.jpg",
    "objects": []
  }
]
```

## Contribution guidelines

**If you want to contribute to Rentadrone.cl, be sure to review the
[contribution guidelines](CONTRIBUTING.md). This project adheres to Contributor Covenant's
[code of conduct](CODE_OF_CONDUCT.md). By participating, you are expected to
uphold this code.**

**We use [GitHub issues](https://github.com/RentadroneCL/model-definition/issues) for
tracking requests and bugs, please see

for general questions and discussion, and please direct specific questions to the team of
[Rentadrone.cl](mailto:contacto@rentadrone.cl).**

## [Code of Conduct](CODE_OF_CONDUCT.md)

The droneraising code of conduct is derived from the [Contributor Covenant](https://www.contributor-covenant.org). Any violations of the code of conduct may be reported to [Rentadrone.cl](mailto:contacto@rentadrone.cl)

## License

droneraising is open-sourced software licensed under the [MIT license.](LICENSE)
