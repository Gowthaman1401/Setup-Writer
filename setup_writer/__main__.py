import argparse
from Setup import *
from colorama import *

init(convert=True)


def get_argument():
    parser = argparse.ArgumentParser(usage="pip-setup [options]", epilog='Press ENTER For default input')
    parser.add_argument('-v', '--version', action='version', help='show version number and exit', version="1.0.0")
    group = parser.add_argument_group("to show help")
    group.add_argument("--print-default", default=False, action='store_true', help='show default values and exit')
    group.add_argument("--classifier", default=False, metavar='', help='show the available in classifier category')
    group.add_argument("--avail-classifier", default=False, action='store_const', const='all',
                       help='show all the available classifiers')
    group.add_argument("--classifier-category", default=False, action='store_true', help=argparse.SUPPRESS)
    parser.add_argument_group(group)
    options = parser.parse_args()
    return options


def get_upload_argument():
    parser = argparse.ArgumentParser(usage="pip-upload [options]", )
    parser.add_argument('-v', '--version', action='version', help='show version number and exit', version="1.0.0")
    group = parser.add_argument_group("to help in uploading your package")
    group.add_argument("-u", "--upload-to", default='test pip', metavar='',
                       help='either real pip or test pip (default: %(default)s)')
    group.add_argument("-p", "--path", default=os.getcwd(), metavar='', help='path to the package (default: %(default)s))')
    parser.add_argument_group(group)
    options = parser.parse_args()
    return options
  
  
  def main():
    try:
        option = get_argument()
        setup = Setup()
        if option.print_default:
            setup.print_default()
        elif option.classifier_category:
            Classifiers().categorize_classifiers(wanted='category')
        elif option.avail_classifier:
            option.avail_classifier = option.avail_classifier.replace(', ', ',').split(',')
            Classifiers().categorize_classifiers(categories=option.avail_classifier)
        elif option.classifier:
            option.classifier = option.classifier.replace(', ', ',').split(',')
            Classifiers().categorize_classifiers(categories=option.classifier)
        else:
            setup.write()
    except KeyboardInterrupt:
        print(Fore.GREEN + "\n\n[" + Fore.WHITE + "-" + Fore.GREEN + "] " + Fore.WHITE + "Keyboard Interruption Occurred")
    except Exception as e:
        raise e


def upload_main():
    try:
        option = get_upload_argument()
        upload(option.path, option.upload_to)
    except KeyboardInterrupt:
        print(Fore.GREEN + "\n[" + Fore.WHITE + "-" + Fore.GREEN + "] " + Fore.WHITE + "Keyboard Interruption Occurred")


if __name__ == '__main__':
    pass
