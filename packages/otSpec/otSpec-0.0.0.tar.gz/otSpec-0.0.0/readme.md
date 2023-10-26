# otSpec

## What is it?

This package contains some useful constants and functions to deal with 
the [OpenType® Specification](https://learn.microsoft.com/de-de/typography/opentype/spec/).

## How to install it?

```shell
pip install otSpec
```

## How to use it?

```python
>>> from otSpec.table.name import getNameDescription
>>> getNameDescription(nameID=3)
'Unique Font Identifier'

>>> from otSpec.table.head import getMacStyleBitNames
>>> getMacStyleBitNames(3)
['Bold', 'Italic']
```

## What's next

For details read the full [Documentation](https://fontstuff.gitlab.io/otSpec).
