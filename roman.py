import re


def int_to_roman(num: int):
    roman = ""
    ROMAN_SYM = reversed(
        [("I", 1), ("IV", 4), ("V", 5), ("IX", 9), ("X", 10), ("XL", 40), ("L", 50), ("XC", 90), ("C", 100),
         ("CD", 400), ("D", 500), ("CM", 900), ("M", 1000)])
    for sym_int_pair in ROMAN_SYM:
        multiplier = num // sym_int_pair[1]
        roman += sym_int_pair[0] * multiplier
        num -= sym_int_pair[1] * multiplier
    return roman


def romanizer(numbers):
    roman_nums = []
    for num in numbers:
        # roman = ""
        # for sym_int_pair in ROMAN_SYM:
        #     multiplier = num // sym_int_pair[1]
        #     roman += sym_int_pair[0] * multiplier
        #     num -= sym_int_pair[1] * multiplier
        roman_nums.append(int_to_roman(num))
    # return [str(num) for num in numbers]
    return roman_nums


def find_domains(lines):
    domains = []
    url_regex = "(http:\/\/|https:\/\/)(www.|ww2.|web.)?(?P<domain>[a-z0-9\-]+.[a-z]+)(\/)?"
    pattern = re.compile(url_regex)
    for line in lines:
        for url_match in pattern.finditer(line):
            if "domain" in url_match.groupdict():
                domains.append(url_match["domain"])
    domains.sort()
    return ",".join(domains)


if __name__ == "__main__":
    print(find_domains(["""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.com/TR/xhtml1/DTD/xhtml1-transitional.dtd" "http://www.aw3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">"""]))
    # print(romanizer([1, 2, 3, 4, 5]))
    # print(int_to_roman(2))
