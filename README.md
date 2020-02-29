# Web-API

[droneraising](https://droneraising.com) REST APIs.

## Requirements
Python 3.6+

## Installation
In the root project execute the following command to install all dependencies project

```
pip install -r requirements.txt
```

You will also need an ASGI server, for production such as <a href="http://www.uvicorn.org" class="external-link" target="_blank">Uvicorn</a> or <a href="https://gitlab.com/pgjones/hypercorn" class="external-link" target="_blank">Hypercorn</a>.

```bash
pip install uvicorn
```

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

### Example of output prediction
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
