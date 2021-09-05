# noise-server
![Image of Noise](https://raw.githubusercontent.com/aglovaile/noise-server/main/noise-server/static/811387.png)

An API server that returns Perlin noise to you.

## API Documentation

### Get Perlin noise as JSON
----

Returns a JSON object of Perlin noise depending on the provided dimensions and parameters.
Perlin noise can be rendered from 1D to 4D.
Noise dimensions are determined by how many are specified in the url.
Dimensions are specified in the URL ending with an 'x' between each dimension.
All requests to this url must be formatted as {X}x{Y}x{Z}x{W}.
Returned noise values will be floats between -1 and 1.


* **URL:**
    /api/noise/{dimensions in {X}x{Y}x{Z}x{W} format}

* **Method:**
    `GET`

* **URL Params:**
    * Optional
        * `octaves: int=1`
        * `lacunarity: float=2.0`
        * `persistence: float=0.5`
        * `base: int=0`
        * `scale: float=1.0`
        * `repeat: int=1024`    ** only used for 1d noise
        * `repeatx: int=1024`   ** only used for 2d noise
        * `repeaty: int=1024`   ** only used for 2d noise

    
* **Data Params**
    * None

* **Success Response**
    * Code: 200
    * Content-Type: application/json
    * Content: 
    ```
    {
        "dimensions": [ dimension1=[int], ... ],
        "octaves": int,
        "persistence": float,
        "lacunarity": float,
        "base": int,
        "scale": float,
        "data": [ Array of Perlin noise ]
    }
    ```

### Get Perlin noise as a PNG
----

Returns a PNG image of Perlin noise depending on provided dimensions and parameters. 
Url path must specify X and Y dimensions, other dimensions will be ignored.
If no Y dimension is specified, a square image of {X}x{X} will be returned.
By default a color image will be returned with colors ranging from #ffffff to #000000.

* **URL:**
    /api/png/{X}x{Y}

* **Method:**
    `GET`

* **URL Params:**
    * Optional
        * `octaves: int=1`
        * `persistence: float=0.5`
        * `lacunarity: float=2.0`
        * `base: int=0`
        * `scale: float=1.0`
        * `maxcolor: str='ffffff'`
        * `mincolor: str='000000'`
        * `grayscale: bool=False`

* **Data Params:**
    * None

* **Success Response:**
    * Code: 200
    * Content-Type: image/png