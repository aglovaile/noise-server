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
        * `octaves=[int]`
        * `lacunarity=[float]`
        * `persistence=[float]`
        * `base=[int]`
    
* **Data Params**
    * None

* **Success Response**
    * Code: 200
    * Content-Type: application/json
    * Content: 
    ``` json
    {
        "dimensions": [ dimension1=[int], ... ],
        "octaves": int,
        "persistence": float,
        "lacunarity": float,
        "base": int,
        "data": [ Array of Perlin noise ]
    }
    ```
