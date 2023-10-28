# Python I2C Driver for Sensirion SHT3X

This repository contains the Python driver to communicate with a Sensirion sensor of the SHT3X family over I2C. 

<img src="https://raw.githubusercontent.com/Sensirion/python-i2c-sht3x/master/images/SHT3x.png"
    width="300px" alt="SHT3X picture">


Click [here](https://sensirion.com/products/catalog/SHT30-DIS-B) to learn more about the Sensirion SHT3X sensor family.


Not all sensors of this driver family support all measurements.
In case a measurement is not supported by all sensors, the products that
support it are listed in the API description.



## Supported sensor types

| Sensor name   | I²C Addresses  |
| ------------- | -------------- |
|[SHT30A](https://sensirion.com/products/catalog/SHT30A-DIS-B)| **0x44**, 0x45|
|[SHT30](https://sensirion.com/products/catalog/SHT30-DIS-B)| **0x44**, 0x45|
|[SHT31A](https://sensirion.com/products/catalog/SHT31A-DIS-B)| **0x44**, 0x45|
|[SHT31](https://sensirion.com/products/catalog/SHT31-DIS-B)| **0x44**, 0x45|
|[SHT33](https://sensirion.com/products/catalog/SHT33-DIS)| **0x44**, 0x45|
|[SHT35A](https://sensirion.com/products/catalog/SHT35A-DIS-B)| **0x44**, 0x45|
|[SHT35](https://sensirion.com/products/catalog/SHT35-DIS-B)| **0x44**, 0x45|

The following instructions and examples use a *SHT30*.



## Connect the sensor

You can connect your sensor over a [SEK-SensorBridge](https://developer.sensirion.com/sensirion-products/sek-sensorbridge/).
For special setups you find the sensor pinout in the section below.

<details><summary>Sensor pinout</summary>
<p>
<img src="https://raw.githubusercontent.com/Sensirion/python-i2c-sht3x/master/images/SHT3x_pinout.png"
     width="300px" alt="sensor wiring picture">

| *Pin* | *Cable Color* | *Name* | *Description*  | *Comments* |
|-------|---------------|:------:|----------------|------------|
| 1 | green | SDA | I2C: Serial data input / output | 
| 2 | black | GND | Ground | 
| 3 | yellow | SCL | I2C: Serial clock input | 
| 4 | red | VDD | Supply Voltage | 2.15V to 5.5V


</p>
</details>


## Documentation & Quickstart

See the [documentation page](https://sensirion.github.io/python-i2c-sht3x) for an API description and a 
[quickstart](https://sensirion.github.io/python-i2c-sht3x/execute-measurements.html) example.


## Contributing

We develop and test this driver using our company internal tools (version
control, continuous integration, code review etc.) and automatically
synchronize the `master` branch with GitHub. But this doesn't mean that we
don't respond to issues or don't accept pull requests on GitHub. In fact,
you're very welcome to open issues or create pull requests :-)

### Check coding style

The coding style can be checked with [`flake8`](http://flake8.pycqa.org/):

```bash
pip install -e .[test]  # Install requirements
flake8                  # Run style check
```

In addition, we check the formatting of files with
[`editorconfig-checker`](https://editorconfig-checker.github.io/):

```bash
pip install editorconfig-checker==2.0.3   # Install requirements
editorconfig-checker                      # Run check
```

## License

See [LICENSE](LICENSE).
