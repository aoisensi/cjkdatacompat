from argparse import ArgumentParser
import json
from collections import OrderedDict
from typing import List, Dict

ap = ArgumentParser()
ap.add_argument('files', nargs='+', help='JSON files to process')
args = ap.parse_args()


def main():
    for name in args.files:
        with open(name, 'r', encoding='utf-8') as f:
            data: List[Dict] = json.load(f, object_pairs_hook=OrderedDict)

            def cond(v: Dict) -> bool:
                if v['op'] != 'replace':
                    return True
                if v['path'].endswith('/name'):
                    return False
                if v['path'].endswith('/description'):
                    return False
                if v['path'].endswith('/note'):
                    return False
                if v['path'].endswith('/message1'):
                    return False
                if v['path'].endswith('/message2'):
                    return False
                if v['path'].endswith('/name/jp'):
                    return False
                return True
            data = list(filter(cond, data))

            with open(name, 'w') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    main()
