"""
word 配置
"""
LOC = {'project_name': (0, 1), 'client': (1, 1), 'testNo': (2, 1),
       'Examined': (0, 1), 'Reviewed': (1, 1), 'Approved': (2, 1), 'Date': (4, 1)
       }

DATA = {
    'cover_1': {'project_name': '测试项目', 'client': '天地皇家建设工程部门', 'testNo': 'No.122321312131'},
    'cover_2': {'Examined': ('张攀', 'Pan Zhang'), 'Reviewed': ('张攀', 'Pan Zhang'), 'Approved': ('鲁全峰', 'Quanfeng Lu'),
                'Date': ('2021/03/03', None)},
}
