# ImageTextureFinder
A project to create an easy-to-use way of finding areas of common patterns and structures within an image. Should work on any image, designed for use on any biological images including DAPI, IMC and H&E.

See `sample_run.sh` for details.

- Branch `baseline` is the most stable. It is ready for pip packaging.
- Branch `pip` is stale at the moment
- Branch `dev` is unstable and for dev purposes only.


## Container
Image tag is `mkrooted/imbg-fastlbp`. Hosted on Docker Hub (https://hub.docker.com/repository/docker/mkrooted/imbg-fastlbp/general).
See https://github.com/imbg-ua/fastLBP-sandbox for details

---

# Guides

## How to build and deploy a pip package

Src: https://packaging.python.org/en/latest/tutorials/packaging-projects/

- Add your access token to `.pypirc`
    ```
    # ~/.pypirc 
    [pypi]
      username = __token__
      password = pypi-TOKEN_FROM_YOUR_PYPI_SETTINGS_GOES_HERE
    ```
- Ensure that your Python is 3.8 because the package targets Python 3.8 and thus requires to be build using this Python version
    ```
    python --version
    # Should show Python 3.8.something
    ```
- Install prerequisites (`twine` and `build`)
    ```
    pip install --upgrade twine build
    ```
- Edit project version in `pyproject.toml`
- Build and upload the project
    ```
    # while in root project directory
    python -m build      # .whl and .gz output will be at ./dist directory
    python3 -m twine upload dist/*   # note that this can accidentally upload unneeded builds
    ```

---

## Algorithm notes

Step 1 performs an LBP and creates histograms for each **method**.

**Method** is a combination of the following parameters:
- image name
- image channel
- LBP radius
- LBP number of points

Every method's result got saved into the separate `.npy` file. There is a correspondence betweeen a method and a computational job.

Step 2 collects all the results and concatenate them along the features dimension.
That means that feature vector of a patch is a concatenation of all LBP codes from all channels and all LBP radii. 

