# Presentation Notebooks for space**tower**™ Software Development Kit

This package contains Jupyter notebooks demonstrating the features of the Software Development Kit (SDK) of space**tower**™ in Python. 

space**tower**™ is Exotrail's Flight Dynamics System (FDS). It covers all the needs of the flight dynamics engineer, including but not limited to :
- Orbit Determination using PV (Position-Velocity) or GPS NMEA measurements;
- Measurement Generation;
- Event prediction e.g. station passes;
- Generation and simulation of maneuvers e.g. for orbit raising;
- Uncertainties evaluation for all of these cases.

The Python SDK brings these features to you through a set of Python modules directly callable in your scripts. These modules interacts with the public Application Programming Interface (API) of space**tower**™ available online.

These notebooks aim at being resources for new users to understand how the SDK is built, as well as showcasing the performances of space**tower**™. They cover the most frequent use cases of an FDS.

## Contents

- Getting started
    - Getting started on your local device
    - Getting started online
- Usage
- Documentation
- Dependencies
- License
- Contact
- Version History


## Getting started

### Request an API key

To use the space**tower**™ SDK, you need to request an API key from Exotrail. This key will allow you to access the space**tower**™ API and use the SDK.

To do so, please register on [Exotrail's customer portal](https://portal.exotrail.space) and request access to the space**tower**™ API.

Once you have received your credentials, you can start using the SDK.

The methods `set_client_id` and `set_client_secret` of the `fds` module allows you to set your credentials.
You can then use the SDK as you wish.

```python
from fds.config import set_client_id, set_client_secret
set_client_id('your_client_id')
set_client_secret('your_client_secret')
```


### Getting started on your local device

If you want to run these notebooks on your local device, you need to have Python 3.11 or higher installed, with a package manager like pip. The procedure described hereafter also requires the use of a Command Line Interface (CLI) and the version control system Git.

Commands to run in the CLI will be written using the following  style.
```bash
myCommand
```

Start by opening a CLI in you working folder, and clone the presentation notebooks repository : 
```bash
git clone https://github.com/exotrail/spacetower-notebooks
```

Then, create a virtual environment where we will install and confine all the required dependencies (you might change the name of your virtual environment if you wish to): 
```bash 
python -m venv .venv 
```
Based on your operating system, you will have to activate the virtual environment differently. For Windows, you can use the following command :
```bash 
.\.venv\Scripts\activate`
``` 
or if you want to use the Powershell script:
```bash 
.\.venv\Scripts\Activate.ps1`
``` 
For Unix-based systems, you can use : 
```bash 
source .venv/bin/activate
```

For more details, please refer to the official Python documentation : https://docs.python.org/3/library/venv.html

Finally, install the space**tower**™ SDK and other dependencies with :
```bash 
pip install .
``` 

Once you have successfully installed this demonstration package with its dependencies, you can just run :
```bash
jupyter notebook
``` 
and the *JupyterLab* interface will run on your favorite browser.

### Getting started online

You can also access space**tower**™'s demonstration notebooks online, through a dedicated JupyterLab environment.

To do so, register on the [Exotrail's customer portal](https://portal.exotrail.space) and request access to the space**tower**™ Jupyter notebooks.

This should take you to the JupyterLab online environment where you can see and use the presentation notebooks.

## Usage

The JupyterLab interface presents you a file explorer view of this space**tower**™'s demonstration package.

Double-click on one of the .ipynb notebook to open it. You will then be able to execute the Python code inside it cell by cell.

We advise you to run them in the order in which they were written first. You can also edit these section to try out your ideas. For a more extensive documentation on how to use Jupyter, please refer to https://jupyter.org/ .

## Documentation

The reference documentation of space**tower**™'s Python SDK(Software Development Kit) used to write these notebooks can be found [here](https://docs.spacetower.exotrail.space/python-sdk/).

## Dependencies

As mentioned in the Getting started section, this demonstration package is written using Python 3.11, and relies on pip for installing dependencies.

Please refer to the README.md file of the space**tower**™ SDK project for a list of its dependencies.

## License

This package is distributed under the MIT License. You are free to use, modify, and distribute the software as you see fit, provided that the original copyright notice and this permission notice are included in all copies or substantial portions of the software.

The software is provided "as is," without warranty of any kind, express or implied.

For more details, please refer to the LICENSE file included in this repository.

## Contact

To get in touch with us, please send a mail to the Flight Dynamics Support service at 
fds-support@exotrailspace.onmicrosoft.com

## Version history

**[1.0.0]** 2024-05-TODO
- Initial release
    - First notebooks : Orbital elements plotting, stations passes