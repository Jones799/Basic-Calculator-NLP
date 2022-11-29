import re
from nltk.stem import WordNetLemmatizer
import decimal


wnl = WordNetLemmatizer()

Input = "what is three hundred and forty five plus two hundred and fifty three and a half"


def is_number(x):
    if type(x) == str:
        x = x.replace(',', '')
    try:
        float(x)
    except:
        return False
    return True

def text2int (textnum, numwords={}):
    units = [
        'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
        'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
        'sixteen', 'seventeen', 'eighteen', 'nineteen',
    ]
    tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    scales = ['hundred', 'thousand', 'million', 'billion', 'trillion']
    ordinal_words = {'first':1, 'third':3, 'fifth':5, 'eighth':8, 'ninth':9, 'twelfth':12}
    ordinal_endings = [('ieth', 'y'), ('th', '')]

    if not numwords:
        numwords['and'] = (1, 0)
        for idx, word in enumerate(units): numwords[word] = (1, idx)
        for idx, word in enumerate(tens): numwords[word] = (1, idx * 10)
        for idx, word in enumerate(scales): numwords[word] = (10 ** (idx * 3 or 2), 0)

    textnum = textnum.replace('-', ' ')

    current = result = 0
    curstring = ''
    onnumber = False
    lastunit = False
    lastscale = False

    def is_numword(x):
        if is_number(x):
            return True
        if word in numwords:
            return True
        return False

    def from_numword(x):
        if is_number(x):
            scale = 0
            increment = int(x.replace(',', ''))
            return scale, increment
        return numwords[x]

    for word in textnum.split():
        if word in ordinal_words:
            scale, increment = (1, ordinal_words[word])
            current = current * scale + increment
            if scale > 100:
                result += current
                current = 0
            onnumber = True
            lastunit = False
            lastscale = False
        else:
            for ending, replacement in ordinal_endings:
                if word.endswith(ending):
                    word = "%s%s" % (word[:-len(ending)], replacement)

            if (not is_numword(word)) or (word == 'and' and not lastscale):
                if onnumber:
                    # Flush the current number we are building
                    curstring += repr(result + current) + " "
                curstring += word + " "
                result = current = 0
                onnumber = False
                lastunit = False
                lastscale = False
            else:
                scale, increment = from_numword(word)
                onnumber = True

                if lastunit and (word not in scales):
                    # Assume this is part of a string of individual numbers to
                    # be flushed, such as a zipcode "one two three four five"
                    curstring += repr(result + current)
                    result = current = 0

                if scale > 1:
                    current = max(1, current)

                current = current * scale + increment
                if scale > 100:
                    result += current
                    current = 0

                lastscale = False
                lastunit = False
                if word in scales:
                    lastscale = True
                elif word in units:
                    lastunit = True

    if onnumber:
        curstring += repr(result + current)

    return curstring
def Convert(string):
    li = list(string.split(" "))
    return li



input1 = text2int(Input)

if " point " in input1:
    input2 = input1.replace(" point ", ".")

    if " point " in input2:
        input2 = input2.replace(" point ", ".")

    if " dot " in input2:

        input2 = input2.replace(" dot ", ".")

    if " and a half" in input2:
        input2 = input2.replace(" and a half", ".5")

elif " dot " in input1:
    
    input2 = input1.replace(" dot ", ".")
    
    if " point " in input2:
        input2 = input2.replace(" point ", ".")

    if " dot " in input2:
        input2 = input2.replace(" dot ", ".")

    if " and a half" in input2:
        input2 = input2.replace(" and a half", ".5")

elif " and a half" in input1:
    input2 = input1.replace(" and a half", ".5")
    if " point " in input2:
        input2 = input2.replace(" point ", ".")

    if " dot " in input2:
        input2 = input2.replace(" dot ", ".")

    if " and a half" in input2:
        input2 = input2.replace(" and a half", ".5")

else:
    input2 = input1


units = ["times", "plus", "subtract", "minus", "divide", "divided", "add", "multiply",
         "divided"]

units2 = (Convert(input2))


Calculations = {"times":"*", "plus":"+", "subtract":"-", "minus":"-", "divide":"/", "add":"+", "multiply":"*", "divided":"/"}



if any(x in Input for x in units):
    AllMatch = [x for x in units2 if x in units]
    calculationword = next((x for x in units2 if x in units), "False")
    FirstNumber = input2.split(calculationword, 1)[0]
    SecondNumber = input2.split(calculationword, 1)[1]
    if '.' in FirstNumber:
        first = (re.findall("\d+\.\d+", FirstNumber))
    else:
        first = (re.findall("[0-9]+", FirstNumber))
    if '.' in SecondNumber:
        second = (re.findall("\d+\.\d+", SecondNumber))
    else:
        second = (re.findall("[0-9]+", SecondNumber))
    first1 = ' '.join(map(str, first))
    second1 = ' '.join(map(str, second))
    result1 = (Calculations[calculationword])
    first2 = decimal.Decimal(first1)
    second2 = decimal.Decimal(second1)
    if '*' in result1:
        answer = first2 * second2
        answerround = "%.1f" % (answer)
        answer1 = str(answerround)
        print(first1 + ' times ' + second1 + ' is ' + answer1)
    if '/' in result1:
        answer = first2 / second2
        answerround = "%.1f" % (answer)
        answer1 = str(answerround)
        print(first1 + ' divided by ' + second1 + ' is ' + answer1)
    if '+' in result1:
        answer = first2 + second2
        answerround = "%.1f" % (answer)
        answer1 = str(answerround)
        print(first1 + ' plus ' + second1 + ' is ' + answer1)
    if '-' in result1:
        answer = first2 - second2
        answerround = "%.1f" % (answer)
        answer1 = str(answerround)
        print(first1 + ' minus ' + second1 + ' is ' + answer1)
else:
    print('I dont understand, what calculation do you want to know the answer to?')






