import random
import string
import datetime


def get_random_string(size):
    return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(size))


def get_random_phrase(word_size_interval, words_interval):
    phrase = ""
    words_range = range(0, random.choice(range(*words_interval)))
    if len(words_range) > 0:
        last_idx = words_range[len(words_range) - 1]
        for i in words_range:
            phrase += get_random_string(random.choice(range(*word_size_interval)))
            if i != last_idx:
                phrase += " "
    return phrase.decode('utf-8')


def get_random_digit():
    return random.choice(string.digits)


def get_random_price():
    s = get_random_digit()
    if random.uniform(0, 1) < 0.5:
        s += get_random_digit()
    s += "."
    s += get_random_digit()
    s += get_random_digit()

    return s


def get_random_tel():
    tel = "("
    for i in range(0, 2):
        tel += get_random_digit()
    tel += ") "
    include_nine = random.choice([True, False])
    if include_nine:
        tel += "9"
    for i in range(0, 4):
        tel += get_random_digit()
    tel += "-"
    for i in range(0, 4):
        tel += get_random_digit()
    return tel


def get_random_cep():
    cep = ""
    for i in range(0, 5):
        cep += get_random_digit()
    cep += "-"
    for i in range(0, 3):
        cep += get_random_digit()
    return cep


def get_random_datetime(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + datetime.timedelta(seconds=random_second)
