# AzCam Server

*azcam-server* is the main server application for the *azcam* acquisition and analysis package. It usually runs in an IPython window and is mainly used to control data acquistion. 

## Documentation

See https://azcam.readthedocs.io/.

## Installation

`pip install azcam-server`

Or download the latest version from from github: https://github.com/mplesser/azcam-server.git.

## Configuration and startup 

An example code snippet to start an *azcamserver* process is:

```
ipython -m azcam_server.server_mock --profile azcamserver  -i
```

and then in the IPython window:

```python
instrument.set_wavelength(450)
wavelength = instrument.get_wavelength()
print(f"Current wavelength is {wavelength}")
exposure.expose(2., 'flat', "a 450 nm flat field image")
```
