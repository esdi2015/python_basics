
def parse_line(line):
    line_ip = line.split('- -')
    line_client = line_ip[1].strip().split('"')[5]
    return line_ip[0].strip(), line_client.strip()


def log_data_gen(log_file):
    with open(log_file, 'r', encoding='utf-8') as f:
        for line in f:
            if line:
                parsed_line = parse_line(line)
                yield parsed_line


if __name__ == '__main__':
    logs_file = 'nginx_logs.txt'
    log_data = log_data_gen(logs_file)
    log_data_dict = {}

    for ld in log_data:
        log_data_dict[ld] = log_data_dict.get(ld, 0) + 1

    spammer = list(sorted(log_data_dict.items(), key=lambda item: item[1], reverse=True)[0])

    print('ip: {}, client: {}, requests count: {}'.format(spammer[0][0], spammer[0][1], spammer[1]))
