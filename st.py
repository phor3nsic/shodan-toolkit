import shodan
import argparse
import mmh3
import requests
import codecs

def disable_warnings():
    from requests.packages.urllib3.exceptions import InsecureRequestWarning
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def shodan_search(queryes, api_key):
    api = shodan.Shodan(api_key)
    hosts = []
    for x in queryes:
        try:
            result = api.search(x)
            for services in result['matches']:
                if services['ip_str'] not in hosts:
                    if ":" not in services['ip_str']: # NOT GET IPV6
                        hosts.append(services['ip_str'])
        except:
            pass

    for host in hosts:
        print(host)

def ssl_mode(domain, api_key):
    queryes = ["ssl:"+domain, "ssl.cert.subject.CN:"+domain]
    shodan_search(queryes, api_key)

def favicon_mode(url_favicon, api_key):
    disable_warnings()
    resp = requests.get(url_favicon, verify=False)
    favicon = codecs.encode(resp.content,"base64")
    hash_favicon = mmh3.hash(favicon)
    search_favicon = ["http.favicon.hash:"+str(hash_favicon)]
    shodan_search(search_favicon, api_key)

def main():

    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument("-k","--api_key", help="Api Key", required=True)
    parser.add_argument("-d", "--domain", help="Domain for search")
    parser.add_argument("-u", "--url", help="Url")
    parser.add_argument("-ssl","--ssl", help="SSL Search", action="store_true")
    parser.add_argument("-favicon","--favicon", help="Favicon Mode", action="store_true")
    args = parser.parse_args()

    if args.ssl == True:
        if args.domain:
            ssl_mode(args.domain, args.api_key)
        else:
            print("[!] Error: it's necessary to use -d/--domain")

    if args.favicon == True:
        if args.url:
            favicon_mode(args.url, args.api_key)
        else:
            print("[!] Error: it's necessary to use -u/--url")

if __name__ == "__main__":
    main()
    