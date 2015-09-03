Future Proof Basic Data Types
=============================

Moving into the future, it is difficult to predict what qualities computers will have.

Based on the simple predictions of:

increases in memory, processing speed, and parallelism.

A programming paradigm capable scaling with those changes without modification offers use a method for ensuring programs and data are accessible well into the future. (at least in the perspective from computing)

Such data types should:
- not ascribe to a "word size" or other upper limit
- be arbitrary precision (able to represent any value in their domain)

The basic datatype is a "bytestring"
====================================

Bytestrings are finite lengths of bytes that can hold any value.
Rather than null termination or similar encoding based termination detection,
bytestings' length is indicated by a prefix.

```
[length][raw bytestring]
```

becuase the length itself is comprised of an unknown number of bytes, it is indicated using a
varint format. The higest bit of each byte before the last byte is set to one, and finally the highest bit of last byte is set to 0.
The length itself is incoded using base 128, utilizing the last 7 bits of the byte.
While this format does offer some "wasted bits", it does not change the O(log(n)) storage behavoir.

We can make more types by composing bytestrings
===============================================

```
[varint struct length][[bytestring struct type] [ ... list of bytestrings that compose the structure]]
```

structure type IDs can be part of a standard set, or UUID style values can be used for user customized structures (hash of a struct description?)

Basic types and IDs:
- 0: boolean value
- 1: signed integers
- 2: rational numbers
- 3: arbitrary accuracy floating point (do we need this? Direct encoding of irrational numbers does not seem viable)
- 4: generalized fixed length arrays

Boolean values
==============
While booleans may be considered a special case of integer by many systems, for clarity and space saving:

False = x04x01x00x01x00 <- five bytes in total
True  = x04x01x00x01x01

operations: AND, OR, NEGATE

Signed integers
===============
This format is for signed integers, there is no format for unsigned integers (just don't use the sign!) as the only argument would be backwards compatibility
