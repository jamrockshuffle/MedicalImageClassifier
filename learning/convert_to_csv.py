import os
import pandas as pd


def main():
    train_folder = 'C:\\Users\\KB\\PycharmProjects\\MachineLearnTest\\archive\\compilation\\val\\'

    files_in_train = sorted(os.listdir(train_folder + 'PNEUMONIA\\')
                            + (os.listdir(train_folder + 'NORMAL\\'))
                            + (os.listdir(train_folder + 'TUBERCULOSIS\\'))
                            + (os.listdir(train_folder + 'COVID19\\'))
                            )

    images = [i for i in files_in_train]

    crutch = []
    for i in images:
        if str(i).__contains__("person"):
            crutch.append(train_folder + 'PNEUMONIA\\' + str(i))
        elif str(i).__contains__("IM"):
            crutch.append(train_folder + 'NORMAL\\' + str(i))
        elif str(i).__contains__("Tuberculosis"):
            crutch.append(train_folder + 'TUBERCULOSIS\\' + str(i))
        elif str(i).__contains__("COVID"):
            crutch.append(train_folder + 'COVID19\\' + str(i))

    df = pd.DataFrame(columns=['Filename'])
    df['Filename'] = [str(x) for x in crutch]
    df.loc[df['Filename'].str.contains('IM'), 'Label'] = "NORMAL"
    df.loc[df['Filename'].str.contains('person'), 'Label'] = "PNEUMONIA"
    df.loc[df['Filename'].str.contains('Tuberculosis'), 'Label'] = "TUBERCULOSIS"
    df.loc[df['Filename'].str.contains('COVID'), 'Label'] = "COVID19"

    df.to_csv('train/val.csv', columns=["Filename", "Label"])


if __name__ == "__main__":
    main()