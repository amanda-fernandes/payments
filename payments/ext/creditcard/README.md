# python-creditcard

A simple credit cards validation library in Python.

Heavily inspired on <https://github.com/contaazul/creditcard.js>

## Quickstart

Install using pip:

```
pip install python-creditcard
```

Basic usage:

```python
from creditcard import CreditCard

card_number = "4539578763621486"  # this is a Visa card
cc = CreditCard(card_number)
cc.is_valid()  # returns True
cc.get_brand()  # returns Visa
```

Handling Brands not yet implemented:

```python
from creditcard import CreditCard
from creditcard.exceptions import BrandNotFound

invalid_card = "1111111111111111"
cc = CreditCard(invalid_card)

try:
    brand = cc.get_brand()
except BrandNotFound:
    # do some magic
