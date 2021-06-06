import re


RE_GET_PARSER = re.compile(r'^(?P<remote_addr>[0-9.]+).*'
                           r'(?P<request_datetime>\[.*\]+)\s+\"'
                           r'(?P<request_type>[A-Z]+)\s+'
                           r'(?P<requested_resource>[^\"]*)\"\s+'
                           r'(?P<response_code>[0-9]+)\s+'
                           r'(?P<response_size>[0-9]+).+$')


if __name__ == '__main__':
    result = []
    with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
        for log_string in f:
            matches = RE_GET_PARSER.search(log_string.strip())
            try:
                result.append(matches.groupdict())
            except ValueError as e:
                print(e.__repr__())

    print(result[:5])


