# dnsmine
Generate pairs of domain:IP by regexp to determine right domain\IP by obscured screenshot.

* Sometimes you have only a screenshot, with partially seen domain and ip. For example `nslookup` output.
This tool will help you determine what is that domain and what it's IP.

## Using
Edit 10 and 11 lines with right regexp for IP and Domain.
The predeterminated one shows regexp for "siiii.ru" domain and 31.31.205.163. (si*.ru and \*1.\*1.2\*5\*.1\*\*)

## Starting
```
pip install -r requirements.txt
python ./main.py
```

## Output
```
$ cat found.txt
Domain: sik.ru IP: 31.31.205.163
```
