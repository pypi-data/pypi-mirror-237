# Transurethral Resection Specimen Calculator

This package is designed to calculate the range of cassettes needed for a given specimen weight.

To install the package, use pip:

```
pip install turp
```

To use, simply instantiate a TurpCounter object with the specimen weight. 

```
turp = TurpCounter(24)

print(
    turp.weight,
    turp.num_cassette_low_end,
    turp.num_cassette_high_end,
    sep='\n'
)
```

The turp object attributes can be accessed directly or you can simply print the turp object to get the values.

```
print(turp)


TurpCounter(specimen_weight=24, num_cassette_low_end=9, num_cassette_high_end=11)
```