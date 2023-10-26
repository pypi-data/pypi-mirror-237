"""
@Author: kang.yang
@Date: 2023/8/1 11:53
"""
import testadr

"""
定位方式：优先选择rid
rid: 根据resourceId进行定位
text：根据text属性进行定位
className：根据className属性进行定位
xpath：根据xpath进行定位
index：获取定位到的第index个元素
"""


class DemoPage(testadr.Page):
    """APP首页"""
    adBtn = testadr.Elem(rid='bottom_btn', desc='广告关闭按钮')
    myTab = testadr.Elem(text='我的', desc='我的tab')
    spaceTab = testadr.Elem(text='科创空间', desc='科创空间tab')
    """我的页"""
    settingBtn = testadr.Elem(rid='me_top_bar_setting_iv', desc='设置按钮')
    """设置页"""
    title = testadr.Elem(rid='tv_actionbar_title', desc='设置页标题')
    agreementText = testadr.Elem(rid='agreement_tv_2', desc='服务协议链接')

