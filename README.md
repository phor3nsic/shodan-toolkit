# Shodan Toolkit

> This tool aims to bring together some main forms of research by shodan and unite the ips, with each new form of interesting research a new module will be implemented.

## Usage

- Install:

```
git clone https://github.com/phor3nsic/shodan-toolkit.git
cd shodan-toolkit
pip3 -r requirements.txt
```

- Searchs:
	- ssl
	- favicon

### Help
```
python3 st.py [-h] -k API_KEY [-d DOMAIN] [-u URL] [-ssl] [-favicon]

optional arguments:
  -h, --help            show this help message and exit
  -k API_KEY, --api_key API_KEY
                        Api Key
  -d DOMAIN, --domain DOMAIN
                        Domain for search
  -u URL, --url URL     Url
  -ssl, --ssl           SSL Search
  -favicon, --favicon   Favicon Mode
```

-- SSL

```
python3 st.py -d twitter.com -k 96XABC123444CCADASDGG... -ssl

192.229.237.25
209.237.211.128
209.237.193.139
199.16.156.41
104.244.42.199

...
```

-- FAVICON

```
python3 st.py -u https://twitter.com/favicon.ico -k 96XABC123444CCADASDGG... -favicon

27.120.102.97
188.165.80.13
101.37.170.108
104.244.42.198
...
```

