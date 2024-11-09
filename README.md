# Keygen95

Keygen95 is a simple Python module that generates valid Windows 95 RTM and OEM keys.

# Disclaimer

I do not condone software piracy. Windows 95 is considered abandonware and the key check algorithm is public knowledge at this point.

# Usage

There are 2 functions inside the keygen95.py file. `generateRetail()` and `generateOEM()`, which generate Retail and OEM keys respectfully. When you run both of these functions, they will return a randomized key you can use.
```
>>> import keygen95 as key
>>> key.generateRetail()
'281-5777011'
>>> key.generateOEM()
'11495-OEM-0331815-81212'
```

# Algorithm
The Windows 95 key checker is stupidly simple, *especially* for Retail copies. To start of, let's look at the latter.

### Retail

`XXX-YYYYYYY`

The first 3 characters are only checked with a simple blacklist. This means that they cannot be one of the following: `333`, `444`, `555`, `666`, `777`, `888`, `999`.

The last 7 characters are checked using an algorithm most commonly referred to as "mod7". You first take all the digits of Y and sum them up. Then, you check if the number you're left with is divisible by 7. If it is, the check passes.

The thing about the key validator in RTM copies is that it doesn't account for few things. First of all, the 3 digits at the beginning are *only* checked with the blacklist. This means that the installer doesn't check if they're even a number at all. The dash right after is also completely unchecked at all, which all of this combined with the nature of the mod7 algorithm, let's us create abominations of a key like `SEX-6666666` or `0000000000` that are technically considered "valid" Windows 95 keys.

The check in OEM copies is unfortunately (or fortunately depending on how you look at it) more strict and complicated than the RTM one, leaving less room for fun. That said, here's the structure of the key:

### OEM

`DDDYY-OEM-SSSSSSS-RRRRR`

The first 5 characters are an ordinal date the key was produced in. `DDD` ranges from 001 to 366 and `YY` does from 95 to 03 (years 1995-2003).

Next, `OEM` must remain the same at all times. Same with all of the dashes in the key.

`SSSSSSS` is the mod7 function we talked about earlier, with some modifications added to it. The algorithm is the same, except the installer also checks if the first digit is a zero, and the last doesn't equal to 0, 8 or 9.

The last 5 digits are not checked. (although they still need to be a number)