def validate_url(url):
    assert isinstance(url, str), f"{url} 应该是一个字符串"
    if not url.startswith(("http://", "https://")):
        return "http://" + url
    return url
