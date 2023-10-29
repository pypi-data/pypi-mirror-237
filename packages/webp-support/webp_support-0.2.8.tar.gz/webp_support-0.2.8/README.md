# webp_supported

Quickly determine whether Webp is supported from UserAgent.

## support webp browser list

- FireFox >= 65
- Chrome >= 32
- Edge >= 18
- AppleWebKit >= 605 # Safari 14
- OPR >= 19
- UCBrowser >= 12
- SamsungBrowser >= 4
- QQBrowser >= 10

## using

`webp_supported(user_agent: bytes) -> bool`

example:

```python
from webp_support import webp_supported
user_agent = b"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
webp_supported(user_agent)    # Chrome > 32 -> True
```
