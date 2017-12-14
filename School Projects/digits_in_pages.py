
def main():

    def count_the_number(pages):
        """Counts the number of digits used for pages"""

        i = len(str(pages))  # index of number of pages

        if i == 1:  # The case of one digit number
            total_sum = pages

        else:
            base_sum = 9  # sum of page digits till the index
            # Calculation of base sum
            for x in range(2, i):
                base_sum += (x * 9 * (10 ** (x - 1)))
            # Calculation of reminder sum
            reminder_sum = (pages - int((i - 1) * '9')) * i
            # Calculation of total sum
            total_sum = base_sum + reminder_sum

        print('\n\tTotal number of digits: ' +
              str('{0:,}'.format(total_sum).replace(',', ' ')))

        # print('\n\tChecking... ')
        # stringas = ''
        # for item in range(1, pages + 1):
        #     stringas += str(item)
        # print('\t' + str('{0:,}'.format(int(len(stringas))).replace(',', ' ')))


    while True:
        try:
            print('\n\n\tEnter 0 to quit or')
            pages = int(input('\tenter a number of page: '))
            if pages == 0:
                break
            count_the_number(pages)
        except ValueError:
            print('\n\tI will accept only an integer, try again.')


if __name__ == '__main__':
    main()
