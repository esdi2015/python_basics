import re


def email_parse(email_address):
    regex = r'^(?P<username>[a-zA-Z0-9_.+-]+)[@](?P<domain>[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)$'
    matches = re.search(regex, email_address)
    if not matches:
        msg = 'wrong email: {}'.format(email_address)
        raise ValueError(msg)
    else:
        return matches.groupdict()


if __name__ == '__main__':
    good_email = 'testemail@dot.com'
    print(email_parse(good_email))

    bad_email = 'testemaildot.com'
    print(email_parse(bad_email))

