import argparse
import translation

languages = ['arabic', 'german', 'english', 'spanish', 'french', 'hebrew', 'japanese',
             'dutch', 'polish', 'portuguese', 'romanian', 'russian', 'turkish']


def check_languages(lng_from, lng_to):
    if lng_from not in languages and lng_from != 'all':
        print(f"Sorry, the program doesn't support {lng_from}")
        exit()
    if lng_to not in languages and lng_to != 'all':
        print(f"Sorry, the program doesn't support {lng_to}")
        exit()


def translate(lng_from, lng_to, user_word):
    word = translation.Translation(user_word, lng_from)

    if lng_to == 'all':
        languages.remove(lng_from)
        for lng_to in languages:
            word.translate(lng_to)
            word.get_results(1)
    else:
        word.translate(lng_to)
        word.get_results()

    return word.output


def main():
    #for n in range(len(languages)):
        #print(f'{n + 1}. {languages[n]}')
    parser = argparse.ArgumentParser()
    parser.add_argument("lng_from",
                        help=f"Choose the language from which to translate from - {languages}")
    parser.add_argument("lng_to",
                        help=f"Choose the language from which to translate from - {languages}")
    parser.add_argument("user_word")
    args = parser.parse_args()

    lng_from_ = args.lng_from.lower()
    lng_to_ = args.lng_to.lower()
    user_word_ = args.user_word.lower()
    check_languages(lng_from_, lng_to_)

    results = translate(lng_from_, lng_to_, user_word_)

    print(results)
    with open(f'{user_word_}.txt', 'w', encoding='utf-8') as f:
        f.write(results)


if __name__ == '__main__':
    main()
