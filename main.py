from pkg.lib.CIEInterface import CIEInterface
import sys
import base64
import json


def main():
    birthDate = sys.argv[1]
    expireDate = sys.argv[2]
    cardId = sys.argv[3]

    interface = CIEInterface()
    interface.mrtdAuth(birthDate, expireDate, cardId)
    data = interface.extractData()

    data['photo'] = base64.b64encode(data['photo'])

    print(json.dumps(data))


if __name__ == "__main__":
    main()
