import pandas as pd
import os
excercise_file = 'C:\\Users\\Administrator\\Desktop\\\
Inline_Ex_Project\\InlineEx.xlsx'


def main():

    # Functions
    def num_of_sets():
        """Function to get input for desired number of sets of excercises."""
        print('\n\n' + 70 * '*' + "\n\t\tOK, how many sets?")
        while True:
            try:
                number_of_sets = int(input("\t\tEnter an integer please: "))
                break
            except ValueError:
                print("\n\t\tNope, I take integers only, try again.")
        return number_of_sets

    def create_list(number_of_sets, all_df):
        """Creates a list of random exc for each of different types found."""
        list_of_exc = []  # Create a list of random excercises
        for i in range(number_of_sets):
            for item in all_df:
                exc = list(item.sample(1).iloc[0])
                while exc in list_of_exc:
                    exc = list(item.sample(1).iloc[0])
                list_of_exc.append(exc)
        return list_of_exc

    xl = pd.ExcelFile(excercise_file)  # Import data frame of exc from Excel
    df = xl.parse('Exc')  # creates a data frame
    df = df.fillna(0)  # changes NaN values into 0
    # Create a list of unique types of exc
    types_of_exc = list(df.Type2.unique())

    all_df = []  # Create a list of separate data frames for every type of exc
    for item in types_of_exc:
        item = df.loc[df['Type2'] == item]
        # item = df.loc[df['Type'] == types_of_exc[types_of_exc.index(item)]]
        all_df.append(item)

    # START an algorithm
    list_of_exc = create_list(num_of_sets(), all_df)
    df_final = pd.DataFrame(list_of_exc)  # Change a list into a data frame
    df_final.columns = ('Excercise', 'Focus', 'Qty',
                        'Unit', 'Type1', 'Type2', 'Time')
    df_final.index += 1
    # Count total time
    total_time = df_final['Time'].sum() + 40 + len(df_final.index)

    # Output to terminal
    print('\n\tStart with a good warm-up, like Cardio' + '\t' + '~30 min.\n')
    print(df_final)
    print('\n\tDo not forget to strech-out:' + '\t' + '~10 min.')
    print('\tTotal time with 1 minute rests after each excercise: ~' +
          str(total_time) + ' min.')
    print('\n\tHave a nice work-out!\n' + 70 * '*')

    # Write into txt file
    with open('InlineExcList.txt', 'w') as f:
        f.write('\n\tStart with a good warm-up, like Cardio' +
                '\t' + '~30 min.\n')
        n = 1
        for x in list_of_exc:
            f.write(str('\n\t' + str(n) + '. ' + x[0]) + ', ' + x[2] +
                    ', ' + str(x[3]) + ', ' + x[4])
            n += 1
        f.write('\n\n\tDo not forget to strech-out:' + '~10 min.')
        f.write('\n\tTotal time with 1 minute rests\
 after each excercise: ~' + str(total_time) + ' min.')
        f.write('\n\n\tHave a nice work-out!\n')
    os.startfile('InlineExcList.txt')


if __name__ == '__main__':
    main()
