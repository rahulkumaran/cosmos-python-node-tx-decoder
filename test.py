
from Naked.toolshed.shell import muterun_js

hash = "CqEBCp4BCiMvY29zbW9zLnN0YWtpbmcudjFiZXRhMS5Nc2dEZWxlZ2F0ZRJ3Ci1jb3Ntb3MxbjY0ZWxucGc1MGt2dWZ2NmZmejR2NnBsbXNkbGphYTZlMHJzanISNGNvc21vc3ZhbG9wZXIxYXdndXdmcm0yMnNoN3lld2t5d3JqdWp1a2M3NWEzcjN0cHdmeXAaEAoFdWF0b20SBzI1MDAwMDASZQpOCkYKHy9jb3Ntb3MuY3J5cHRvLnNlY3AyNTZrMS5QdWJLZXkSIwohAuG+31nz0/VQ2ylcYJsZ8kpfU41iCoRgQEIcggZyQFGLEgQKAggBEhMKDQoFdWF0b20SBDUwMDAQwJoMGkCdB1jBsSowAxBdtvAJV6d1ApfpPWFCRHxWmE1wtOa4M0QwV/TKCxqW2h1+1GR/1uSDqAKb0Q9ycufp+uwUgqcC"

response = muterun_js('temp.js', hash)

if response:
    special_chars = ['\n', " ", "'", "delegatorAddress", "validatorAddress",  "amountdenomuatom", "amount", "{", "}", ":"]

    output = (response.stdout)
    output = output.decode("utf-8")[:-2]

    for char in special_chars:
        output = output.replace(char, "")

    output = output.split(",")

    print(output)
else:
    print(response)
