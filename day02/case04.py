# 已写好的数据和函数，不用改

FEATURES = {
    'alarm':  {'label': '闹钟',  'desc': '到点提醒'},
    'timer':  {'label': '计时器','desc': '番茄工作法'},
    'stats':  {'label': '统计',  'desc': '查看记录'},
}

# 模拟某几个功能已开启（用 set 存已开启的）
ENABLED = {'alarm'}
def check_feature_exsit(feature:str) ->bool:
    if feature not in FEATURES:
        return False
    else:
        for i in ENABLED:
            if i == feature:
                return True
            else:
                return False

def ask(prompt:str)->str:
    v = input(prompt).strip()

    return v if v else None








def pick_features():
    status = {}
    missing = []
    print('检测alarm功能是否开启',end ='\n')
    for feature in FEATURES:
        if check_feature_exsit(feature):
            status[feature] = 'on'
        else:
            status[feature] = 'off'
        print(feature,status[feature])
        missing = [(feature,info) for feature,info in FEATURES.items() if status.get(feature) =='off']
    if len(missing) == 0:
        print('所有功能已开启')
        return
    else:
        print(f'共发现{len(missing)}个功能未开启')
        for ids,(feature,info) in enumerate(missing,1):

            print(f'{ids} {feature} {info} ')
    content = ask('请输入需要开启的编号')
    selected_idx = []
    if content == 'a':
        for ids,(feature,info) in enumerate(missing,1):
            selected_idx.append(ids)
    elif content == '0':
        print('未选择功能编号')
        return
    else:
        for i in content.replace('，',',').split(','):
            i = i.strip()
            if i.isdigit():
                idx = int(i)
                if 1<= idx <=len(missing):
                    selected_idx.append(idx)
    for selected_id in selected_idx:
        for ids,(feature,info) in enumerate(missing,1):
            if selected_id not in ids:
                print('用户没选任何编号')
                return
            else:
                label = info['label']
                print(f'已启用{label}')



if __name__ == '__main__':
    pick_features()