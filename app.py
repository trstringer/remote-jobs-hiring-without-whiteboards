"""List all remote jobs that don't do whiteboard hiring"""
import re
import requests


def hiring_without_whiteboards():
    """Get all companies that don't do whiteboard hiring"""

    # pylint: disable=line-too-long
    req = requests.get('https://raw.githubusercontent.com/poteto/hiring-without-whiteboards/master/README.md')
    return [
        re.search(r'^- \[(.*)\]', _).group(1)
        for _ in req.text.split('\n')
        if re.search(r'^- \[(.*)\]', _)
    ]


def remote_friendly_companies():
    """Get all companies that have remote job opportunities"""

    req = requests.get('https://raw.githubusercontent.com/jessicard/remote-jobs/master/README.md')

    regex_search = r'(\[(.*)\]|^(.*) \|.*\|)'
    return [
        re.search(regex_search, _).group(2)
        if re.search(regex_search, _).group(2)
        else re.search(regex_search, _).group(3)
        for _ in req.text.split('\n')
        if re.search(regex_search, _)
    ]


def main():
    """Main script execution"""

    no_whiteboard_companies = hiring_without_whiteboards()
    remote_companies = remote_friendly_companies()

    # pylint: disable=expression-not-assigned
    [print('- {}'.format(_)) for _ in no_whiteboard_companies if _ in remote_companies]  # NOQA

if __name__ == '__main__':
    main()
