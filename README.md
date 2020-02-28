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
uvicorn main:app --reload
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
