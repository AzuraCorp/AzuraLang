# AzuraLang# What is AzuraLang?
Azuralang is a python-library/toolkit to easily make Python-based apps using tTk¹.
>¹tTk = themed Tkinter, a python library to make better looking/themed tkinter windows/apps.

It is a high-level library, that is really easy to use, mod and contribute.

## Installation
### Stable releases:
#### Normally to install Azuralang you can use pip:
```bash
pip install azuralang
```
#### For linux(only if the PEP 668/externally managed envirement error):
```bash
pip install azuralang --break-system-packages
```
or(Arch linux, not tested)
```bash
pacman -Suy python-azuralang
```
or(Ubuntu/Debian, also not tested)
```bash
apt upgrade && apt update
apt install python-azuralang
```
### ADaC(AllDistributions and Commits) channel
>[!NOTE]
>This way you'll get all the new features asap, but some distribution/versions/commits have bugs or aren't stable to    use normally - so be carefull!

#### Building(inclusive Betas and Alphas, f. e.: vBETA-1, vF-10 and vPreREL-3)
>[!WARNING]
>Currently, we don't support Windows/OSX for building the core files! 
>We reccomend to use Arch(Manjaro), because of untested Ubuntu-, Debian- and RPM-based system-behaving!

1. Clone the repo: `git clone https://github.com/AzuraCorp/AzuraLang/tree/main`
2. Enter the folder: `cd AzuraLang`
3. Build! `bash build.bash` or `sh build.bash`

#### Use the builded files(only PreReleases and Full versions, f. e.: vPreREL-3 and vF-10)
