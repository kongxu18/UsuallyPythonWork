import pandas as pd
import os


def modify_csv(file_dir):
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            fileName, extension = os.path.splitext(file)[0], os.path.splitext(file)[1]

            if extension == '.csv' or extension == '.CSV':
                print(files)
                try:
                    data = pd.read_csv(os.path.join(root, file), encoding='utf8')
                    data.to_excel(os.path.join(root, fileName + '.xlsx'))
                except Exception as err:
                    print('---')
                    file_data = []
                    with open(os.path.join(root, file), 'r') as f:
                        for i in f.readlines():
                            if i[-1] != ',':
                                last = i[-1]
                                i = i[:-1] + ',' + last
                            file_data.append(i)
                    with open(os.path.join(root, fileName + '.xlsx'), 'w') as f:
                        f.writelines(file_data)


modify_csv('/操作excel/单顶新构件号')
